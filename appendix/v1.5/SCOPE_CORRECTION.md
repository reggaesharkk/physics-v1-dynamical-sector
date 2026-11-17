# Appendix A v1.5 scope correction

This note corrects the verification scope described in the original Appendix A v1.5 package.

## Lean boundary certificate

`BoundaryVerification.lean` machine-checks the six algebraic boundary inequalities and auxiliary bounds. The manuscript then applies Nagumo's subtangentiality theorem and standard ODE existence results to obtain forward invariance. That analytic step is not formalized in Lean, so the CI result should be described as a passing boundary certificate rather than a machine-checked ODE-flow theorem.

## Floquet diagnostics

The variational equation is integrated with SciPy in float64. The reported Liouville calculation estimates the return-map determinant near `10^-4519`, far below float64's representable range. The raw transverse eigenvalues near `2.6634e-16` are therefore roundoff-scale outputs, not upper bounds on the true transverse multipliers. The finite-difference estimates (`1.98e-6` and `2.37e-9`) have no certified error enclosure and do not establish contraction.

The tested trajectories from three initial conditions approach a numerically periodic relaxation oscillation, with close results across LSODA and DOP853. This is a reproduced numerical observation for the tested benchmark. It does not establish a transverse stability bound or an analytic limit-cycle theorem.

The repository's PDF remains the archived release binary. The corrected LaTeX source and verifier use the scope stated here; regenerate the PDF before replacing that archived binary.
