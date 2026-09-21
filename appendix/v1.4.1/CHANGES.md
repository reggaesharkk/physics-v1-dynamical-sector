# Appendix A v1.4 -> v1.4.1

Author: Prince Upadhyay, Independent Research  
Date: 21 September 2026  
Classification: documentation/tooling errata patch

No change is made to the theorem, the exact certificate, the symbolic derivation, the parent phenomenological model, or any numerical result.

## Corrections

- Corrected the proof-audit status from the stale candidate wording to a frozen-author errata status.
- Corrected the verifier's default certificate filename.
- Stated the verifier's scope precisely: coefficient positivity proves N/D>0 but does not by itself prove N/D=Re(G21).
- Added an optional independent numerical identity check using 50-digit eigenvector calculations at 25 deterministic random positive parameter points.
- Regenerated the verifier output without the unrelated environment traceback present in the v1.4 artifact.
- Recorded the transversality derivative explicitly.
- Stated the first-Lyapunov convention explicitly: l1=Re(G21)/(2*omega), with <p,q>=1.
- Stated the local bifurcation side explicitly: with positive transversality and l1>0, the Hopf is subcritical and the local unstable periodic orbit lies on the e<e_c side.

## Unchanged certificate

exact_positive_polynomial_certificate_v1_4.json  
SHA-256: 34439e86255d7d9e61c483e3c97044e247d9eae09bc2c00b13791704c8a68667

## Provenance rule

The frozen v1.4 OSF registration U7M6H is not replaced, edited, or rewritten. v1.4.1 is an additive errata/documentation-and-tooling patch preserving the historical v1.4 record.
