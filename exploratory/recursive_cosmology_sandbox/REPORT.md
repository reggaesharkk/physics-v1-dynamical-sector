# Recursive cosmology toy sandbox: equilibrium and closure audit

This is a separate, exploratory check of the three-variable sandbox supplied
in conversation. It is **not** the Physics v1.0 Appendix A ODE, and it changes
none of the frozen Appendix A theorem, its proof, or its DOI records.

For strictly positive `a,b,c,d,e,f,g,T`, the unclipped ODE is

\[
 \dot R=aT\Gamma(1-R)-bR,\quad
 \dot\Psi=cR(1-\Psi)-d\Psi,\quad
 \dot\Gamma=e\Psi+fT-g\Gamma.
\]

The domain `0<=R,Psi<=1`, `Gamma>=0` is forward invariant: each boundary
vector field points inward or tangentially. Gamma is bounded above by a
solution of `Gamma' <= e+fT-g Gamma`. Clipping `R,Psi` in an ODE solver is
unnecessary for an exact solution starting in this domain; it changes the
vector field outside it.

## Equilibrium and local stability

At equilibrium,

\[
 \Psi(R)=\frac{cR}{cR+d},\qquad
 \Gamma(R)=\frac{e\Psi(R)+fT}{g},\qquad
 F(R)=aT\Gamma(R)(1-R)-bR=0.
\]

On `[0,1]`, `Gamma(R)` is increasing and concave. `F(0)>0`, `F(1)<0`, and
`F''(R)=aT[(1-R)Gamma''(R)-2Gamma'(R)]<0`. It follows that `F` has exactly
one zero in `(0,1)`: after its first crossing from positive to negative,
strict concavity prevents a return. This proves a unique physical equilibrium
under the stated positive-parameter conditions.

Its Jacobian has diagonal entries `-x,-y,-g` with `x=aT Gamma*+b`,
`y=cR*+d`, and one positive three-edge loop of strength
`L=aT(1-R*)c(1-Psi*)e`. Concavity gives `F'(R*)<0`, equivalently
`L < x y g`. Hence the characteristic equation

\[
 (\lambda+x)(\lambda+y)(\lambda+g)-L=0
\]

has all roots in the left half-plane: for `Re(lambda)>=0`, the magnitude of
the product is at least `xyg>L`. The equilibrium is locally asymptotically
stable. This note does **not** assert global attraction for every initial
state or every altered parameter convention.

The accompanying script computes the equilibrium by bisection and checks the
Jacobian numerically. At baseline `(a,b,c,d,e,f,g,T)=(1.2,.35,1,.30,.55,.25,.45,1)`,
it obtains approximately `(R*,Psi*,Gamma*)=(.83293242,.73520045,1.45413388)`.

## Normalized proximity is not a fixed-point test

The proposed operator samples `N` with Gaussian entries and sets
`C(U)=qU+(1-q)N`, `q=R Psi`. At the positive equilibrium, `q<1` because
`b,d>0` imply `R*,Psi*<1`. Each fresh noise sample makes `C` a **random
operator**; a pathwise fixed point needs a specified noise realization and
coupling across iterations. With fixed `N`, its sole fixed point is `U=N`.
With fresh continuous noise, an exact `C(U)=U` for a fixed prescribed `U`
has probability zero at each evaluation.

More decisively, the reported proximity normalizes both nonzero matrices:

\[
 \Pi(U,C)=1-\min\left(1,\frac{\|\widehat U-\widehat C\|_F}{\sqrt2}\right),
 \qquad \widehat U=U/\|U\|_F,\quad\widehat C=C/\|C\|_F.
\]

For zero noise and any `0<q<1`, `C(U)=qU`, so **Pi=1 while C(U) differs
from U**. The normalized score identifies a positive ray, not a universe
state. Its value under random noise depends on the matrix, random seed,
dimension, and noise scale; it cannot be inferred solely from `(R*,Psi*)`.

The scalar `Gamma` is also not normalized to `[0,1]` in this model; its
baseline equilibrium exceeds one. None of these toy state variables has an
operational identification with LRSC rank, Navier–Stokes cutoff, or an AI
benchmark outcome. Such connections require an independently specified
measurement map and held-out test.

## Reproduce

From this repository root, with NumPy installed:

```bash
python exploratory/recursive_cosmology_sandbox/closure_audit.py
```

`output.txt` records this run. The exact arguments above carry the analytic
claims; decimal output is a diagnostic, not a formal numerical certificate.
