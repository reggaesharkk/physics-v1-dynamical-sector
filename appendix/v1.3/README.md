# Appendix A v1.3 — Frozen Nonlinear-Dynamics Release

Author: Prince Upadhyay, Independent Research  
Freeze date: 2026-09-21

This release is additive to frozen Physics v1.0 and Appendix A v1.1. It does not modify the parent model or the Gate 0 conclusion.

## Frozen numerical result

Using F(X)=AX+1/2 B(X,X), the audit slice reproduces e_c=135/26, omega_c=sqrt(2/13), and l1=+0.519589117351219.

The corrected seeded sweep evaluated 122,378 valid Hopf points from 200,000 draws: 122,378 l1>0; 0 l1<0; 0 l1=0.

The adversarial reduced-coordinate stress test sampled 50,000 points with each positive coordinate spanning 1e-8 to 1e8. Double precision nominated 327 apparent negative candidates; 326 were successfully rechecked at high precision and all were positive. One pathological candidate could not be high-precision evaluated and remains open.

## Claim boundary

This is broad reproducible numerical evidence, not a universal algebraic theorem. Universal l1 positivity, the one unrecomputed pathological candidate, complete global basin-boundary topology, positivity-preserving physical completion, and microscopic derivation remain open.

Frozen package SHA-256: 58cd5da63ebbef4bce18925df06bd9d4423f5175b49b7b05f171d02966a0257a
