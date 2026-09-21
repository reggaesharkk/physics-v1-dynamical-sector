# Appendix A v1.4.1 — Proof Audit and Errata

Author: Prince Upadhyay, Independent Research  
Date: 21 September 2026  
Status: FROZEN AUTHOR ERRATA / DOCUMENTATION-AND-TOOLING PATCH  
Parent release: Appendix A v1.4 — OSF U7M6H — DOI 10.17605/OSF.IO/U7M6H

## Purpose

This v1.4.1 patch corrects documentation and verification-tooling defects in the frozen v1.4 release. It does not change the theorem, the exact coefficient certificate, the symbolic derivation, the parent phenomenological model, or any numerical result. The v1.4 OSF registration remains an immutable historical record.

## Result

Exact symbolic reconstruction gives Re(G21)=N/D after imposing omega^2=alpha*mu*g/(alpha+mu+g). N has 93 monomials and D has 28 monomials, and every exact coefficient in both is strictly positive.

The certificate verifier checks all 121 coefficients. This establishes N/D>0 on the positive orthant but does not, by itself, establish N/D=Re(G21). The optional identity mode separately compares N/D with Re(G21) computed from numerical eigenvectors at 50-digit precision over 25 deterministic random positive parameter points. The recorded worst relative difference is 1.53e-47. The analytic identity itself is supplied by the symbolic derivation.

Transversality follows from the characteristic polynomial
lambda^3+(alpha+mu+g)lambda^2+(alpha*mu+alpha*g+mu*g-beta*delta*e)lambda+alpha*mu*g.
At the Hopf point,
d Re(lambda)/de = beta*delta*(alpha+mu+g)^2/(2*D3) > 0,
where D3 is the positive-coefficient cubic factor appearing in the exact denominator.

## Convention and local bifurcation side

I use l1=Re(G21)/(2*omega), with <p,q>=1. With positive transversality as e increases, l1>0 gives a subcritical Hopf bifurcation: the small-amplitude periodic orbit is unstable and lies locally on the e<e_c side, while the equilibrium loses stability as e crosses e_c upward.

## Theorem scope

For alpha,mu,g,beta,delta,K,C>0 on
e_c=(alpha+g)(alpha+mu)(g+mu)/(beta*delta*(alpha+mu+g)),
omega_c^2=alpha*mu*g/(alpha+mu+g),
the stated first Lyapunov coefficient satisfies l1>0. Together with positive transversality, every covered interior e-driven Hopf bifurcation is subcritical in this convention.

## Important boundary

This is a theorem about the specified phenomenological dynamical family. It is not a microscopic derivation, does not close Gate 0, does not establish a global basin-boundary theorem, and does not by itself establish that nature realizes the model.

## Reproducibility

Unchanged certificate SHA-256: 34439e86255d7d9e61c483e3c97044e247d9eae09bc2c00b13791704c8a68667
