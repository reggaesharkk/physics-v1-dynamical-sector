# Physics v1.0 — Dynamical Sector

Reproducibility repository for **Physics v1.0** and **Appendix A v1.1**, by Prince Upadhyay (Independent Research).

## Archival source of record

**Physics v1.0:** *An Information-Theoretic Framework for Emergent Spacetime Dynamics, Horizon Thermodynamics, and Testable Cosmological Signatures*  
DOI: https://doi.org/10.17605/OSF.IO/TSW4B

The OSF project/registration is the archival source of record. This GitHub repository is the version-controlled reproducibility companion for the dynamical-sector analysis.

## Appendix A v1.1

Appendix A analyzes equations (9)–(11) of the frozen Physics v1.0 phenomenological dynamical sector. It is additive: it does **not** modify the frozen Physics v1.0 equations and introduces **no new postulate**.

Within the frozen ansatz, the appendix derives:

- the unique closed-form equilibrium;
- independence of the steady-state model-information rate from the entropy sector;
- the irreversible-erasure-controlled equilibrium gap;
- the physical-admissibility bound;
- the exact Jacobian and characteristic polynomial;
- the unique linear Hopf stability boundary;
- the exact critical feedback threshold and crossing frequency;
- the inverse scaling of the critical feedback gain with the irreversible-erasure rate;
- numerical checks agreeing with the analytic threshold and crossing frequency to machine precision.

The numerical integrations also show that the frozen ansatz is not globally positivity-preserving for the benchmark parameter set. The Hopf normal form has not been computed, so numerical behavior above threshold is described only as consistent with a supercritical Hopf bifurcation, not as an analytic proof of criticality.

## Scope firewall

This repository does **not** claim:

- a microscopic derivation of the phenomenological ODE system;
- a derived physical relation between model-information and irreversible-erasure rates;
- a geometric, causal-horizon, or holographic interpretation of H_max;
- progress on the observer-entropy to horizon-entropy bridge;
- a new cosmological prediction from Appendix A;
- a constraint on the gravitational-wave template of Physics v1.0.

**Gate 0 remains unchanged: UNRESOLVED IN GENERALITY.**

## Reproducibility

Run:

```bash
python analysis/physics_v1_0_ode_analysis.py
```

Reference environment recorded in the Appendix A manifest:

- NumPy 2.4.4
- SciPy 1.17.1
- pdfTeX 3.141592653-2.6-1.40.25 (TeX Live 2023)

The exact release artifacts and SHA-256 provenance records are preserved on OSF. The manifest included here is the frozen Appendix A build manifest and therefore retains its original pre-deposit status string.

## Citation

Please cite the archival Physics v1.0 DOI above. A machine-readable `CITATION.cff` is included in this repository.

## License

The archived research materials on OSF are released under CC BY 4.0. Repository licensing for source code should be interpreted separately unless an explicit software license is added here.
