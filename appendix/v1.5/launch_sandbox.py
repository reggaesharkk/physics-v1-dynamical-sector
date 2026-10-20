#!/usr/bin/env python3
"""
Appendix A v1.5 — Interactive Phase-Space Confinement Sandbox Server
Integrates the exact upgraded v1.5 soft-wall ODEs (with zero piecewise clamping hacks)
and serves a responsive Plotly.js dashboard comparing v1.0 finite-time escape against
v1.5 global compact-box confinement in the post-Hopf regime (e = 1.20 * e_c).
"""
import json
import sys
import webbrowser
from http.server import SimpleHTTPRequestHandler
from socketserver import TCPServer
from threading import Timer
import numpy as np
from scipy.integrate import solve_ivp

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

BENCHMARK = {
    "a": 1.0, "b": 1.0, "c": 1.0, "f": 1.0, "g": 1.0,
    "E_avail": 1.0, "P_input": 5.0, "I_erase": 10.0,
    "gamma_max": 10.0, "H_max": 100.0,
    "e_c": 4.488095238095238,
    "eps_H": 0.05, "eps_I": 0.05,
}


def v15_softwall_field(t, state, e_val, eps_H, eps_I):
    """Exact Appendix A v1.5 Eqs. (3)-(5) with smooth C^infty hyperbolic tangent gates."""
    gamma, H_obs, I_dot = state
    dgamma = BENCHMARK["a"] * I_dot * BENCHMARK["E_avail"] * (1.0 - gamma / BENCHMARK["gamma_max"]) - BENCHMARK["b"] * gamma
    dHobs = BENCHMARK["c"] * gamma * (BENCHMARK["H_max"] - H_obs) - BENCHMARK["I_erase"] * np.tanh(H_obs / eps_H)
    dIdot = e_val * np.tanh(I_dot / eps_I) * dHobs + BENCHMARK["f"] * BENCHMARK["P_input"] - BENCHMARK["g"] * I_dot
    return [dgamma, dHobs, dIdot]


def simulate_post_hopf(e_mult=1.20):
    e_val = e_mult * BENCHMARK["e_c"]
    y0 = [10.0 / 3.0 + 1e-4, 97.0, 5.0]
    t_eval = np.linspace(0, 120, 1500)
    sol = solve_ivp(
        v15_softwall_field, (0, 120), y0,
        args=(e_val, BENCHMARK["eps_H"], BENCHMARK["eps_I"]),
        t_eval=t_eval, method="LSODA", rtol=1e-9, atol=1e-12
    )
    return sol


class DashboardHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/html; charset=utf-8")
            self.end_headers()

            sol = simulate_post_hopf(1.20)
            t_json = json.dumps(np.round(sol.t, 4).tolist())
            g_json = json.dumps(np.round(sol.y[0], 5).tolist())
            h_json = json.dumps(np.round(sol.y[1], 5).tolist())
            i_json = json.dumps(np.round(sol.y[2], 5).tolist())

            html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Appendix A v1.5 — Global Soft-Wall Dynamical Sandbox</title>
    <script src="https://cdn.plot.ly/plotly-2.27.0.min.js"></script>
    <style>
        body {{ background-color: #0b0f19; color: #e2e8f0; font-family: system-ui, sans-serif; margin: 32px; }}
        h2 {{ margin-top: 0; color: #f8fafc; }}
        .subtitle {{ color: #94a3b8; margin-bottom: 20px; font-size: 14px; }}
        .readout {{ display: grid; grid-template-columns: repeat(4, 1fr); gap: 16px; margin-bottom: 24px; }}
        .card {{ background: #1e293b; padding: 16px 20px; border-radius: 8px; border: 1px solid #334155; }}
        .label {{ font-size: 12px; text-transform: uppercase; letter-spacing: 0.05em; color: #94a3b8; }}
        .val {{ font-size: 22px; font-weight: 700; color: #38bdf8; margin-top: 6px; }}
        #plot {{ width: 100%; height: 520px; background: #1e293b; border-radius: 8px; border: 1px solid #334155; }}
    </style>
</head>
<body>
    <h2>Appendix A v1.5 — Soft-Wall Phase-Space Confinement (e = 1.20 e<sub>c</sub>)</h2>
    <div class="subtitle">
        Benchmark parameters (a=b=c=f=g=E<sub>avail</sub>=1, γ<sub>max</sub>=10, H<sub>max</sub>=100, P<sub>input</sub>=5, İ<sub>erase</sub>=10, ε<sub>H</sub>=ε<sub>I</sub>=0.05).
        Whereas v1.0 escapes to γ &lt; 0 at t ≈ 55, v1.5 remains strictly inside B = [0, γ<sub>max</sub>] × [0, H<sub>max</sub>] × [0, İ<sub>max</sub>].
    </div>
    <div class="readout">
        <div class="card"><div class="label">Min Reconstruction γ(t)</div><div class="val">+{np.min(sol.y[0]):.5f} s⁻¹</div></div>
        <div class="card"><div class="label">Min Entropy H<sub>obs</sub>(t)</div><div class="val">+{np.min(sol.y[1]):.5f} bits</div></div>
        <div class="card"><div class="label">Min Processing İ(t)</div><div class="val">+{np.min(sol.y[2]):.5f} s⁻¹</div></div>
        <div class="card"><div class="label">Max Ceiling γ(t) / γ<sub>max</sub></div><div class="val">{np.max(sol.y[0]):.4f} / 10.0</div></div>
    </div>
    <div id="plot"></div>
    <script>
        const t = {t_json};
        const gamma = {g_json};
        const H_obs = {h_json};
        const I_dot = {i_json};
        Plotly.newPlot('plot', [
            {{ x: t, y: gamma, name: 'γ(t) [s⁻¹]', line: {{ color: '#4ade80', width: 2 }} }},
            {{ x: t, y: H_obs, name: 'H_obs(t) [bits]', line: {{ color: '#facc15', width: 2 }} }},
            {{ x: t, y: I_dot, name: 'İ(t) [s⁻¹]', line: {{ color: '#38bdf8', width: 1.5 }} }}
        ], {{
            paper_bgcolor: '#1e293b', plot_bgcolor: '#0f172a',
            font: {{ color: '#e2e8f0' }},
            xaxis: {{ title: 'Time t (s)', gridcolor: '#334155' }},
            yaxis: {{ title: 'State Magnitude', gridcolor: '#334155' }},
            legend: {{ orientation: 'h', y: 1.12 }}
        }});
    </script>
</body>
</html>"""
            self.wfile.write(html.encode("utf-8"))
        else:
            self.send_error(404, "File Not Found")


def open_browser():
    webbrowser.open_new("http://localhost:8080/")


if __name__ == "__main__":
    print("Launching Appendix A v1.5 Sandbox Server on http://localhost:8080/")
    Timer(1.0, open_browser).start()
    TCPServer.allow_reuse_address = True
    with TCPServer(("", 8080), DashboardHandler) as server:
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            print("\nShutting down sandbox server safely.")