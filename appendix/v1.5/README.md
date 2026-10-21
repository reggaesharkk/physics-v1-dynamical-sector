# Physics v1.0 — Dynamical Sector: Appendix A v1.5 (Upgraded Lake-Verified & VRK v0.3.1 Release)

*(Additive to frozen Physics v1.0 [DOI: 10.17605/OSF.IO/N3DQU](https://doi.org/10.17605/OSF.IO/N3DQU), Appendix A v1.4 [DOI: 10.17605/OSF.IO/U7M6H](https://doi.org/10.17605/OSF.IO/U7M6H), and Appendix A v1.4.1 [DOI: 10.17605/OSF.IO/S7WHX](https://doi.org/10.17605/OSF.IO/S7WHX); verified under IntentSeal VRK v0.3.1 [DOI: 10.5281/zenodo.23018459](https://doi.org/10.5281/zenodo.23018459), Prototype Lineage v0.1.1–v0.5.0 [DOI: 10.5281/zenodo.23016445](https://doi.org/10.5281/zenodo.23016445), and STRENGTH-INTENT-NS-LEAN [DOI: 10.5281/zenodo.23474505](https://doi.org/10.5281/zenodo.23474505)).*

* **Zenodo Archive DOIs:** <https://doi.org/10.5281/zenodo.23497142> | <https://doi.org/10.5281/zenodo.23501526>
* **VRK & Ecosystem Lineage DOIs:** <https://doi.org/10.5281/zenodo.23018459> | <https://doi.org/10.5281/zenodo.23016445> | <https://doi.org/10.5281/zenodo.23474505>
* **Author:** Prince Upadhyay (`starxshark@gmail.com`, ORCID: [0009-0002-1170-4487](https://orcid.org/0009-0002-1170-4487))
* **Release Date:** October 21, 2026

## Summary of Upgraded v1.5 Contributions & VRK Epistemic Classification

1. **Conditional Holographic Closure of Gate 0 (Proposition 1 — `CONDITIONAL_FRONTIER` / `OPEN`):** Formulates an explicit covariant dictionary linking the fine-grained von Neumann entropy ceiling $H_{\max}$ of a causal-diamond observer subsystem $\mathcal{D}(\mathcal{A})$ to the area of its Hubeny–Rangamani–Takayanagi (HRT) extremal surface $\Sigma_{\text{HRT}}$, $H_{\max} = \operatorname{Area}(\Sigma_{\text{HRT}})/(4\ell_P^2 \ln 2)$, while maintaining strict epistemic separation from non-geometric tensor factorizations (where Gate 0 remains `OPEN`).
2. **Positivity-Preserving Soft-Wall Dynamical Completion & Global Trapping Box Theorem (Theorem 3 — `ANALYTIC_THEOREM`):**
   * Gates the irreversible-erasure sink with $\Psi_{\epsilon_H}(H_{\text{obs}}) = \tanh(H_{\text{obs}}/\epsilon_H)$ and gates the derivative-feedback channel with $\Phi_{\epsilon_I}(\dot{I}) = \tanh(\dot{I}/\epsilon_I)$.
   * Proves via Nagumo's subtangentiality theorem that both the positive orthant $\mathbb{R}^3_+$ and the compact trapping box $\mathcal{B} = [0,\gamma_{\max}]\times[0,H_{\max}]\times[0,\dot{I}_{\max}]$ are globally forward-invariant for all $t \ge 0$ and all positive parameters (`ANALYTIC_THEOREM`).
   * Demonstrates numerically (`REPRODUCED_RESULT`) via multi-initial-condition Poincaré return-map integration and linearized transverse Floquet multiplier evaluation ($\rho(DP) = 8.96 \times 10^{-6} \ll 1$) that post-Hopf trajectories ($e > e_c$) converge onto an attracting periodic relaxation oscillation inside $\mathcal{B}$.
3. **Exact Interior Equilibrium, SymPy Tensor Audit & $\epsilon$-Scaling Bounds (Proposition 4 — `ANALYTIC_THEOREM` + `REPRODUCED_RESULT`):**
   * Because $\left.dH_{\text{obs}}/dt\right|_* = 0$ at any equilibrium, the first derivative of the processing gate vanishes **identically** in the equilibrium Jacobian, leaving $\dot{I}^* = f\mathcal{P}_{\text{input}}/g$ and $\gamma^* = K\gamma_{\max}/(b\gamma_{\max}+K)$ exact.
   * Independent `SymPy` symbolic differentiation verifies that $f_1=f_2=f_3=0$ at steady state and that the analytical 1st-, 2nd-, and 3rd-order Taylor tensors ($J_{\text{v1.5}}, B_{\text{v1.5}}, C_{1,\text{v1.5}}=0, C_{2,\text{v1.5}}, C_{3,\text{v1.5}}$) match symbolic differentiation of Eqs. (3)–(5) with zero residual.
   * Across a 5-point parametric sweep $\epsilon_H = \epsilon_I = \epsilon \in \{0.10, 0.05, 0.02, 0.01, 0.005\}$ on the v1.3/v1.4 audit slice, $\|J_{\text{v1.5}} - J_{\text{v1.4}}\|_F$ and $|\Delta l_1|$ decay exponentially from $2.21 \times 10^{-8}$ and $1.75 \times 10^{-6}$ at $\epsilon = 0.10$, to $1.48 \times 10^{-86}$ and $1.11 \times 10^{-82}$ at $\epsilon = 0.01$ (where $1 - \tanh(\dot{I}^*/\epsilon_I) = 2.77 \times 10^{-87}$ and $\operatorname{sech}^2(H_{\text{obs}}^*/\epsilon_H) = 5.38 \times 10^{-695}$), and $2.05 \times 10^{-173}$ and $6.11 \times 10^{-169}$ at $\epsilon = 0.005$.
4. **Full 6-Face Machine-Checked Lean 4 Lake Package (`BoundaryVerification.lean` / `boundary_verification.lean`, `lakefile.lean`, `lake-manifest.json`, `lean-toolchain`):**
   * Formalizes the exact upgraded vector field and compact box bounds (`M_H`, `I_dot_max`) over Mathlib's `Real` (`ℝ`) under `leanprover/lean4:v4.36.0-rc1` (Mathlib `10156080d0e7997b71f3ef86bd6f0211b42ab90d`) and proves all six boundary face and ceiling theorems (`dgamma_dt_nonneg_at_boundary`, `dgamma_dt_neg_at_ceiling`, `dHobs_dt_nonneg_at_boundary`, `dHobs_dt_neg_at_ceiling`, `dIdot_dt_pos_at_boundary`, `dIdot_dt_nonpos_at_ceiling`), the auxiliary bound `dHobs_dt_le_M_H`, and the unified 6-face certificate `compact_box_nagumo_certificate` using explicit monotonicity lemmas (`mul_le_mul_of_nonneg_left`, `mul_le_mul_of_nonneg_right`, `mul_assoc`, `mul_div_cancel₀`, and `linarith`) with zero `sorry` axioms and zero `nlinarith` heuristics.

## Six-Layer Mechanical & VRK v0.3.1 Verification Chain

| Layer | Tool / Module | VRK Claim Class | Certified Claim & Quantitative Bound | Manuscript Scope |
| :--- | :--- | :--- | :--- | :--- |
| **1. Formal Kernel** | Lean 4 Lake (`BoundaryVerification.lean` / `boundary_verification.lean`) | `ANALYTIC_THEOREM` | All 6 face/ceiling conditions of $\mathcal{B}$, `dHobs_dt_le_M_H`, and `compact_box_nagumo_certificate` (`0 sorry`, `0 nlinarith`, `leanprover/lean4:v4.36.0-rc1`, Mathlib `10156080d0e7`) | Theorem 3 (Global Containment) |
| **2. Symbolic Algebra** | `SymPy` (`verification_patch_v1_5.py`) | `ANALYTIC_THEOREM` | Exact equilibrium ($f_1=f_2=f_3=0$) and zero symbolic residual for $J_{\text{v1.5}}, B_{\text{v1.5}}, C_{1,\text{v1.5}}=0, C_{2,\text{v1.5}}, C_{3,\text{v1.5}}$ | Proposition 4 (Normal-Form Tensors) |
| **3. 60-Digit Spectral** | `mpmath` 60-digit (`verification_patch_v1_5.py`) | `REPRODUCED_RESULT` | $e_c = 135/26$, $\omega_c = \sqrt{2/13}$, and $l_{1,\text{v1.4}}$ verified against 50-digit reference ($|\Delta| = 9.38 \times 10^{-52}$) | Section 6 / Table 1 (v1.4 Baseline) |
| **4. 750/1450-Digit Sweep** | `mpmath` 750/1450-digit (`verification_patch_v1_5.py`) | `REPRODUCED_RESULT` | Two-gate scales at $\epsilon = 0.01$ and 5-point exponential convergence sweep across $\epsilon \in [0.005, 0.10]$ | Proposition 4 / Tables 1–2 |
| **5. Return Map & Floquet** | `SciPy` `LSODA` (`verification_patch_v1_5.py`) | `REPRODUCED_RESULT` | 6-face grid check, post-Hopf confinement ($e/e_c \in [0.9, 2.0]$), 3-IC Poincaré convergence ($\max\|\Delta y_{\text{IC}}\|_2 = 1.83\times 10^{-8} < 10^{-6}$), period $T = 18.95704705\text{ s}$ (spread $< 10^{-6}\text{ s}$ across x86_64/ARM64), and transverse Floquet radius $\rho(DP) = 8.96\times 10^{-6} \ll 1$ | Section 6 / Table 3 (Attracting Orbit) |
| **6. VRK v0.3.1 Audit** | `verification_patch_v1_5.py` ([10.5281/zenodo.23018459](https://doi.org/10.5281/zenodo.23018459)) | `CERTIFIED` (Schema Gate) | Validates `intentseal-vrk-claim-v2` roles, rejects illegal `REPRODUCED_RESULT -> ANALYTIC_THEOREM` promotion, and emits telemetry-free deterministic certificate digest `99325d5313ae791cf001b3efc16e6631425d46f6343c244396d9bc65d366634c` | Section 1 & Section 6 (VRK Provenance) |

## Bundle Inventory & Reproducibility

| File | Description |
| :--- | :--- |
| `Physics_v1_5_Appendix_A.pdf` | Compiled 6-page publication-ready PDF of Appendix A v1.5 |
| `appendix_a_v1_5.tex` | Self-contained LaTeX source manuscript (compiles cleanly with `lualatex` or `pdflatex`) |
| `BoundaryVerification.lean` | Primary Lean 4 Lake target covering all 6 faces of the compact box $\mathcal{B}$ (`0 sorry`, `0 nlinarith`) |
| `boundary_verification.lean` | Byte-identical mirror of `BoundaryVerification.lean` for backward compatibility with v1.5 manuscript scripts |
| `lakefile.lean` | Lean 4 Lake build configuration defining package `boundaryVerification` and library target `BoundaryVerification` |
| `lake-manifest.json` | Deterministic Lake dependency lockfile pinning Mathlib (`10156080d0e7997b71f3ef86bd6f0211b42ab90d`) |
| `lean-toolchain` | Lean 4 toolchain pin (`leanprover/lean4:v4.36.0-rc1`) |
| `verification_patch_v1_5.py` | 60/750/1450-digit `mpmath`, `SymPy` tensor audit, $\epsilon$-scaling sweep, 6-face LSODA, 3-IC Poincaré, Floquet, Lake manifest & VRK v0.3.1 verifier |
| `launch_sandbox.py` | Dependency-clean local web dashboard (`http://localhost:8080/`) visualizing post-Hopf confinement |
| `README.md` | Release overview, 6-layer VRK verification ledger, `lake build` instructions, and SHA-256 checksum manifest |

### Quick Verification Commands

```bash
# 1. Verify the Lean 4 6-face compact-box theorems via Lake (requires elan / Lean 4 v4.36.0-rc1):
lake exe cache get
lake build

# 2. Run the 60/750/1450-digit spectral, SymPy tensor, eps-sweep, 6-face Nagumo, 3-IC Poincare, Floquet & VRK v0.3.1 suite:
python3 verification_patch_v1_5.py

# 3. Launch the interactive local phase-space web dashboard:
python3 launch_sandbox.py
```

## SHA-256 Checksum Manifest

| File | SHA-256 |
| :--- | :--- |
| `Physics_v1_5_Appendix_A.pdf` | `7c74a125da33970851cdb5bbc3ee5622c820b996c4b097d3d4464a3450842cad` |
| `appendix_a_v1_5.tex` | `05e82d8f93664a9ad0153802c4cfcd8153137c64f0b37d2c9cd93f8126cef7f2` |
| `BoundaryVerification.lean` | `4dce891b0867a75bacaf6fed63166d3534cdbeccc0d72d5c2aa683fa9a94958d` |
| `boundary_verification.lean` | `4dce891b0867a75bacaf6fed63166d3534cdbeccc0d72d5c2aa683fa9a94958d` |
| `lakefile.lean` | `d8fa0f64b9a781c9e6b811a6d5f0ba872d9f6cfba573c43238b54b45f3cfce8c` |
| `lake-manifest.json` | `54ca7b4da4159237d9913c799616276a775c8ee97a4aa5b1edfc67bb923739b7` |
| `lean-toolchain` | `964acf49a540b2fbb4d25edc186eb68236afd8020473dfad7ccb08dc6ffa1d66` |
| `verification_patch_v1_5.py` | `7076789c4ec6b37543bb6aae8c5c091c940589931b88dfb4fc6f8d4f1065d2ca` |
| `launch_sandbox.py` | `ab044a634a20805a6b5bd97b15f32fde7dfac84d100c38623de20f02cd908f07` |
