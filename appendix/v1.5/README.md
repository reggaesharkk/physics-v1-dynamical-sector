# Physics v1.0 — Dynamical Sector: Appendix A v1.5 (Upgraded Lake-Verified & VRK v0.3.1 Release)

*(Additive to frozen Physics v1.0 [DOI: 10.17605/OSF.IO/N3DQU], Appendix A v1.4 [DOI: 10.17605/OSF.IO/U7M6H](https://doi.org/10.17605/OSF.IO/U7M6H), and Appendix A v1.4.1 [DOI: 10.17605/OSF.IO/S7WHX](https://doi.org/10.17605/OSF.IO/S7WHX); verified under IntentSeal VRK v0.3.1 [DOI: 10.5281/zenodo.23018459](https://doi.org/10.5281/zenodo.23018459), Prototype Lineage v0.1.1-v0.5.0 [DOI: 10.5281/zenodo.23016445](https://doi.org/10.5281/zenodo.23016445), and STRENGTH-INTENT-NS-LEAN [DOI: 10.5281/zenodo.23474505](https://doi.org/10.5281/zenodo.23474505)).*

* **Zenodo Archive DOIs:** <https://doi.org/10.5281/zenodo.23497142> | <https://doi.org/10.5281/zenodo.23501526>
* **VRK & Ecosystem Lineage DOIs:** <https://doi.org/10.5281/zenodo.23018459> | <https://doi.org/10.5281/zenodo.23016445> | <https://doi.org/10.5281/zenodo.23474505>
* **Author:** Prince Upadhyay (`starxshark@gmail.com`, ORCID: `0009-0002-1170-4487`)
* **Release Date:** October 21, 2026

> **Scope correction:** See [SCOPE_CORRECTION.md](SCOPE_CORRECTION.md). Lean checks the six algebraic boundary inequalities; the manuscript applies Nagumo’s theorem analytically, and that theorem and the ODE-flow conclusion are not formalized in Lean. The transverse Floquet outputs are unresolved float64 diagnostics, not stability bounds.

## Summary of Upgraded v1.5 Contributions & VRK Epistemic Classification

1. **Conditional Holographic Closure of Gate 0 (Proposition 1 — `CONDITIONAL_FRONTIER` / `OPEN`):** Formulates an explicit covariant dictionary linking the fine-grained von Neumann entropy ceiling $H_{\max}$ of a causal-diamond observer subsystem $\mathcal{D}(\mathcal{A})$ to the area of its Hubeny-Rangamani-Takayanagi (HRT) extremal surface $\Sigma_{\text{HRT}}$, $H_{\max} = \operatorname{Area}(\Sigma_{\text{HRT}})/(4\ell_P^2 \ln 2)$, while maintaining strict epistemic separation from non-geometric tensor factorizations (where Gate 0 remains `OPEN`).
2. **Positivity-Preserving Soft-Wall Dynamical Completion & Gain-Dependent Trapping Box Theorem (Theorem 3 — `ANALYTIC_THEOREM`):**
   * Gates the irreversible-erasure sink with $\Psi_{\epsilon_H}(H_{\text{obs}}) = \tanh(H_{\text{obs}}/\epsilon_H)$ and gates the derivative-feedback channel with $\Phi_{\epsilon_I}(\dot{I}) = \tanh(\dot{I}/\epsilon_I)$.
   * The manuscript's analytic proof applies Nagumo's subtangentiality theorem to establish forward invariance of the positive orthant $\mathbb{R}^3_+$ and the gain-dependent compact box $\mathcal{B}(e) = [0,\gamma_{\max}]\times[0,H_{\max}]\times[0,\dot{I}_{\max}(e)]$, where $\dot{I}_{\max}(e) = (e M_H + f\mathcal{P}_{\text{input}})/g$ (`ANALYTIC_THEOREM`). The Lean module checks the six boundary inequalities used as premises; it does not formalize Nagumo's theorem or the ODE-flow conclusion.
   * Demonstrates numerically (`REPRODUCED_RESULT`) via multi-initial-condition Poincaré return-map integration replicated across independent `LSODA` (Adams/BDF) and `DOP853` (8th-order Runge-Kutta) solvers, the Liouville orbital divergence integral ($\int_0^T \operatorname{div} F(y(t))\,dt = -10405.41 \implies \det(DP) \approx 10^{-4519} \ll 1$), numerical float64 integration of the variational equation. Its raw transverse eigenvalue near machine precision ($\approx 2.66 \times 10^{-16}$) is unresolved at the Liouville determinant scale reported above; finite-difference return-map values without certified error enclosures are diagnostics, not upper bounds. The tested trajectories approached a periodic relaxation oscillation, an empirical observation for those runs; no transverse Floquet stability bound is established.
3. **Exact Interior Equilibrium, Uniqueness, SymPy Tensor Audit & $\epsilon$-Scaling Bounds (Proposition 4 — `ANALYTIC_THEOREM` + `REPRODUCED_RESULT`):**
   * **Analytic Identity & Uniqueness (`ANALYTIC_THEOREM`):** Because $\left.dH_{\text{obs}}/dt\right|_* = 0$ at any equilibrium, the first derivative of the processing gate vanishes **identically** in the equilibrium Jacobian, leaving $\dot{I}^* = f\mathcal{P}_{\text{input}}/g$ and $\gamma^* = K\gamma_{\max}/(b\gamma_{\max}+K)$ exact, while $H_{\text{obs}}^*$ is the unique root on $(0, H_{\max})$ of $g(H_{\text{obs}}) = c\gamma^*(H_{\max}-H_{\text{obs}}) - \dot{I}_{\text{erase}}\tanh(H_{\text{obs}}/\epsilon_H) = 0$ ($g(0) > 0$, $g(H_{\max}) < 0$, $g' < 0$). Independent `SymPy` symbolic differentiation verifies $f_1=f_2=f_3=0$ at steady state, strict monotonicity of $g$, and zero symbolic residual across all 1st-, 2nd-, and 3rd-order Taylor tensors ($J_{\text{v1.5}}, B_{\text{v1.5}}, C_{1,\text{v1.5}}=0, C_{2,\text{v1.5}}, C_{3,\text{v1.5}}$).
   * **Multiprecision Scaling Sweep (`REPRODUCED_RESULT`):** Across $\epsilon_H = \epsilon_I = \epsilon \in \{0.10, 0.05, 0.02, 0.01, 0.005\}$ on the v1.3/v1.4 audit slice, $\|J_{\text{v1.5}} - J_{\text{v1.4}}\|_F$ and $|\Delta l_1|$ decay exponentially from $2.21 \times 10^{-8}$ and $1.75 \times 10^{-6}$ at $\epsilon = 0.10$, to $1.48 \times 10^{-86}$ and $1.11 \times 10^{-82}$ at $\epsilon = 0.01$ (where $1 - \tanh(\dot{I}^*/\epsilon_I) = 2.77 \times 10^{-87}$, agreeing with the asymptotic formula $2e^{-2\dot{I}^*/\epsilon_I}$ to relative error $< 10^{-86}$, and $\operatorname{sech}^2(H_{\text{obs}}^*/\epsilon_H) = 5.38 \times 10^{-695}$), and $2.05 \times 10^{-173}$ and $6.11 \times 10^{-169}$ at $\epsilon = 0.005$.
4. **Six-Face Machine-Checked Lean 4 Boundary Package (`BoundaryVerification.lean`, `lakefile.lean`, `lake-manifest.json`, `lean-toolchain`):**
   * Machine-checks the six boundary inequalities and auxiliary compact-box bounds over Mathlib’s `Real` ($\mathbb{R}$), including `M_H_nonneg`, `I_dot_max_pos`, `dHobs_dt_le_M_H`, and `compact_box_nagumo_certificate` (zero `sorry`, zero `nlinarith`). These are the premises for the manuscript’s analytic Nagumo argument; the theorem application and ODE-flow conclusion are not formalized in Lean.

## Six-Layer Mechanical & VRK v0.3.1 Verification Chain

| Layer | Tool / Module | VRK Claim Class | Verified Claim & Quantitative Bound | Manuscript Scope |
| :--- | :--- | :--- | :--- | :--- |
| **1. Formal Kernel** | Lean 4 Lake (`BoundaryVerification.lean`) | `ANALYTIC_THEOREM` support | Checks all 6 face inequalities and auxiliary bounds (`0 sorry`, `0 nlinarith`, pinned Lean/Mathlib). It does not formalize Nagumo's theorem or the ODE-flow invariance conclusion; that implication is proved analytically in the manuscript. | Theorem 3 (Global Containment) |
| **2. Symbolic Algebra** | `SymPy` (`verification_patch_v1_5.py`) | `ANALYTIC_THEOREM` | Exact equilibrium ($f_1=f_2=f_3=0$), uniqueness of $H_{\text{obs}}^* \in (0, H_{\max})$, $\partial_{\dot{I}}[e\tanh(\dot{I}/\epsilon_I)\dot{H}_{\text{obs}}]_* = 0$, and zero symbolic residual for $J_{\text{v1.5}}, B_{\text{v1.5}}, C_{1,\text{v1.5}}=0, C_{2,\text{v1.5}}, C_{3,\text{v1.5}}$ | Proposition 4(1)–(2) (Exactness & Tensors) |
| **3. 60-Digit Spectral** | `mpmath` 60-digit (`verification_patch_v1_5.py`) | `REPRODUCED_RESULT` | $e_c = 135/26$, $\omega_c = \sqrt{2/13}$, and $l_{1,\text{v1.4}}$ verified against 50-digit reference ($|\Delta| = 9.38 \times 10^{-52}$) | Section 6 / Table 1 (v1.4 Baseline) |
| **4. 750/1450-Digit Sweep** | `mpmath` 750/1450-digit (`verification_patch_v1_5.py`) | `REPRODUCED_RESULT` | Two-gate scales at $\epsilon = 0.01$ and 5-point exponential convergence sweep across $\epsilon \in [0.005, 0.10]$ cross-checked against asymptotic $2e^{-2\dot{I}^*/\epsilon_I}$ | Proposition 4(3) / Tables 1–2 |
| **5. Return Map, Liouville & Variational Floquet** | `SciPy` `LSODA` & `DOP853` (`verification_patch_v1_5.py`) | `REPRODUCED_RESULT` | 6-face grid check, post-Hopf confinement ($e/e_c \in [0.9, 2.0]$), `LSODA`/`DOP853` replication ($\|\Delta y\|_2 < 10^{-6}$), 3-IC Poincaré convergence ($\max\|\Delta y_{\text{IC}}\|_2 < 10^{-6}$), period $T = 18.957047\text{ s}$ (spread $< 10^{-6}\text{ s}$), Liouville integral $\int_0^T \operatorname{div} F\,dt = -10405.41$ ($\det(DP) \approx 10^{-4519} \ll 1$), float64 variational integration finds the trivial multiplier near 1; transverse multipliers are unresolved (raw second eigenvalue $\approx 2.66 \times 10^{-16}$ at machine precision). Finite-difference values have no certified error enclosure and are not bounds. Multi-IC convergence is empirical; no transverse stability claim is made | Section 6 / Table 3 (Numerical Orbit Observation) |
| **6. VRK v0.3.1 Schema & Manifest Gate** | `verification_patch_v1_5.py` ([10.5281/zenodo.23018459](https://doi.org/10.5281/zenodo.23018459)) | `SCHEMA_AND_MANIFEST_VALIDATED` | Validates 4 separated `intentseal-vrk-claim-v2` claims (`ANALYTIC_THEOREM` x2, `REPRODUCED_RESULT` x2) and on-disk file/anchor presence, rejects illegal `REPRODUCED_RESULT -> ANALYTIC_THEOREM` promotion, and binds `BoundaryVerification.lean` SHA-256 into deterministic certificate digest `25db5306e05cf90e0959f08553d8aa3db6f15996ce225abad75a1bf95a0f48d9` | Section 1 & Section 6 (VRK Provenance) |

## Bundle Inventory & Reproducibility

| File | Description |
| :--- | :--- |
| `Physics_v1_5_Appendix_A.pdf` | Archived 7-page release PDF; its scope is corrected by `SCOPE_CORRECTION.md` and the updated LaTeX source |
| `SCOPE_CORRECTION.md` | Corrected scope for the Lean boundary certificate and unresolved float64 Floquet diagnostics |
| `appendix_a_v1_5.tex` | Updated LaTeX source manuscript corresponding to the scope correction |
| `BoundaryVerification.lean` | Canonical Lean 4 Lake module covering all 6 faces of the compact box $\mathcal{B}(e)$ (`0 sorry`, `0 nlinarith`) |
| `lakefile.lean` | Lean 4 Lake build configuration defining package `boundaryVerification` and library target `BoundaryVerification` |
| `lake-manifest.json` | Deterministic Lake dependency lockfile pinning Mathlib (`10156080d0e7997b71f3ef86bd6f0211b42ab90d`) |
| `lean-toolchain` | Lean 4 toolchain pin (`leanprover/lean4:v4.36.0-rc1`) |
| `verification_patch_v1_5.py` | 60/750/1450-digit `mpmath`, `SymPy` tensor audit, $\epsilon$-scaling sweep, `LSODA`/`DOP853` Poincaré, Liouville and unresolved float64 Floquet diagnostics, VRK v0.3.1 gate |
| `launch_sandbox.py` | Dependency-clean local web dashboard (`http://localhost:8080/`) visualizing post-Hopf confinement |
| `requirements.txt` | Pinned Python verification dependencies |
| `README.md` | Release overview, 6-layer VRK verification ledger, `lake build` instructions, and SHA-256 checksum manifest |

*(CI workflow is located at `.github/workflows/verify.yml` in the repository root.)*

### Quick Verification Commands

```bash
# 1. Verify the Lean 4 6-face compact-box theorems via Lake (requires elan / Lean 4 v4.36.0-rc1):
lake exe cache get
lake build

# 2. Run the 60/750/1450-digit spectral, SymPy tensor, eps-sweep, 6-face boundary checks, LSODA/DOP853 Poincare, Liouville/Floquet diagnostics & VRK v0.3.1 gate:
python3 verification_patch_v1_5.py

# 3. Launch the interactive local phase-space web dashboard:
python3 launch_sandbox.py
```

## SHA-256 Checksum Manifest

| File | SHA-256 |
| :--- | :--- |
| `Physics_v1_5_Appendix_A.pdf` | `1fe5e9e21e753114677a7b5be109b18e8830488b77d9eeffa72de4d8529e509b` |
| `SCOPE_CORRECTION.md` | `10984572df46c14ecec3fc9bada0d3bee418088b0763c195e4d82cf79d711a19` |
| `appendix_a_v1_5.tex` | `ec1421c8dc2944389de91cb395771a44952e193c68a644a04e4c5e340a6a0f0f` |
| `BoundaryVerification.lean` | `eb491d262a9c99e4385bcec0b7b3e6f1636a8a09f1540df3223c557efa58a6f9` |
| `lakefile.lean` | `d8fa0f64b9a781c9e6b811a6d5f0ba872d9f6cfba573c43238b54b45f3cfce8c` |
| `lake-manifest.json` | `54ca7b4da4159237d9913c799616276a775c8ee97a4aa5b1edfc67bb923739b7` |
| `lean-toolchain` | `964acf49a540b2fbb4d25edc186eb68236afd8020473dfad7ccb08dc6ffa1d66` |
| `verification_patch_v1_5.py` | `3e22649252e8d6db702ddc67c7656f41c0ad198bab3b3534e42477da61caf95c` |
| `launch_sandbox.py` | `ab044a634a20805a6b5bd97b15f32fde7dfac84d100c38623de20f02cd908f07` |
| `requirements.txt` | `9af84be3bb66b3ad7cfface4fbc876788d44532e7e75713ba4cb1d3fc5483f5a` |
