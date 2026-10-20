# Physics v1.0 — Dynamical Sector: Appendix A v1.5 (Upgraded & Formally Verified Release)

*(Additive to frozen Physics v1.0 [DOI: 10.17605/OSF.IO/N3DQU](https://doi.org/10.17605/OSF.IO/N3DQU), Appendix A v1.4 [DOI: 10.17605/OSF.IO/U7M6H](https://doi.org/10.17605/OSF.IO/U7M6H), and Appendix A v1.4.1 [DOI: 10.17605/OSF.IO/S7WHX](https://doi.org/10.17605/OSF.IO/S7WHX)).*

* **Zenodo Archive DOIs:** [https://doi.org/10.5281/zenodo.23497142](https://doi.org/10.5281/zenodo.23497142) | [https://doi.org/10.5281/zenodo.23501526](https://doi.org/10.5281/zenodo.23501526)
* **Author:** Prince Upadhyay (`starxshark@gmail.com`)
* **Release Date:** October 20, 2026

## Summary of Upgraded v1.5 Contributions

1. **Conditional Holographic Closure of Gate 0 (Proposition 1):** Formulates an explicit covariant dictionary linking the fine-grained von Neumann entropy ceiling $H_{\max}$ of a causal-diamond observer subsystem $\mathcal{D}(\mathcal{A})$ to the area of its Hubeny–Rangamani–Takayanagi (HRT) extremal surface $\Sigma_{\text{HRT}}$, $H_{\max} = \operatorname{Area}(\Sigma_{\text{HRT}})/(4\ell_P^2 \ln 2)$, while maintaining strict epistemic separation from non-geometric tensor factorizations.
2. **Positivity-Preserving Soft-Wall Dynamical Completion & Global Trapping Box Theorem (Theorem 3):**
   * Gates the irreversible-erasure sink with $\Psi_{\epsilon_H}(H_{\text{obs}}) = \tanh(H_{\text{obs}}/\epsilon_H)$ and gates the derivative-feedback channel with $\Phi_{\epsilon_I}(\dot{I}) = \tanh(\dot{I}/\epsilon_I)$.
   * Proves via Nagumo's subtangentiality theorem that both the positive orthant $\mathbb{R}^3_+$ and the compact trapping box $\mathcal{B} = [0,\gamma_{\max}]\times[0,H_{\max}]\times[0,\dot{I}_{\max}]$ are globally forward-invariant for all $t \ge 0$ and all positive parameters (an analytical containment theorem).
   * Demonstrates numerically via multi-initial-condition Poincaré return-map integration and linearized transverse Floquet multiplier evaluation ($\rho(DP) = 8.96 \times 10^{-6} \ll 1$) that post-Hopf trajectories ($e > e_c$) converge onto an attracting periodic relaxation oscillation inside $\mathcal{B}$.
3. **Exact Interior Equilibrium, SymPy Tensor Audit & $\epsilon$-Scaling Bounds (Proposition 4):**
   * Because $dH_{\text{obs}}/dt|_* = 0$ at any equilibrium, the first derivative of the processing gate vanishes **identically** in the equilibrium Jacobian, leaving $\dot{I}^* = f\mathcal{P}_{\text{input}}/g$ and $\gamma^* = K\gamma_{\max}/(b\gamma_{\max}+K)$ exact.
   * Independent `SymPy` symbolic differentiation verifies that $f_1=f_2=f_3=0$ at steady state and that the analytical 1st-, 2nd-, and 3rd-order Taylor tensors ($J_{\text{v1.5}}, B_{\text{v1.5}}, C_{1,\text{v1.5}}=0, C_{2,\text{v1.5}}, C_{3,\text{v1.5}}$) match symbolic differentiation of Eqs. (3)–(5) with zero residual.
   * Across a 5-point parametric sweep $\epsilon_H = \epsilon_I = \epsilon \in \{0.10, 0.05, 0.02, 0.01, 0.005\}$ on the v1.3/v1.4 audit slice, $\|J_{\text{v1.5}} - J_{\text{v1.4}}\|_F$ and $|\Delta l_1|$ decay exponentially from $2.21 \times 10^{-8}$ and $1.75 \times 10^{-6}$ at $\epsilon = 0.10$, to $1.48 \times 10^{-86}$ and $1.11 \times 10^{-82}$ at $\epsilon = 0.01$ (where $1 - \tanh(\dot{I}^*/\epsilon_I) = 2.77 \times 10^{-87}$ and $\operatorname{sech}^2(H_{\text{obs}}^*/\epsilon_H) = 5.38 \times 10^{-695}$), and $2.05 \times 10^{-173}$ and $6.11 \times 10^{-169}$ at $\epsilon = 0.005$.
4. **Full 6-Face Machine-Checked Lean 4 Formal Proofs (`boundary_verification.lean`):**
   * Formalizes the exact upgraded vector field and compact box bounds (`M_H`, `I_dot_max`) over Mathlib's `Real` (`ℝ`) and proves all six boundary face and ceiling theorems (`dgamma_dt_nonneg_at_boundary`, `dgamma_dt_neg_at_ceiling`, `dHobs_dt_nonneg_at_boundary`, `dHobs_dt_neg_at_ceiling`, `dIdot_dt_pos_at_boundary`, `dIdot_dt_nonpos_at_ceiling`), the auxiliary bound `dHobs_dt_le_M_H`, and the unified 6-face certificate `compact_box_nagumo_certificate` using explicit monotonicity lemmas (`mul_le_mul_of_nonneg_left`, `mul_le_mul_of_nonneg_right`, `mul_assoc`, `mul_div_cancel₀`, and `linarith`) with zero `sorry` axioms and zero `nlinarith` heuristics.

## Five-Layer Mechanical Verification Chain

| Layer | Tool / Module | Certified Claim & Quantitative Bound | Manuscript Scope |
| :--- | :--- | :--- | :--- |
| **1. Formal Kernel** | Lean 4 (`boundary_verification.lean`) | All 6 face/ceiling conditions of $\mathcal{B}$, `dHobs_dt_le_M_H`, and `compact_box_nagumo_certificate` (`0 sorry`, `0 nlinarith`) | Theorem 3 (Global Containment) |
| **2. Symbolic Algebra** | `SymPy` (`verification_patch_v1_5.py`) | Exact equilibrium ($f_1=f_2=f_3=0$) and zero symbolic residual for $J_{\text{v1.5}}, B_{\text{v1.5}}, C_{1,\text{v1.5}}=0, C_{2,\text{v1.5}}, C_{3,\text{v1.5}}$ | Proposition 4 (Normal-Form Tensors) |
| **3. 60-Digit Spectral** | `mpmath` 60-digit (`verification_patch_v1_5.py`) | $e_c = 135/26$, $\omega_c = \sqrt{2/13}$, and $l_{1,\text{v1.4}}$ verified against 50-digit reference ($|\Delta| = 9.38 \times 10^{-52}$) | Section 6 / Table 1 (v1.4 Baseline) |
| **4. 750/1450-Digit Sweep** | `mpmath` 750/1450-digit (`verification_patch_v1_5.py`) | Two-gate scales at $\epsilon = 0.01$ and 5-point exponential convergence sweep across $\epsilon \in [0.005, 0.10]$ | Proposition 4 / Tables 1–2 |
| **5. Return Map & Floquet** | `SciPy` `LSODA` (`verification_patch_v1_5.py`) | 6-face grid check, post-Hopf confinement ($e/e_c \in [0.9, 2.0]$), 3-IC Poincaré convergence ($\max\|\Delta y_{\text{IC}}\|_2 = 1.83\times 10^{-8} < 10^{-6}$), period $T = 18.95704705\text{ s}$ (spread $< 10^{-6}\text{ s}$ across x86\_64/ARM64), and transverse Floquet radius $\rho(DP) = 8.96\times 10^{-6} \ll 1$ | Section 6 / Table 3 (Attracting Orbit) |

## Bundle Inventory & Reproducibility

| File | Description |
| :--- | :--- |
| `Physics_v1_5_Appendix_A.pdf` | Compiled 6-page publication-ready PDF of Appendix A v1.5 |
| `appendix_a_v1_5.tex` | Self-contained LaTeX source manuscript (compiles cleanly with `lualatex` or `pdflatex`) |
| `boundary_verification.lean` | Lean 4 / Mathlib formalization covering all 6 faces of the compact box $\mathcal{B}$ |
| `verification_patch_v1_5.py` | 60/750/1450-digit `mpmath`, `SymPy` tensor audit, $\epsilon$-scaling sweep, 6-face LSODA, 3-IC Poincaré & Floquet verifier |
| `launch_sandbox.py` | Dependency-clean local web dashboard (`http://localhost:8080/`) visualizing post-Hopf confinement |
| `README.md` | Release overview, 5-layer verification ledger, and SHA-256 checksum manifest |

### Quick Verification Commands

```bash
# Run the 60/750/1450-digit spectral, SymPy tensor, eps-sweep, 6-face Nagumo, 3-IC Poincare & Floquet suite:
python3 verification_patch_v1_5.py

# Launch the interactive local phase-space web dashboard:
python3 launch_sandbox.py
```

## SHA-256 Checksum Manifest

| File | SHA-256 |
| :--- | :--- |
| `Physics_v1_5_Appendix_A.pdf` | `b3eacefb415a839397fc34b6bc71af2388ef1f64e1e0bdb2995bd7e4a7e20bbf` |
| `appendix_a_v1_5.tex` | `54f1412146dd635dd33dde6ebe4fb16e4f1cd1544c5b8b7d2cd1fccc0fad600f` |
| `boundary_verification.lean` | `ca158b624dfcd4ec649ac66b6742929211fe6e5b24bf8f95adea4a3f974a98a2` |
| `verification_patch_v1_5.py` | `9efb6f15045c924673b5d4c4f9da055bc532bce13b8199b99dbd82dc50e88ce7` |
| `launch_sandbox.py` | `ab044a634a20805a6b5bd97b15f32fde7dfac84d100c38623de20f02cd908f07` |
