# Physics v1.0 — Dynamical Sector: Appendix A v1.5 (Upgraded & Formally Verified Release)

*(Additive to frozen Physics v1.0 [DOI: 10.17605/OSF.IO/N3DQU](https://doi.org/10.17605/OSF.IO/N3DQU), Appendix A v1.4 [DOI: 10.17605/OSF.IO/U7M6H](https://doi.org/10.17605/OSF.IO/U7M6H), and Appendix A v1.4.1 [DOI: 10.17605/OSF.IO/S7WHX](https://doi.org/10.17605/OSF.IO/S7WHX)).*

* **Zenodo Archive DOIs:** [https://doi.org/10.5281/zenodo.23497142](https://doi.org/10.5281/zenodo.23497142) | [https://doi.org/10.5281/zenodo.23501526](https://doi.org/10.5281/zenodo.23501526)
* **Author:** Prince Upadhyay (`starxshark@gmail.com`)
* **Release Date:** October 20, 2026

## Summary of Upgraded v1.5 Contributions

1. **Conditional Holographic Closure of Gate 0 (Proposition 1):** Formulates an explicit covariant dictionary linking the fine-grained von Neumann entropy ceiling $H_{\max}$ of a causal-diamond observer subsystem $\mathcal{D}(\mathcal{A})$ to the area of its Hubeny–Rangamani–Takayanagi (HRT) extremal surface $\Sigma_{\text{HRT}}$, $H_{\max} = \operatorname{Area}(\Sigma_{\text{HRT}})/(4\ell_P^2 \ln 2)$, while maintaining strict epistemic separation from non-geometric tensor factorizations.
2. **Positivity-Preserving Soft-Wall Dynamical Completion & Global Trapping Box Theorem (Theorem 3):**
   * Gates the irreversible-erasure sink with $\Psi_{\epsilon_H}(H_{\text{obs}}) = \tanh(H_{\text{obs}}/\epsilon_H)$ and gates the derivative-feedback channel with $\Phi_{\epsilon_I}(\dot{I}) = \tanh(\dot{I}/\epsilon_I)$.
   * Proves via Nagumo's subtangentiality theorem that both the positive orthant $\mathbb{R}^3_+$ and the compact trapping box $\mathcal{B} = [0,\gamma_{\max}]\times[0,H_{\max}]\times[0,\dot{I}_{\max}]$ are globally forward-invariant for all $t \ge 0$ and all positive parameters.
   * Eliminates the finite-time escape to $\gamma < 0$ across the subcritical Hopf boundary ($e > e_c$), capturing post-Hopf trajectories onto a globally bounded relaxation oscillation inside $\mathcal{B}$.
3. **Exact Interior Equilibrium & Two-Scale Gate Perturbation Bounds (Proposition 4):**
   * Because $dH_{\text{obs}}/dt|_* = 0$ at any equilibrium, the first derivative of the processing gate vanishes **identically** in the equilibrium Jacobian, leaving $\dot{I}^* = f\mathcal{P}_{\text{input}}/g$ and $\gamma^* = K\gamma_{\max}/(b\gamma_{\max}+K)$ exact.
   * At the v1.3/v1.4 audit slice with $\epsilon_H = \epsilon_I = 0.01$, the processing gate deviation is $1 - \tanh(\dot{I}^*/\epsilon_I) = 2.77 \times 10^{-87}$ (giving $\|J_{\text{v1.5}} - J_{\text{v1.4}}\|_F = 1.48 \times 10^{-86}$, $|e_{c,\text{v1.5}} - e_{c,\text{v1.4}}| = 1.44 \times 10^{-86}$, and $|l_{1,\text{v1.5}} - l_{1,\text{v1.4}}| = 1.11 \times 10^{-82}$), while the entropy gate deviation is $\operatorname{sech}^2(H_{\text{obs}}^*/\epsilon_H) = 5.38 \times 10^{-695}$ (shifting $H_{\text{obs}}^*$ by $5.38 \times 10^{-695}$). Both scales are orders of magnitude below the $10^{-50}$ threshold.
4. **Full 6-Face Machine-Checked Lean 4 Formal Proofs (`boundary_verification.lean`):**
   * Formalizes the exact upgraded vector field and compact box bounds (`M_H`, `I_dot_max`) over Mathlib's `Real` (`ℝ`) and proves all six boundary face and ceiling theorems (`dgamma_dt_nonneg_at_boundary`, `dgamma_dt_neg_at_ceiling`, `dHobs_dt_nonneg_at_boundary`, `dHobs_dt_neg_at_ceiling`, `dIdot_dt_pos_at_boundary`, `dIdot_dt_nonpos_at_ceiling`), the auxiliary bound `dHobs_dt_le_M_H`, and the unified 6-face certificate `compact_box_nagumo_certificate` with zero `sorry` axioms.

## Bundle Inventory & Reproducibility

| File | Description |
| :--- | :--- |
| `Physics_v1_5_Appendix_A.pdf` | Compiled 6-page publication-ready PDF of Appendix A v1.5 |
| `appendix_a_v1_5.tex` | Self-contained LaTeX source manuscript (compiles cleanly with `lualatex` or `pdflatex`) |
| `boundary_verification.lean` | Lean 4 / Mathlib formalization covering all 6 faces of the compact box $\mathcal{B}$ |
| `verification_patch_v1_5.py` | 60/750-digit `mpmath` Kuznetsov $l_1$ verifier, Frobenius Jacobian audit, and 6-face LSODA test |
| `launch_sandbox.py` | Dependency-clean local web dashboard (`http://localhost:8080/`) visualizing post-Hopf confinement |
| `README.md` | Release overview, theorem ledger, and SHA-256 checksum manifest |

### Quick Verification Commands

```bash
# Run the 60/750-digit algebraic, Frobenius Jacobian, and 6-face global confinement verification suite:
python3 verification_patch_v1_5.py

# Launch the interactive local phase-space web dashboard:
python3 launch_sandbox.py
```

## SHA-256 Checksum Manifest

| File | SHA-256 |
| :--- | :--- |
| `Physics_v1_5_Appendix_A.pdf` | `b3c13ea6b2ecd933e8423bb7314c914ce6150240fc0e173bf18badd4350afdc9` |
| `appendix_a_v1_5.tex` | `b8e6a631ec41d286b7c657146dde1dec6e7f32f50ae836379fc1ad9dd209fdea` |
| `boundary_verification.lean` | `19f16e30a18491e206cde7bebc4e96e60e3681c77d32605d6ca2c866903255ad` |
| `verification_patch_v1_5.py` | `b91a31d50cf618d43971cff8e0d4570edc44c2bbd4d802db0becaae03ab45a90` |
| `launch_sandbox.py` | `ab044a634a20805a6b5bd97b15f32fde7dfac84d100c38623de20f02cd908f07` |
