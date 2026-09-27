#!/usr/bin/env python3
"""Audit the separately supplied recursive-cosmology toy sandbox.

This is not the Physics v1.0 Appendix A dynamical system.
"""
import numpy as np


def equilibrium(a=1.2, b=0.35, c=1.0, d=0.30, e=0.55, f=0.25,
                g=0.45, T=1.0):
    assert min(a, b, c, d, e, f, g, T) > 0

    def values(R):
        psi = c * R / (c * R + d)
        gamma = (e * psi + f * T) / g
        return psi, gamma

    def balance(R):
        _, gamma = values(R)
        return a * T * gamma * (1 - R) - b * R

    lo, hi = 0.0, 1.0
    for _ in range(100):
        mid = (lo + hi) / 2
        if balance(mid) > 0:
            lo = mid
        else:
            hi = mid
    R = (lo + hi) / 2
    psi, gamma = values(R)
    x, y = a * T * gamma + b, c * R + d
    J = np.array([[-x, 0, a * T * (1 - R)],
                  [c * (1 - psi), -y, 0],
                  [0, e, -g]])
    loop_gain = a * T * (1 - R) * c * (1 - psi) * e
    diagonal_product = x * y * g
    assert max(abs(z) for z in (balance(R), c * R * (1 - psi) - d * psi,
                                e * psi + f * T - g * gamma)) < 1e-12
    assert loop_gain < diagonal_product
    return np.array([R, psi, gamma]), np.linalg.eigvals(J), loop_gain / diagonal_product


def proximity(U, C):
    norm_u, norm_c = np.linalg.norm(U), np.linalg.norm(C)
    if norm_u == 0 or norm_c == 0:
        raise ValueError("normalized proximity undefined for zero state")
    return 1 - min(1., np.linalg.norm(U / norm_u - C / norm_c) / np.sqrt(2))


def main():
    cases = (("baseline", {}), ("higher c", {"c": 2.2}),
             ("higher b", {"b": 0.75}))
    for name, kwargs in cases:
        state, eigenvalues, ratio = equilibrium(**kwargs)
        print(name, "equilibrium", np.array2string(state, precision=9),
              "max Re eigenvalue", f"{max(eigenvalues.real):.9f}",
              "loop ratio", f"{ratio:.9f}")
    state, _, _ = equilibrium()
    fidelity = state[0] * state[1]
    U = np.eye(4)
    print("fidelity R*Psi", f"{fidelity:.9f}")
    print("zero-noise proximity", proximity(U, fidelity * U),
          "raw fixed-point error", f"{np.linalg.norm(U - fidelity * U):.9f}")
    for seed in range(5):
        noise = np.random.default_rng(seed).normal(0, .1, U.shape)
        C = fidelity * U + (1 - fidelity) * noise
        print("seed", seed, "proximity", f"{proximity(U, C):.9f}")


if __name__ == "__main__":
    main()
