<p align="center"><a href="https://github.com/reggaesharkk/Reggae-shark-universe-"><img src="https://raw.githubusercontent.com/reggaesharkk/Reggae-shark-universe-/main/assets/universe_bar.svg" alt="Reggae Shark Universe — public research map" width="100%" /></a></p>

<p align="center"><a href="https://github.com/reggaesharkk/Reggae-shark-universe-">Public research map</a> &nbsp;·&nbsp; <a href="https://github.com/reggaesharkk?tab=repositories">All public repositories</a> &nbsp;·&nbsp; <a href="https://orcid.org/0009-0002-1170-4487">ORCID</a></p>

> I keep each project’s evidence, scope, and open questions alongside the work.

---

# Physics v1.0 — Dynamical Sector
*(For the full document text and archival details, see OSF record DOI 10.17605/OSF.IO/TSW4B and Appendix A v1.4 DOI 10.17605/OSF.IO/U7M6H).*

**Rights boundary — effective 1 October 2026:** New author-owned original material first published here from this date is **All Rights Reserved** by default.

I maintain this repository as the release map for Appendix A. The linked OSF and Zenodo records identify the citable versions; the v1.4 line remains frozen while v1.5 is the active release.

## Appendix A v1.5

| Result | Scope and evidence |
| --- | --- |
| Gate 0 (Proposition 1) | The entropy ceiling is related to extremal-surface area under the holographic dictionary assumed in the manuscript. Gate 0 remains open for non-geometric factorizations. [Read the manuscript](appendix/v1.5/Physics_v1_5_Appendix_A.pdf). |
| Boundary confinement (Theorem 3) | The [Lean certificate](appendix/v1.5/BoundaryVerification.lean) establishes the vector-field inequalities on all six faces of the gain-dependent box. The manuscript uses those inequalities to establish forward invariance. |
| Post-Hopf oscillation | The [Python verification suite](appendix/v1.5/verification_patch_v1_5.py) examines attraction numerically using return maps and Floquet calculations for the reported parameter choices. |

Cite the [archived v1.5 Lean release](https://doi.org/10.5281/zenodo.23501526).

## Reproduce the checks

From the repository root, with Python 3.11 and elan installed:

```bash
cd appendix/v1.5
lake exe cache get
lake build BoundaryVerification
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python verification_patch_v1_5.py
```

The [v1.5 release guide](appendix/v1.5/README.md) lists the six verification layers, expected numerical results, and SHA-256 checksums. Earlier work is available in the [frozen v1.4 theorem release](appendix/v1.4/) and the [analysis directory](analysis/).
