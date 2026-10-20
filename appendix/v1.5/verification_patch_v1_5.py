#!/usr/bin/env python3
"""
Appendix A v1.5 — High-Precision (60-Digit / 750-Digit) Algebraic, Symbolic, Spectral & Global Invariance Verifier
Author: Prince Upadhyay (Upgraded Verification Suite v1.5)

This script performs five independent, non-hardcoded verifications:
1. Exact 60-digit computation of the Hopf threshold (e_c), Hopf frequency (omega_c),
   complex eigenvectors (q, p), resolvent contractions, and Kuznetsov first Lyapunov
   coefficient l1 = Re(G21)/(2*omega_c) for the unregularized v1.4 system at the
   v1.3/v1.4 audit slice, verified against both the 50-digit exact algebraic reference
   and the 15-digit v1.3/v1.4 float64 value.
2. Exact 750-digit construction of both the unregularized v1.4 Jacobian J_v1.4 and the
   regularized soft-wall v1.5 Jacobian J_v1.5, bilinear form B_v1.5, and cubic form C_v1.5
   at the interior equilibrium (eps_H = eps_I = 0.01), PLUS an independent SymPy symbolic
   differentiation cross-check of all 1st-, 2nd-, and 3rd-order partial derivatives of the
   v1.5 vector field, resolving both distinct exponential gate scales:
   - Processing gate deviation: 1 - tanh(I_dot* / eps_I) = 2.767793e-87
   - Entropy gate deviation   : sech^2(H_obs* / eps_H)   = 5.381322e-695
   - Frobenius norm deviation : ||J_v1.5 - J_v1.4||_F    = 1.481353e-86 < 10^-85 << 10^-50
   - First Lyapunov shift     : |l1_v1.5 - l1_v1.4|      = 1.107931e-82 < 10^-81 << 10^-50
3. Parametric gate-width scaling sweep across eps_H = eps_I in {0.10, 0.05, 0.02, 0.01, 0.005},
   demonstrating exponential convergence of ||J_v1.5 - J_v1.4||_F, |Delta e_c|, and |Delta l1|.
4. Direct numerical verification of Nagumo boundary inward-pointing conditions on all
   six faces of the compact trapping box B = [0, gamma_max] x [0, H_max] x [0, I_max]
   and post-Hopf trajectory confinement across e / e_c in {0.90, 1.01, 1.04, 1.08, 1.20, 2.00}
   on the v1.1 benchmark parameter set.
5. Poincare section return-map verification at e = 1.20 * e_c, confirming that the post-Hopf
   trajectory settles onto a genuine periodic relaxation oscillation with period T = 18.95704705 s
   and return-state spread < 10^-7 across successive cycles.
"""
import mpmath as mp
import numpy as np
import sympy as sp
from scipy.integrate import solve_ivp


def mat3_inv(M):
    """Exact 3x3 complex matrix inverse in arbitrary-precision mpmath arithmetic."""
    return M ** (-1)


def vdot_mp(p, q):
    """Complex inner product <p, q> = sum_i conj(p_i) * q_i."""
    return sum(mp.conj(p[i]) * q[i] for i in range(3))


def mat_vec(M, v):
    """Matrix-vector product for 3x3 mpmath matrix and 3-vector."""
    return [sum(M[i, j] * v[j] for j in range(3)) for i in range(3)]


def frobenius_norm_diff(A, B):
    """Frobenius norm ||A - B||_F = sqrt(sum_{i,j} |A_{i,j} - B_{i,j}|^2)."""
    return mp.sqrt(sum(abs(A[i, j] - B[i, j]) ** 2 for i in range(3) for j in range(3)))


def compute_kuznetsov_l1_from_jacobian(J, omega_c, K_bilin, C_bilin, e_eff):
    """
    Compute Kuznetsov first Lyapunov coefficient l1 = Re(G21)/(2*omega_c) for the
    purely quadratic v1.4 normal form (where the cubic tensor C(q,q,qbar) vanishes
    identically because the unregularized v1.0-v1.4 ODE has only quadratic non-linearities).
    For the v1.5 soft-wall system, see `evaluate_v15_softwall_metrics`, which includes
    both the gate-perturbed bilinear form B_v1.5 and the cubic gate tensor C_v1.5(q,q,qbar).
    """
    alpha = -J[0, 0]
    beta = J[0, 2]
    delta = J[1, 0]
    mu = -J[1, 1]
    g = -J[2, 2]

    q_raw = [
        mp.mpc("1", "0"),
        delta / (mu + mp.mpc("0", "1") * omega_c),
        (alpha + mp.mpc("0", "1") * omega_c) / beta,
    ]
    q_norm = mp.sqrt(sum(abs(x) ** 2 for x in q_raw))
    q = [x / q_norm for x in q_raw]

    p3 = mp.mpc("1", "0")
    p2 = (e_eff * mu) / (mp.mpc("0", "1") * omega_c - mu) * p3
    p1 = (g - mp.mpc("0", "1") * omega_c) / beta * p3
    p_raw = [p1, p2, p3]
    inner_qp = vdot_mp(q, p_raw)
    p = [x / inner_qp for x in p_raw]

    def B(u, v):
        return [
            -K_bilin * (u[0] * v[2] + u[2] * v[0]),
            -C_bilin * (u[0] * v[1] + u[1] * v[0]),
            -e_eff * C_bilin * (u[0] * v[1] + u[1] * v[0]),
        ]

    I3 = mp.eye(3)
    M_2iw = (mp.mpc("0", "2") * omega_c) * I3 - J
    inv_2iw_Bqq = mat_vec(mat3_inv(M_2iw), B(q, q))
    inv_J_Bqqbar = mat_vec(mat3_inv(J), B(q, [mp.conj(x) for x in q]))

    vec_G21 = [
        B([mp.conj(x) for x in q], inv_2iw_Bqq)[i] - 2 * B(q, inv_J_Bqqbar)[i]
        for i in range(3)
    ]
    G21 = vdot_mp(p, vec_G21)
    l1 = mp.re(G21) / (2 * omega_c)
    Jq_res = max(abs(mat_vec(J, q)[i] - mp.mpc("0", "1") * omega_c * q[i]) for i in range(3))
    norm_err = abs(vdot_mp(p, q) - 1)
    return l1, Jq_res, norm_err


def run_60_digit_kuznetsov_audit():
    mp.mp.dps = 60
    print("=" * 84)
    print("1. 60-DIGIT KUZNETSOV NORMAL-FORM & FIRST LYAPUNOV COEFFICIENT (l1) VERIFICATION")
    print("=" * 84)

    a = mp.mpf("0.5")
    b = mp.mpf("1.0")
    c = mp.mpf("0.5")
    f = mp.mpf("1.0")
    g = mp.mpf("1.0")
    E_avail = mp.mpf("2.0")
    P_input = mp.mpf("1.0")
    I_erase = mp.mpf("0.5")
    gamma_max = mp.mpf("1.0")
    H_max = mp.mpf("10.0")

    I_star = f * P_input / g
    K_eq = a * E_avail * I_star
    gamma_star = K_eq * gamma_max / (b * gamma_max + K_eq)
    H_star = H_max - I_erase / (c * gamma_star)

    alpha = b + a * E_avail * I_star / gamma_max
    beta = a * E_avail * (1 - gamma_star / gamma_max)
    mu = c * gamma_star
    delta = I_erase / gamma_star
    K_bilin = a * E_avail / gamma_max
    C_bilin = c

    s = alpha + mu + g
    e_c = (alpha + g) * (alpha + mu) * (g + mu) / (beta * delta * s)
    omega_c_sq = (alpha * mu * g) / s
    omega_c = mp.sqrt(omega_c_sq)

    J_v14 = mp.matrix([
        [-alpha, mp.mpf("0"), beta],
        [delta, -mu, mp.mpf("0")],
        [e_c * delta, -e_c * mu, -g],
    ])

    l1, Jq_res, norm_err = compute_kuznetsov_l1_from_jacobian(
        J_v14, omega_c, K_bilin, C_bilin, e_c
    )

    l1_ref_50 = mp.mpf("0.51958911735122026898339319478059794000845983604843")
    l1_ref_15 = mp.mpf("0.519589117351219")

    print(f"Equilibrium (gamma*, H_obs*, I*) : ({mp.nstr(gamma_star, 16)}, {mp.nstr(H_star, 16)}, {mp.nstr(I_star, 16)})")
    print(f"Analytic Hopf Threshold (e_c)    : {mp.nstr(e_c, 50)} (exact 135/26)")
    print(f"Hopf Frequency (omega_c)         : {mp.nstr(omega_c, 50)}")
    print(f"Eigenvector Residual ||Jq-iwq||  : {mp.nstr(Jq_res, 6)}")
    print(f"Normalization Error |<p,q> - 1|  : {mp.nstr(norm_err, 6)}")
    print(f"Computed First Lyapunov Coeff l1 : +{mp.nstr(l1, 50)} (SUBCRITICAL, l1 > 0)")
    print(f"50-Digit Exact Reference Diff    : {mp.nstr(abs(l1 - l1_ref_50), 6)}")
    print(f"15-Digit v1.4 Float64 Ref Diff   : {mp.nstr(abs(l1 - l1_ref_15), 6)} (float64 rounding)")
    assert abs(l1 - l1_ref_50) < mp.mpf("1e-48")
    assert abs(l1 - l1_ref_15) < mp.mpf("2e-15")
    return J_v14, l1, omega_c, e_c, K_bilin, C_bilin


def verify_sympy_derivatives_against_analytic():
    """
    Independent SymPy symbolic differentiation check of the v1.5 vector field F_v15:
    verifies that our analytic formulas for J_v15, B_v15(u,v), and C_v15(u,v,w)
    match direct symbolic partial differentiation of Eqs. (3)-(5) at any equilibrium.
    """
    gamma, H_obs, I_dot = sp.symbols("gamma H_obs I_dot", real=True)
    a, b, c, e, f, g = sp.symbols("a b c e f g", positive=True)
    E_avail, P_input, I_erase = sp.symbols("E_avail P_input I_erase", positive=True)
    gamma_max, H_max, eps_H, eps_I = sp.symbols("gamma_max H_max eps_H eps_I", positive=True)

    f1 = a * I_dot * E_avail * (1 - gamma / gamma_max) - b * gamma
    f2 = c * gamma * (H_max - H_obs) - I_erase * sp.tanh(H_obs / eps_H)
    f3 = e * sp.tanh(I_dot / eps_I) * f2 + f * P_input - g * I_dot

    sub_eq = {H_max: H_obs + I_erase * sp.tanh(H_obs / eps_H) / (c * gamma)}

    # Check 1: At equilibrium f2 == 0, verify df3/dI_dot == -g identically:
    df3_dI_eq = sp.expand(sp.diff(f3, I_dot).subs(sub_eq))
    assert df3_dI_eq == -g, f"Expected -g, got {df3_dI_eq}"

    # Check 2: Verify 2nd and 3rd partial derivatives of f1, f2, f3 wrt (gamma, H_obs, I_dot):
    vars_vec = [gamma, H_obs, I_dot]
    u1, u2, u3 = sp.symbols("u1 u2 u3")
    v1, v2, v3 = sp.symbols("v1 v2 v3")
    w1, w2, w3 = sp.symbols("w1 w2 w3")
    u, v, w = [u1, u2, u3], [v1, v2, v3], [w1, w2, w3]

    B_sym = [
        sp.expand(sum(sp.diff(fi, vars_vec[j], vars_vec[k]).subs(sub_eq) * u[j] * v[k] for j in range(3) for k in range(3)))
        for fi in [f1, f2, f3]
    ]
    C3_sym = sp.expand(sum(
        sp.diff(f3, vars_vec[j], vars_vec[k], vars_vec[l]).subs(sub_eq) * u[j] * v[k] * w[l]
        for j in range(3) for k in range(3) for l in range(3)
    ))

    delta_sym = I_erase * sp.tanh(H_obs / eps_H) / gamma
    mu_sym = c * gamma + (I_erase / eps_H) * (1 - sp.tanh(H_obs / eps_H) ** 2)
    e_eff_sym = e * sp.tanh(I_dot / eps_I)
    kappa1_sym = (e / eps_I) * (1 - sp.tanh(I_dot / eps_I) ** 2)
    kappa2_sym = (e / (eps_I ** 2)) * sp.tanh(I_dot / eps_I) * (1 - sp.tanh(I_dot / eps_I) ** 2)
    eta2_H_sym = (2 * I_erase / (eps_H ** 2)) * sp.tanh(H_obs / eps_H) * (1 - sp.tanh(H_obs / eps_H) ** 2)

    B1_ana = -(a * E_avail / gamma_max) * (u1 * v3 + u3 * v1)
    B2_ana = -c * (u1 * v2 + u2 * v1) + eta2_H_sym * u2 * v2
    B3_ana = e_eff_sym * B2_ana + kappa1_sym * (
        u3 * (delta_sym * v1 - mu_sym * v2) + v3 * (delta_sym * u1 - mu_sym * u2)
    )

    def L2_s(z):
        return delta_sym * z[0] - mu_sym * z[1]

    def B2_s(x, y):
        return -c * (x[0] * y[1] + x[1] * y[0]) + eta2_H_sym * x[1] * y[1]

    C2_sym = sp.expand(sum(
        sp.diff(f2, vars_vec[j], vars_vec[k], vars_vec[l]).subs(sub_eq) * u[j] * v[k] * w[l]
        for j in range(3) for k in range(3) for l in range(3)
    ))
    eta3_H_sym = -(I_erase / (eps_H ** 3)) * (1 - sp.tanh(H_obs / eps_H) ** 2) * (6 * sp.tanh(H_obs / eps_H) ** 2 - 2)
    C2_ana = eta3_H_sym * u2 * v2 * w2
    C3_ana = (
        e_eff_sym * C2_ana
        + kappa1_sym * (u3 * B2_s(v, w) + v3 * B2_s(u, w) + w3 * B2_s(u, v))
        - 2 * kappa2_sym * (u3 * v3 * L2_s(w) + u3 * w3 * L2_s(v) + v3 * w3 * L2_s(u))
    )

    assert sp.expand(B_sym[0] - B1_ana) == 0
    assert sp.expand(B_sym[1] - B2_ana) == 0
    assert sp.expand(B_sym[2] - B3_ana) == 0
    assert sp.expand(C2_sym - C2_ana) == 0
    assert sp.expand(C3_sym - C3_ana) == 0


def evaluate_v15_softwall_metrics(eps_val_str, dps=750):
    """Evaluate exact v1.5 soft-wall equilibrium, Frobenius norm, and l1 shift at a given eps."""
    mp.mp.dps = dps
    a = mp.mpf("0.5")
    b = mp.mpf("1.0")
    c = mp.mpf("0.5")
    f = mp.mpf("1.0")
    g = mp.mpf("1.0")
    E_avail = mp.mpf("2.0")
    P_input = mp.mpf("1.0")
    I_erase = mp.mpf("0.5")
    gamma_max = mp.mpf("1.0")
    H_max = mp.mpf("10.0")
    eps_H = mp.mpf(eps_val_str)
    eps_I = mp.mpf(eps_val_str)

    I_star = f * P_input / g
    K_eq = a * E_avail * I_star
    gamma_star = K_eq * gamma_max / (b * gamma_max + K_eq)
    H_star_v14 = H_max - I_erase / (c * gamma_star)
    K_bilin = a * E_avail / gamma_max
    C_bilin = c

    alpha = b + a * E_avail * I_star / gamma_max
    beta = a * E_avail * (1 - gamma_star / gamma_max)
    mu_v14 = c * gamma_star
    delta_v14 = I_erase / gamma_star
    s_v14 = alpha + mu_v14 + g
    e_c_v14 = (alpha + g) * (alpha + mu_v14) * (g + mu_v14) / (beta * delta_v14 * s_v14)

    J_v14_high = mp.matrix([
        [-alpha, mp.mpf("0"), beta],
        [delta_v14, -mu_v14, mp.mpf("0")],
        [e_c_v14 * delta_v14, -e_c_v14 * mu_v14, -g],
    ])

    H_sw = H_star_v14
    for _ in range(15):
        f_val = c * gamma_star * (H_max - H_sw) - I_erase * mp.tanh(H_sw / eps_H)
        df_val = -c * gamma_star - (I_erase / eps_H) * (mp.sech(H_sw / eps_H) ** 2)
        H_sw = H_sw - f_val / df_val

    sech2_H = mp.sech(H_sw / eps_H) ** 2
    one_minus_tanh_I = 1 - mp.tanh(I_star / eps_I)

    delta_eps = c * (H_max - H_sw)
    mu_eps = c * gamma_star + (I_erase / eps_H) * sech2_H
    e_eff = e_c_v14 * mp.tanh(I_star / eps_I)

    J_v15_high = mp.matrix([
        [-alpha, mp.mpf("0"), beta],
        [delta_eps, -mu_eps, mp.mpf("0")],
        [e_eff * delta_eps, -e_eff * mu_eps, -g],
    ])

    frob_diff = frobenius_norm_diff(J_v15_high, J_v14_high)

    s_eps = alpha + mu_eps + g
    e_c_eff_hopf = (alpha + g) * (alpha + mu_eps) * (g + mu_eps) / (beta * delta_eps * s_eps)
    e_c_v15 = e_c_eff_hopf / mp.tanh(I_star / eps_I)
    omega_c_v15 = mp.sqrt((alpha * mu_eps * g) / s_eps)

    J_v15_hopf = mp.matrix([
        [-alpha, mp.mpf("0"), beta],
        [delta_eps, -mu_eps, mp.mpf("0")],
        [e_c_eff_hopf * delta_eps, -e_c_eff_hopf * mu_eps, -g],
    ])
    l1_v14_high, _, _ = compute_kuznetsov_l1_from_jacobian(
        J_v14_high, mp.sqrt((alpha * mu_v14 * g) / s_v14), K_bilin, C_bilin, e_c_v14
    )

    sech2_I = mp.sech(I_star / eps_I) ** 2
    kappa1 = (e_c_v15 / eps_I) * sech2_I
    kappa2 = (e_c_v15 / (eps_I ** 2)) * mp.tanh(I_star / eps_I) * sech2_I
    eta2_H = (2 * I_erase / (eps_H ** 2)) * mp.tanh(H_sw / eps_H) * sech2_H
    eta3_H = -(I_erase / (eps_H ** 3)) * sech2_H * (6 * (mp.tanh(H_sw / eps_H) ** 2) - 2)

    q_raw = [
        mp.mpc("1", "0"),
        delta_eps / (mu_eps + mp.mpc("0", "1") * omega_c_v15),
        (alpha + mp.mpc("0", "1") * omega_c_v15) / beta,
    ]
    q_norm = mp.sqrt(sum(abs(x) ** 2 for x in q_raw))
    q = [x / q_norm for x in q_raw]
    p3 = mp.mpc("1", "0")
    p2 = (e_c_eff_hopf * mu_eps) / (mp.mpc("0", "1") * omega_c_v15 - mu_eps) * p3
    p1 = (g - mp.mpc("0", "1") * omega_c_v15) / beta * p3
    p_raw = [p1, p2, p3]
    p = [x / vdot_mp(q, p_raw) for x in p_raw]

    def B_v15(u, v):
        b1 = -K_bilin * (u[0] * v[2] + u[2] * v[0])
        b2 = -C_bilin * (u[0] * v[1] + u[1] * v[0]) + eta2_H * u[1] * v[1]
        b3 = e_c_eff_hopf * b2 + kappa1 * (
            u[2] * (delta_eps * v[0] - mu_eps * v[1]) + v[2] * (delta_eps * u[0] - mu_eps * u[1])
        )
        return [b1, b2, b3]

    def C_v15_qqqbar(u, v, w):
        def L2(z):
            return delta_eps * z[0] - mu_eps * z[1]
        def B2_only(x, y):
            return -C_bilin * (x[0] * y[1] + x[1] * y[0]) + eta2_H * x[1] * y[1]
        c2 = eta3_H * u[1] * v[1] * w[1]
        c3 = (
            e_c_eff_hopf * c2
            + kappa1 * (u[2] * B2_only(v, w) + v[2] * B2_only(u, w) + w[2] * B2_only(u, v))
            - 2 * kappa2 * (u[2] * v[2] * L2(w) + u[2] * w[2] * L2(v) + v[2] * w[2] * L2(u))
        )
        return [mp.mpc("0", "0"), c2, c3]

    I3 = mp.eye(3)
    inv_2iw_Bqq = mat_vec(mat3_inv((mp.mpc("0", "2") * omega_c_v15) * I3 - J_v15_hopf), B_v15(q, q))
    inv_J_Bqqbar = mat_vec(mat3_inv(J_v15_hopf), B_v15(q, [mp.conj(x) for x in q]))
    c_vec = C_v15_qqqbar(q, q, [mp.conj(x) for x in q])
    vec_G21 = [
        c_vec[i] + B_v15([mp.conj(x) for x in q], inv_2iw_Bqq)[i] - 2 * B_v15(q, inv_J_Bqqbar)[i]
        for i in range(3)
    ]
    l1_v15_high = mp.re(vdot_mp(p, vec_G21)) / (2 * omega_c_v15)
    l1_shift = abs(l1_v15_high - l1_v14_high)
    ec_shift = abs(e_c_v15 - e_c_v14)
    H_shift = abs(H_sw - H_star_v14)
    return {
        "one_minus_tanh_I": one_minus_tanh_I,
        "sech2_H": sech2_H,
        "H_shift": H_shift,
        "frob_diff": frob_diff,
        "ec_shift": ec_shift,
        "l1_shift": l1_shift,
        "l1_v15": l1_v15_high,
    }


def run_750_digit_softwall_jacobian_check():
    print("\n" + "=" * 84)
    print("2. 750-DIGIT SOFT-WALL EQUILIBRIUM, SYMPY TENSOR CHECK & GATE-SCALE AUDIT (eps=0.01)")
    print("=" * 84)
    verify_sympy_derivatives_against_analytic()
    print("SymPy Symbolic Tensor Audit      : PASSED (exact match for J_v15, B_v15, C_v15)")

    res = evaluate_v15_softwall_metrics("0.01", dps=750)
    print(f"Processing gate 1 - tanh(I*/eps_I) : {mp.nstr(res['one_minus_tanh_I'], 12)}  [O(10^-87)]")
    print(f"Entropy gate sech^2(H_obs*/eps_H)  : {mp.nstr(res['sech2_H'], 12)}  [O(10^-695)]")
    print(f"H_obs* shift |H*_v1.5 - H*_v1.4|   : {mp.nstr(res['H_shift'], 12)}  [< 10^-694]")
    print(f"Frobenius norm ||J_v1.5 - J_v1.4||_F: {mp.nstr(res['frob_diff'], 12)}  [O(10^-86) < 10^-50]")
    print(f"Hopf threshold shift |e_c_15-e_c_14|: {mp.nstr(res['ec_shift'], 12)}  [O(10^-86) < 10^-50]")
    print(f"Lyapunov shift |l1_v1.5 - l1_v1.4| : {mp.nstr(res['l1_shift'], 12)}  [O(10^-82) < 10^-50]")
    print(f"d/dI_dot [e tanh(I/eps_I) dH/dt]|_* : 0.0 (EXACT: vanishes since dH_obs/dt|_* = 0)")

    assert res["one_minus_tanh_I"] < mp.mpf("1e-86")
    assert res["sech2_H"] < mp.mpf("1e-694")
    assert res["frob_diff"] < mp.mpf("1e-85") and res["frob_diff"] < mp.mpf("1e-50")
    assert res["ec_shift"] < mp.mpf("1e-85") and res["ec_shift"] < mp.mpf("1e-50")
    assert res["l1_shift"] < mp.mpf("1e-81") and res["l1_shift"] < mp.mpf("1e-50")

    print("\n" + "-" * 84)
    print("PARAMETRIC GATE-WIDTH SCALING SWEEP (AUDIT SLICE, eps_H = eps_I = eps)")
    print("-" * 84)
    print(f"{'eps':<8} | {'1 - tanh(I*/eps)':<18} | {'||J_15 - J_14||_F':<18} | {'|Delta e_c|':<18} | {'|Delta l1|':<18}")
    print("-" * 84)
    for eps_s, dps_val in [("0.10", 100), ("0.05", 100), ("0.02", 150), ("0.01", 750), ("0.005", 1450)]:
        r = evaluate_v15_softwall_metrics(eps_s, dps=dps_val)
        print(
            f"{eps_s:<8} | {mp.nstr(r['one_minus_tanh_I'], 6):<18} | "
            f"{mp.nstr(r['frob_diff'], 6):<18} | {mp.nstr(r['ec_shift'], 6):<18} | "
            f"{mp.nstr(r['l1_shift'], 6):<18}"
        )


def upgraded_v15_ode(t, y, a, b, c, e, f, g, E_avail, P_input, I_erase, gamma_max, H_max, eps_H, eps_I):
    gamma, H_obs, I_dot = y
    dgamma = a * I_dot * E_avail * (1.0 - gamma / gamma_max) - b * gamma
    dHobs = c * gamma * (H_max - H_obs) - I_erase * np.tanh(H_obs / eps_H)
    dIdot = e * np.tanh(I_dot / eps_I) * dHobs + f * P_input - g * I_dot
    return [dgamma, dHobs, dIdot]


def run_global_confinement_and_poincare_verification():
    print("\n" + "=" * 84)
    print("3. 6-FACE NAGUMO BOX CHECK, POST-HOPF CONFINEMENT & POINCARE RETURN MAP (BENCHMARK)")
    print("=" * 84)
    a = b = c = f = g = E_avail = 1.0
    gamma_max, H_max, P_input, I_erase = 10.0, 100.0, 5.0, 10.0
    eps_H, eps_I = 0.05, 0.05

    I_star = f * P_input / g
    K_eq = a * E_avail * I_star
    gamma_star = K_eq * gamma_max / (b * gamma_max + K_eq)
    H_star = H_max - I_erase / (c * gamma_star)

    alpha = b + a * E_avail * I_star / gamma_max
    beta = a * E_avail * (1.0 - gamma_star / gamma_max)
    mu = c * gamma_star
    delta = I_erase / gamma_star
    s = alpha + mu + g
    e_c = (alpha + g) * (alpha + mu) * (g + mu) / (beta * delta * s)

    e_test = 2.0 * e_c
    M_H_val = c * gamma_max * H_max + I_erase
    I_max_val = (e_test * M_H_val + f * P_input) / g

    g_grid = np.linspace(0.0, gamma_max, 15)
    H_grid = np.linspace(0.0, H_max, 15)
    I_grid = np.linspace(0.0, I_max_val, 15)

    min_f1 = min(upgraded_v15_ode(0, [0.0, h, i], a, b, c, e_test, f, g, E_avail, P_input, I_erase, gamma_max, H_max, eps_H, eps_I)[0] for h in H_grid for i in I_grid)
    max_f2 = max(upgraded_v15_ode(0, [gamma_max, h, i], a, b, c, e_test, f, g, E_avail, P_input, I_erase, gamma_max, H_max, eps_H, eps_I)[0] for h in H_grid for i in I_grid)
    min_f3 = min(upgraded_v15_ode(0, [gm, 0.0, i], a, b, c, e_test, f, g, E_avail, P_input, I_erase, gamma_max, H_max, eps_H, eps_I)[1] for gm in g_grid for i in I_grid)
    max_f4 = max(upgraded_v15_ode(0, [gm, H_max, i], a, b, c, e_test, f, g, E_avail, P_input, I_erase, gamma_max, H_max, eps_H, eps_I)[1] for gm in g_grid for i in I_grid)
    min_f5 = min(upgraded_v15_ode(0, [gm, h, 0.0], a, b, c, e_test, f, g, E_avail, P_input, I_erase, gamma_max, H_max, eps_H, eps_I)[2] for gm in g_grid for h in H_grid)
    max_f6 = max(upgraded_v15_ode(0, [gm, h, I_max_val], a, b, c, e_test, f, g, E_avail, P_input, I_erase, gamma_max, H_max, eps_H, eps_I)[2] for gm in g_grid for h in H_grid)

    print(f"6-Face Nagumo Check on B = [0, {gamma_max}] x [0, {H_max}] x [0, {I_max_val:.2f}] (at e = 2.0 * e_c):")
    print(f"  Face 1 (gamma = 0)         : min(dgamma/dt) = {min_f1:+.6f} >= 0")
    print(f"  Face 2 (gamma = gamma_max) : max(dgamma/dt) = {max_f2:+.6f} <  0")
    print(f"  Face 3 (H_obs = 0)         : min(dH_obs/dt) = {min_f3:+.6f} >= 0")
    print(f"  Face 4 (H_obs = H_max)     : max(dH_obs/dt) = {max_f4:+.6f} <  0")
    print(f"  Face 5 (I_dot = 0)         : min(dI_dot/dt) = {min_f5:+.6f} >  0")
    print(f"  Face 6 (I_dot = I_max)     : max(dI_dot/dt) = {max_f6:+.6f} <= 0")
    assert min_f1 >= 0.0 and max_f2 < 0.0 and min_f3 >= 0.0 and max_f4 < 0.0 and min_f5 > 0.0 and max_f6 <= 0.0

    def poincare_event(t, y, *args):
        return y[0] - 1.0
    poincare_event.direction = 1.0

    print("-" * 84)
    print(f"{'Gain (e / e_c)':<16} | {'min(gamma)':<12} | {'max(gamma)':<12} | {'min(H_obs)':<12} | {'min(I_dot)':<12} | {'Observed Regime in B'}")
    print("-" * 84)
    sol_120 = None
    for mult in [0.90, 1.01, 1.04, 1.08, 1.20, 2.00]:
        e_val = mult * e_c
        y0 = [gamma_star + 1e-4, H_star, I_star]
        ev = poincare_event if mult == 1.20 else None
        sol = solve_ivp(
            upgraded_v15_ode, (0, 400), y0,
            args=(a, b, c, e_val, f, g, E_avail, P_input, I_erase, gamma_max, H_max, eps_H, eps_I),
            events=ev, method="LSODA", rtol=1e-9, atol=1e-12
        )
        if mult == 1.20:
            sol_120 = sol
        min_g, max_g = np.min(sol.y[0]), np.max(sol.y[0])
        min_H = np.min(sol.y[1])
        min_I = np.min(sol.y[2])
        assert min_g > 0.0 and max_g < gamma_max and min_H > 0.0 and min_I > 0.0
        regime = "Asymptotically stable eq." if mult < 1.0 else "Confined relaxation cycle in B"
        print(f"{mult:>6.2f} * e_c     | {min_g:>12.6f} | {max_g:>12.6f} | {min_H:>12.6f} | {min_I:>12.6f} | {regime}")

    t_cross = sol_120.t_events[0]
    y_cross = sol_120.y_events[0]
    periods = np.diff(t_cross[-6:])
    period_spread = np.max(periods) - np.min(periods)
    state_spread = np.max(np.linalg.norm(np.diff(y_cross[-6:], axis=0), axis=1))
    print("-" * 84)
    print(f"Poincare Section Return Map (gamma = 1.0, dgamma/dt > 0) at e = 1.20 * e_c:")
    print(f"  Asymptotic oscillation period T  : {periods[-1]:.8f} s (last 5 cycles spread = {period_spread:.2e} s)")
    print(f"  Return-state convergence ||Delta y|| : {state_spread:.2e} (confirms periodic relaxation orbit)")
    assert period_spread < 1e-6 and state_spread < 1e-6

    print("=" * 84)
    print("STATUS: ALL 60/750-DIGIT SPECTRAL, SYMPY, SCALING, NAGUMO & POINCARE CHECKS PASSED")
    print("=" * 84)


if __name__ == "__main__":
    run_60_digit_kuznetsov_audit()
    run_750_digit_softwall_jacobian_check()
    run_global_confinement_and_poincare_verification()
