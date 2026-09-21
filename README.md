# Physics v1.0 — Dynamical Sector

Reproducibility repository for **Physics v1.0** and the Appendix A dynamical-sector lineage, by **Prince Upadhyay (Independent Research)**.

## Archival sources of record

**Physics v1.0:** *An Information-Theoretic Framework for Emergent Spacetime Dynamics, Horizon Thermodynamics, and Testable Cosmological Signatures*  
DOI: https://doi.org/10.17605/OSF.IO/TSW4B

**Appendix A v1.4 — frozen analytic theorem record**  
OSF registration: U7M6H  
DOI: https://doi.org/10.17605/OSF.IO/U7M6H

The OSF registrations/releases are the archival sources of record. This GitHub repository is the version-controlled reproducibility companion.

## Appendix A lineage

### v1.1 — linear analysis

Appendix A v1.1 derived the equilibrium, admissibility conditions, Jacobian and characteristic polynomial, the unique linear Hopf boundary, critical feedback threshold/frequency, and inverse erasure scaling for the frozen Physics v1.0 phenomenological ODE.

**Historical correction:** v1.1 described numerical behavior above threshold as *consistent with a supercritical Hopf bifurcation* because the Hopf normal form had not yet been computed. That wording is superseded by the later nonlinear audit and exact v1.4 theorem. The frozen v1.1 artifact is preserved as historical provenance rather than silently rewritten.

### v1.3 — numerical nonlinear audit

The corrected deterministic bounded sweep (seed 20260921) sampled 200,000 parameter combinations and produced **122,378 valid Hopf points**. Every valid point had positive first Lyapunov coefficient in the stated convention.

Adversarial wide-range testing exposed floating-point conditioning issues; high-precision rechecks motivated replacing numerical sign evidence with an exact symbolic proof.

### v1.4 — exact positivity theorem

For the covered strictly-positive interior reduced family, on the exact e-driven Hopf surface,

    e_c = (alpha+g)(alpha+mu)(g+mu) / [beta delta (alpha+mu+g)]
    omega_c^2 = alpha mu g / (alpha+mu+g)

with convention

    l1 = Re(G21)/(2 omega),    <p,q> = 1,

the symbolic calculation reduces

    Re(G21) = N/D

to an exact positivity certificate. The expanded numerator has **93 monomials** and the denominator **28 monomials**; every exact coefficient is strictly positive. Therefore **l1 > 0** throughout the theorem's positive domain.

The eigenvalue pair crosses with positive transversality. Hence every covered interior e-driven Hopf bifurcation is **subcritical** in the stated convention. Locally, the small unstable periodic orbit lies on the **e < e_c** side, while the equilibrium loses stability as e increases through e_c.

The r = 0 / delta = 0 boundary is excluded: there the e-driven Hopf mechanism covered by this theorem is absent.

### v1.4.1 — documentation and verification-tooling patch

v1.4.1 corrects documentation/tooling issues without changing the theorem, exact certificate, or numerical result. The coefficient-only verifier proves positivity of the listed certificate; the optional high-precision identity mode separately checks the identity between N/D and the eigenvector-based Re(G21) calculation.

## What happened to the v1.1 “supercritical” numerical behavior?

The v1.4 theorem reverses the old local interpretation: the covered small Hopf cycle is unstable, not stable. Therefore any stable oscillation seen above threshold in the historical v1.1 benchmark cannot be the small local Hopf cycle covered by the theorem. It requires a different explanation — for example a larger-amplitude attractor outside the local normal-form neighborhood, a separate global bifurcation, or dynamics associated with leaving the intended physical domain. No specific global mechanism is claimed here without a separate proof.

## Scope firewall

This repository does **not** claim:

- a microscopic derivation of the phenomenological ODE system;
- that the ODE is a fundamental law of nature;
- a derived physical identity between model-information and irreversible-erasure rates;
- closure of the observer-entropy to horizon-entropy bridge;
- proof that consciousness creates spacetime;
- a global basin theorem from the local Hopf result.

**Gate 0 remains UNRESOLVED IN GENERALITY.**  
The v1.4 theorem strengthens the nonlinear mathematics of the phenomenological model; it does not close Gate 0.

## Repository navigation

- `appendix/v1.4/` — frozen theorem release documentation and provenance
- `appendix/v1.4.1/` — author errata / verification-tooling patch
- `analysis/` — dynamical-sector analysis code
- `manifests/` — provenance records

## Citation

For the analytic Hopf theorem, cite **Appendix A v1.4, DOI 10.17605/OSF.IO/U7M6H**.  
For the parent phenomenological framework, cite **Physics v1.0, DOI 10.17605/OSF.IO/TSW4B**.

## License

Archived research materials on OSF are released under CC BY 4.0. Repository source-code licensing should be interpreted separately unless an explicit software license is attached.
