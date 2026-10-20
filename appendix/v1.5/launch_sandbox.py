#!/usr/bin/env python3
import sys
import webbrowser
from threading import Timer
from http.server import SimpleHTTPRequestHandler
from socketserver import TCPServer
import numpy as np
from scipy.integrate import solve_ivp
import plotly.graph_objects as go

# Fix encoding defaults for terminal output streams
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

COEFFS = {"a": 1.0, "b": 1.0, "c": 1.0, "e": 1.5, "f": 1.0, "gamma_max": 10.0, "H_max": 100.0, "E_avail": 1.0}

def vector_field(t, state, g, erasure, P, eps):
    gamma, H_obs, I_dot = state
    theta = np.tanh(gamma / eps) if gamma > 0 else 0.0
    psi = 0.5 * (1.0 + np.tanh(H_obs / eps)) if H_obs > 0 else 0.0
    phi = np.tanh(I_dot / eps) if I_dot > 0 else 0.0
    
    dgamma = COEFFS["a"] * I_dot * COEFFS["E_avail"] * (1.0 - gamma / COEFFS["gamma_max"]) - COEFFS["b"] * gamma * theta
    dHobs = COEFFS["c"] * gamma * (COEFFS["H_max"] - H_obs) - erasure * psi
    dIdot = COEFFS["e"] * dHobs + COEFFS["f"] * P - g * I_dot * phi
    return [dgamma, dHobs, dIdot]

class DashboardHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html; charset=utf-8')
            self.end_headers()
            
            init = [4.86, 2.55, 8.39]
            t_eval = np.linspace(0, 50, 1000)
            sol = solve_ivp(vector_field, (0, 50), init, args=(3.0, 2.0, 5.0, 0.80), t_eval=t_eval, method="LSODA")
            
            fig = go.Figure()
            fig.add_trace(go.Scatter(x=list(sol.t), y=list(sol.y[0]), name="X (γ)", line=dict(color="#4ade80")))
            fig.add_trace(go.Scatter(x=list(sol.t), y=list(sol.y[1]), name="Y (H_obs)", line=dict(color="#facc15")))
            fig.add_trace(go.Scatter(x=list(sol.t), y=list(sol.y[2]), name="Z (I_dot)", line=dict(color="#38bdf8")))
            fig.add_hline(y=0.80, line_dash="dash", line_color="red", annotation_text="Soft-Wall Limit")
            fig.update_layout(title="Dynamical Sector Sandbox Trajectory", plot_bgcolor="black", paper_bgcolor="black", font=dict(color="white"))
            
            plot_html = fig.to_html(full_html=False, include_plotlyjs='cdn')
            
            html = f"""
            <html>
            <head>
                <title>Physics Sandbox v1.5</title>
                <style>
                    body {{ background-color: #111; color: white; font-family: sans-serif; margin: 40px; }}
                    .readout {{ display: flex; gap: 20px; margin-bottom: 20px; }}
                    .card {{ background: #222; padding: 20px; border-radius: 8px; flex: 1; border: 1px solid #333; }}
                    .val {{ font-size: 24px; font-weight: bold; color: #38bdf8; }}
                </style>
            </head>
            <body>
                <h2>Bounded Soft-Wall Dynamical System</h2>
                <div class="readout">
                    <div class="card"><div>Terminal X (γ)</div><div class="val">{sol.y[0][-1]:.4f}</div></div>
                    <div class="card"><div>Terminal Y (H<sub>obs</sub>)</div><div class="val">{sol.y[1][-1]:.4f}</div></div>
                    <div class="card"><div>Terminal Z (&Icirc;&middot;)</div><div class="val">{sol.y[2][-1]:.4f}</div></div>
                </div>
                {plot_html}
            </body>
            </html>
            """
            self.wfile.write(html.encode('utf-8'))
        else:
            self.send_error(404, "File Not Found")

def open_browser():
    # Upgrade: Uses native standard localhost routing strings to bypass ARM64 port blockage
    webbrowser.open_new("http://localhost:8080/")

if __name__ == '__main__':
    print("Launching Local Sandbox Web Engine on http://localhost:8080/")
    Timer(1.0, open_browser).start()
    TCPServer.allow_reuse_address = True
    # Binding globally to '' handles local operating system loopback rules natively
    with TCPServer(("", 8080), DashboardHandler) as server:
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            print("\nShutting down engine server safely.")
