# Physics v1.0 — Dynamical Sector: Appendix A v1.5 (Upgraded Lake-Verified & VRK v0.3.1 Release)

*(Additive to frozen Physics v1.0 [DOI: 10.17605/OSF.IO/N3DQU], Appendix A v1.4 [DOI: 10.17605/OSF.IO/U7M6H](https://doi.org/10.17605/OSF.IO/U7M6H), and Appendix A v1.4.1 [DOI: 10.17605/OSF.IO/S7WHX](https://doi.org/10.17605/OSF.IO/S7WHX); verified under IntentSeal VRK v0.3.1 [DOI: 10.5281/zenodo.23018459](https://doi.org/10.5281/zenodo.23018459), Prototype Lineage v0.1.1-v0.5.0 [DOI: 10.5281/zenodo.23016445](https://doi.org/10.5281/zenodo.23016445), and STRENGTH-INTENT-NS-LEAN [DOI: 10.5281/zenodo.23474505](https://doi.org/10.5281/zenodo.23474505)).*

* **Zenodo Archive DOIs:** <https://doi.org/10.5281/zenodo.23497142> | <https://doi.org/10.5281/zenodo.23501526>
* **VRK & Ecosystem Lineage DOIs:** <https://doi.org/10.5281/zenodo.23018459> | <https://doi.org/10.5281/zenodo.23016445> | <https://doi.org/10.5281/zenodo.23474505>
* **Author:** Prince Upadhyay (`starxshark@gmail.com`, ORCID: `0009-0002-1170-4487`)
* **Release Date:** October 21, 2026

## Summary of Upgraded v1.5 Contributions & VRK Epistemic Classification

1. **Conditional Holographic Closure of Gate 0 (Proposition 1 — `CONDITIONAL_FRONTIER` / `OPEN`):** Formulates an explicit covariant dictionary linking the fine-grained von Neumann entropy ceiling $H_{\max}$ of a causal-diamond observer subsystem $\mathcal{D}(\mathcal{A})$ to the area of its Hubeny-Rangamani-Takayanagi (HRT) extremal surface $\Sigma_{\text{HRT}}$, $H_{\max} = \operatorname{Area}(\Sigma_{\text{HRT}})/(4\ell_P^2 \ln 2)$, while maintaining strict epistemic separation from non-geometric tensor factorizations (where Gate 0 remains `OPEN`).
2. **Positivity-Preserving Soft-Wall Dynamical Completion & Gain-Dependent Trapping Box Theorem (Theorem 3 — `ANALYTIC_THEOREM`):**
   * Gates the irreversible-erasure sink with $\Psi_{\epsilon_H}(H_{\text{obs}}) = \tanh(H_{\text{obs}}/\epsilon_H)$ and gates the derivative-feedback channel with $\Phi_{\epsilon_I}(\dot{I}) = \tanh(\dot{I}/\epsilon_I)$.
   * Proves via Nagumo's subtangentiality theorem that both the positive orthant $\mathbb{R}^3_+$ and the gain-dependent compact trapping box $\mathcal{B}(e) = [0,\gamma_{\max}]\times[0,H_{\max}]\times[0,\dot{I}_{\max}(e)]$ with $\dot{I}_{\max}(e) = (e M_H + f\mathcal{P}_{\text{input}})/g$ are globally forward-invariant for all $t \ge 0$ and all positive parameters (`ANALYTIC_THEOREM`).
   * Demonstrates numerically (`REPRODUCED_RESULT`) via multi-initial-condition Poincare return-map integration replicated across independent `LSODA` (Adams/BDF) and `DOP853` (8th-order Runge-Kutta) solvers, the Liouville orbital divergence integral ($\int_0^T \operatorname{div} F(y(t))\,dt = -10405.41 \implies \det(DP) \approx 10^{-4519} \ll 1$), and finite-difference transverse Floquet upper bounds ($\rho_{\text{FD}}(DP) < 10^{-8}$ at $\text{rtol}=10^{-12}, \Delta h = 10^{-2}$, below the $\sim \text{rtol}/(2\Delta h) \sim 10^{-6}$ solver noise floor at $\text{rtol}=10^{-9}, \Delta h = 10^{-3}$) that post-Hopf trajectories ($e > e_c$) settle onto an attracting periodic relaxation oscillation inside $\mathcal{B}(e)$.
3. **Exact Interior Equilibrium, SymPy Tensor Audit & $\epsilon$-Scaling Bounds (Proposition 4 — `ANALYTIC_THEOREM` + `REPRODUCED_RESULT`):**
   * **Analytic Identity (`ANALYTIC_THEOREM`):** Because $\left.dH_{\text{obs}}/dt\right|_* = 0$ at any equilibrium, the first derivative of the processing gate vanishes **identically** in the equilibrium Jacobian, leaving $\dot{I}^* = f\mathcal{P}_{\text{input}}/g$ and $\gamma^* = K\gamma_{\max}/(b\gamma_{\max}+K)$ exact. Independent `SymPy` symbolic differentiation verifies $f_1=f_2=f_3=0$ at steady state and zero symbolic residual across all 1st-, 2nd-, and 3rd-order Taylor tensors ($J_{\text{v1.5}}, B_{\text{v1.5}}, C_{1,\text{v1.5}}=0, C_{2,\text{v1.5}}, C_{3,\text{v1.5}}$).
   * **Multiprecision Scaling Sweep (`REPRODUCED_RESULT`):** Across $\epsilon_H = \epsilon_I = \epsilon \in \{0.10, 0.05, 0.02, 0.01, 0.005\}$ on the v1.3/v1.4 audit slice, $\|J_{\text{v1.5}} - J_{\text{v1.4}}\|_F$ and $|\Delta l_1|$ decay exponentially from $2.21 \times 10^{-8}$ and $1.75 \times 10^{-6}$ at $\epsilon = 0.10$, to $1.48 \times 10^{-86}$ and $1.11 \times 10^{-82}$ at $\epsilon = 0.01$ (where $1 - \tanh(\dot{I}^*/\epsilon_I) = 2.77 \times 10^{-87}$, agreeing with the asymptotic formula $2e^{-2\dot{I}^*/\epsilon_I}$ to relative error $< 10^{-86}$, and $\operatorname{sech}^2(H_{\text{obs}}^*/\epsilon_H) = 5.38 \times 10^{-695}$), and $2.05 \times 10^{-173}$ and $6.11 \times 10^{-169}$ at $\epsilon = 0.005$.
4. **Full 6-Face Machine-Checked Lean 4 Lake Package (`BoundaryVerification.lean`, `lakefile.lean`, `lake-manifest.json`, `lean-toolchain`):**
   * Formalizes the upgraded vector field and compact box bounds (`M_H`, `I_dot_max`) over Mathlib's `Real` (`ℝ`) under `leanprover/lean4:v4.36.0-rc1` (Mathlib `10156080d0e7997b71f3ef86bd6f0211b42ab90d`) and proves all six boundary face and ceiling theorems (`dgamma_dt_nonneg_at_boundary`, `dgamma_dt_neg_at_ceiling`, `dHobs_dt_nonneg_at_boundary`, `dHobs_dt_neg_at_ceiling`, `dIdot_dt_pos_at_boundary`, `dIdot_dt_nonpos_at_ceiling`), the auxiliary bound `dHobs_dt_le_M_H`, and the unified 6-face certificate `compact_box_nagumo_certificate` using explicit monotonicity lemmas (`mul_le_mul_of_nonneg_left`, `mul_le_mul_of_nonneg_right`, `mul_assoc`, `mul_div_cancel₀`, and `linarith`) with zero `sorry` axioms and zero `nlinarith` heuristics.

## Six-Layer Mechanical & VRK v0.3.1 Verification Chain

| Layer | Tool / Module | VRK Claim Class | Verified Claim & Quantitative Bound | Manuscript Scope |
| :--- | :--- | :--- | :--- | :--- |
| **1. Formal Kernel** | Lean 4 Lake (`BoundaryVerification.lean`) | `ANALYTIC_THEOREM` | All 6 face/ceiling conditions of $\mathcal{B}(e)$, `dHobs_dt_le_M_H`, and `compact_box_nagumo_certificate` (`0 sorry`, `0 nlinarith`, `leanprover/lean4:v4.36.0-rc1`, Mathlib `10156080d0e7`) | Theorem 3 (Global Containment) |
| **2. Symbolic Algebra** | `SymPy` (`verification_patch_v1_5.py`) | `ANALYTIC_THEOREM` | Exact equilibrium ($f_1=f_2=f_3=0$), $\partial_{\dot{I}}[e\tanh(\dot{I}/\epsilon_I)\dot{H}_{\text{obs}}]_* = 0$, and zero symbolic residual for $J_{\text{v1.5}}, B_{\text{v1.5}}, C_{1,\text{v1.5}}=0, C_{2,\text{v1.5}}, C_{3,\text{v1.5}}$ | Proposition 4(1)–(2) (Exactness & Tensors) |
| **3. 60-Digit Spectral** | `mpmath` 60-digit (`verification_patch_v1_5.py`) | `REPRODUCED_RESULT` | $e_c = 135/26$, $\omega_c = \sqrt{2/13}$, and $l_{1,\text{v1.4}}$ verified against 50-digit reference ($|\Delta| = 9.38 \times 10^{-52}$) | Section 6 / Table 1 (v1.4 Baseline) |
| **4. 750/1450-Digit Sweep** | `mpmath` 750/1450-digit (`verification_patch_v1_5.py`) | `REPRODUCED_RESULT` | Two-gate scales at $\epsilon = 0.01$ and 5-point exponential convergence sweep across $\epsilon \in [0.005, 0.10]$ cross-checked against asymptotic $2e^{-2\dot{I}^*/\epsilon_I}$ | Proposition 4(3) / Tables 1–2 |
| **5. Return Map & Liouville/Floquet** | `SciPy` `LSODA` & `DOP853` (`verification_patch_v1_5.py`) | `REPRODUCED_RESULT` | 6-face grid check, post-Hopf confinement ($e/e_c \in [0.9, 2.0]$), `LSODA`/`DOP853` replication ($\|\Delta y\|_2 < 10^{-6}$), 3-IC Poincare convergence ($\max\|\Delta y_{\text{IC}}\|_2 < 10^{-6}$), period $T = 18.957047\text{ s}$ (spread $< 10^{-6}\text{ s}$), Liouville integral $\int_0^T \operatorname{div} F\,dt = -10405.41$ ($\det(DP) \approx 10^{-4519} \ll 1$), and $\rho_{\text{FD}}(DP) < 10^{-8}$ at $\text{rtol}=10^{-12}, \Delta h = 10^{-2}$ | Section 6 / Table 3 (Attracting Orbit) |
| **6. VRK v0.3.1 Schema & Manifest Gate** | `verification_patch_v1_5.py` ([10.5281/zenodo.23018459](https://doi.org/10.5281/zenodo.23018459)) | `SCHEMA_AND_MANIFEST_VALIDATED` | Validates 4 separated `intentseal-vrk-claim-v2` claims (`ANALYTIC_THEOREM` x2, `REPRODUCED_RESULT` x2) and on-disk file/anchor presence, rejects illegal `REPRODUCED_RESULT -> ANALYTIC_THEOREM` promotion, and binds `BoundaryVerification.lean` SHA-256 into deterministic certificate digest `5eb316f25edef8e711db7ddec88224172a9cadd8cf7d332457dfa596f4368117` | Section 1 & Section 6 (VRK Provenance) |

## Bundle Inventory & Reproducibility

| File | Description |
| :--- | :--- |
| `Physics_v1_5_Appendix_A.pdf` | Compiled 6-page publication-ready PDF of Appendix A v1.5 |
| `appendix_a_v1_5.tex` | Self-contained LaTeX source manuscript (compiles cleanly with `lualatex` or `pdflatex`) |
| `BoundaryVerification.lean` | Canonical Lean 4 Lake module covering all 6 faces of the compact box $\mathcal{B}(e)$ (`0 sorry`, `0 nlinarith`) |
| `lakefile.lean` | Lean 4 Lake build configuration defining package `boundaryVerification` and library target `BoundaryVerification` |
| `lake-manifest.json` | Deterministic Lake dependency lockfile pinning Mathlib (`10156080d0e7997b71f3ef86bd6f0211b42ab90d`) |
| `lean-toolchain` | Lean 4 toolchain pin (`leanprover/lean4:v4.36.0-rc1`) |
| `verification_patch_v1_5.py` | 60/750/1450-digit `mpmath`, `SymPy` tensor audit, $\epsilon$-scaling sweep, `LSODA`/`DOP853` Poincare, Liouville/Floquet & VRK v0.3.1 gate |
| `launch_sandbox.py` | Dependency-clean local web dashboard (`http://localhost:8080/`) visualizing post-Hopf confinement |
| `verify_ci.yml` | GitHub Actions CI workflow (`.github/workflows/verify.yml`) running `lake build` and `verification_patch_v1_5.py` |
| `README.md` | Release overview, 6-layer VRK verification ledger, `lake build` instructions, and SHA-256 checksum manifest |

### Quick Verification Commands

```bash
# 1. Verify the Lean 4 6-face compact-box theorems via Lake (requires elan / Lean 4 v4.36.0-rc1):
lake exe cache get
lake build

# 2. Run the 60/750/1450-digit spectral, SymPy tensor, eps-sweep, 6-face Nagumo, LSODA/DOP853 Poincare, Liouville/Floquet & VRK v0.3.1 gate:
python3 verification_patch_v1_5.py

# 3. Launch the interactive local phase-space web dashboard:
python3 launch_sandbox.py
```

## SHA-256 Checksum Manifest

| File | SHA-256 |
| :--- | :--- |
| `Physics_v1_5_Appendix_A.pdf` | `5050c88bb3500864bf8043b6fd75dd1307092c732c065002585bfb529aa9d43d` |
| `appendix_a_v1_5.tex` | `e722114b7dd61b221da5c0efda9cacabd75fbe7c57c074048845ece4cd8c82c7` |
| `BoundaryVerification.lean` | `49229b6163b5a3a77dc83779a7dc5350502ff2b3d6a7f2de4d39996f4460e417` |
| `lakefile.lean` | `d8fa0f64b9a781c9e6b811a6d5f0ba872d9f6cfba573c43238b54b45f3cfce8c` |
| `lake-manifest.json` | `54ca7b4da4159237d9913c799616276a775c8ee97a4aa5b1edfc67bb923739b7` |
| `lean-toolchain` | `964acf49a540b2fbb4d25edc186eb68236afd8020473dfad7ccb08dc6ffa1d66` |
| `verification_patch_v1_5.py` | `af0cff7250410ec9c869c71c751fd32134dcc4a12f5a021bf680c3f84eed0e5e` |
| `launch_sandbox.py` | `ab044a634a20805a6b5bd97b15f32fde7dfac84d100c38623de20f02cd908f07` |
| `verify_ci.yml` | `b1137073642d9c292797fe3daf13e0b3568c2eb3aa5a27c6a3c3fe22e59c53b2` |
