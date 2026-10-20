import Mathlib.Analysis.SpecialFunctions.Trigonometric.Basic
import Mathlib.Topology.MetricSpace.Basic

/-- State space coordinates used in Appendix A v1.5. -/
structure CosmologicalState where
  gamma : ℝ        -- Reconstruction Capacity (\gamma)
  H_obs : ℝ        -- Observer Entropy (H_obs)
  I_dot : ℝ        -- Information Accumulation Rate (\dot{I})

/-- Individual component tracking for dgamma/dt derivative. -/
def dgamma_dt (a b E_avail : ℝ) (s : CosmologicalState) : ℝ :=
  a * s.I_dot * E_avail - b * s.gamma

/-- Individual component tracking for dHobs/dt derivative. -/
def dHobs_dt (c H_max I_erase epsH : ℝ) (s : CosmologicalState) : ℝ :=
  c * s.gamma * (H_max - s.H_obs) - I_erase * (1/2) * (1 + Real.tanh (s.H_obs / epsH))

/-- Individual component tracking for dIdot/dt derivative. -/
def dIdot_dt (e f g c H_max I_erase epsH epsI : ℝ) (s : CosmologicalState) : ℝ :=
  e * (dHobs_dt c H_max I_erase epsH s) + f - g * s.I_dot * Real.tanh (s.I_dot / epsI)

/-- The unified vector field function F mapping coordinates simultaneously. -/
def F (a b c e f g H_max E_avail I_erase epsH epsI : ℝ) (s : CosmologicalState) : CosmologicalState :=
{ gamma := dgamma_dt a b E_avail s
, H_obs := dHobs_dt c H_max I_erase epsH s
, I_dot := dIdot_dt e f g c H_max I_erase epsH epsI s }