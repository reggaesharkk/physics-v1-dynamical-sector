# Frozen v1.3 adversarial-test metadata.
SEED=20260921
N=50000
LO,HI=1e-8,1e8
# Reduced positive variables: alpha, mu, g, beta, delta, K, C.
# Exact Hopf surface:
# e_c=((alpha+g)*(alpha+mu)*(g+mu))/(beta*delta*(alpha+mu+g))
# omega^2=alpha*mu*g/(alpha+mu+g)
# Double precision nominated 327 l1<0 candidates.
# 326 were successfully recomputed at high precision; all 326 had l1>0.
# One pathological high-precision evaluation failure remains open.
