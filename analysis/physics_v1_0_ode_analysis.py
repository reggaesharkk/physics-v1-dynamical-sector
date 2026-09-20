"""
Fixed-point and linear-stability analysis of the Physics v1.0 dynamical sector.

System (paper_physics_v1.0_release.tex, eqs. 9-11):

    dgamma/dt = a * Idot_model * E_avail * (1 - gamma/gamma_max) - b*gamma
    dH_obs/dt = c * gamma * (H_max - H_obs) - Idot_erase
    dIdot_model/dt = e * dH_obs/dt + f * P_input - g * Idot_model

Units (paper eq. 13):  [a]=[f]=J^-1 s^-1, [b]=[e]=[g]=s^-1, [c]=1,
[gamma]=[gamma_max]=[Idot]=s^-1, [E_avail]=J, [P_input]=J s^-1, [H]=bits.

Nothing here modifies Physics v1.0. This is analysis of the frozen ansatz.
"""
import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import brentq

# ---------------------------------------------------------------- model

def rhs(t, y, p):
    gam, H, I = y
    a, b, c, e, f, g, gmax, Hmax, E, P, Ier = p
    Hdot = c * gam * (Hmax - H) - Ier
    return [a * I * E * (1 - gam / gmax) - b * gam,
            Hdot,
            e * Hdot + f * P - g * I]


def fixed_point(p):
    """Closed-form equilibrium.  Note Hdot=0 there, so the e-coupling drops out
    of the third equation entirely and Idot* is set by input power alone."""
    a, b, c, e, f, g, gmax, Hmax, E, P, Ier = p
    Istar = f * P / g
    K = a * E * Istar
    gstar = K * gmax / (b * gmax + K)
    Dstar = Ier / (c * gstar)            # equilibrium gap H_max - H_obs
    return np.array([gstar, Hmax - Dstar, Istar]), K, Dstar


def jacobian(p):
    a, b, c, e, f, g, gmax, Hmax, E, P, Ier = p
    (gs, Hs, Is), K, Ds = fixed_point(p)
    alpha = a * E * Is / gmax + b        # identity: alpha*beta  = a*E*b
    beta = a * E * (1 - gs / gmax)
    mu = c * gs                          # identity: mu*delta    = c*Idot_erase
    delta = c * Ds
    J = np.array([[-alpha,   0.0,   beta],
                  [-delta,   -mu,    0.0],
                  [e * delta, e * mu,  -g]])
    return J, (alpha, beta, mu, delta)


def e_crit(p):
    """Hopf threshold from Routh-Hurwitz: a2*a1 = a0 for the cubic
    lambda^3 + (alpha+mu+g) lambda^2 + (alpha*mu+alpha*g+mu*g - e*beta*delta) lambda
            + alpha*mu*g = 0."""
    a, b, c, e, f, g, gmax, Hmax, E, P, Ier = p
    _, (alpha, beta, mu, delta) = jacobian(p)
    a2 = alpha + mu + g
    return (a2 * (alpha * mu + alpha * g + mu * g) - alpha * mu * g) / (beta * delta * a2)


def setp(e, Ier=1.0):
    #        a    b    c   e    f    g   gmax   Hmax   E    P    Idot_erase
    return [1.0, 1.0, 1.0, e, 1.0, 1.0, 10.0, 100.0, 1.0, 5.0, Ier]


# ---------------------------------------------------------------- checks

if __name__ == "__main__":
    print("--- structural identities ---")
    p = setp(1.0)
    _, (al, be, mu, de) = jacobian(p)
    print(f"  alpha*beta = {al*be:.6f}  =  a*E*b        = {p[0]*p[8]*p[1]:.6f}")
    print(f"  mu*delta   = {mu*de:.6f}  =  c*Idot_erase = {p[2]*p[10]:.6f}")

    for Ier in (1.0, 10.0):
        p = setp(1.0, Ier)
        (gs, Hs, Is), K, Ds = fixed_point(p)
        ec = e_crit(p)
        num = brentq(lambda e: np.max(np.real(np.linalg.eigvals(
            jacobian(setp(e, Ier))[0]))), 0.01, 10 * ec)
        print(f"\n--- Idot_erase = {Ier} s^-1 ---")
        print(f"  gamma* = {gs:.4f} s^-1   H* = {Hs:.4f} bits   Idot* = {Is:.4f} s^-1")
        print(f"  residual |f(x*)|  = {np.max(np.abs(rhs(0, [gs, Hs, Is], p))):.2e}")
        print(f"  e_crit analytic   = {ec:.6f}")
        print(f"  e_crit numeric    = {num:.6f}")
        print(f"  admissibility: H* >= 0 requires Idot_erase <= c*gamma**H_max "
              f"= {p[2]*gs*p[7]:.2f} s^-1")

    print("\n--- behaviour across the threshold (Idot_erase = 10) ---")
    Ier = 10.0
    ec = e_crit(setp(1.0, Ier))

    def gamma_zero(t, y, p):
        return y[0]
    gamma_zero.terminal = True
    gamma_zero.direction = -1

    for mult in (0.90, 1.01, 1.02, 1.04, 1.08, 1.20):
        e = mult * ec
        p = setp(e, Ier)
        x0, _, _ = fixed_point(p)
        s = solve_ivp(rhs, [0, 300], x0 * (1 + 1e-4 * np.array([1, 0, 0])),
                      args=(p,), rtol=1e-9, atol=1e-12, method="LSODA",
                      events=gamma_zero)
        if len(s.t_events[0]):
            print(f"  e = {mult:.2f} e_c : ESCAPES (gamma -> 0 at t = {s.t[-1]:.1f})")
        else:
            tail = s.y[:, s.t > 0.75 * s.t[-1]]
            print(f"  e = {mult:.2f} e_c : bounded, gamma amplitude = "
                  f"{tail[0].max()-tail[0].min():.5f} s^-1")
