# Canonical source hierarchy

This is a preimplementation specification, not validated runtime content. `data/mission-definitions.yaml` contains all 42 main missions. `data/*-definitions.yaml` is the structured source; individual `docs/missions/ACT-ROME-###.md` files describe authored intent. `docs/canon/continuity-matrix.md` records narrative constraints. If these disagree, stop implementation and fix all affected files together; no silent precedence resolves a contradiction.

Only files enumerated in `docs/canon/canonical-manifest.yaml` may be used as canonical input. The legacy folder contains warnings rather than original snapshots. Older duplicate YAML files still exist at the root of `data/`; they are not in the manifest and must not be imported. Their removal or archival requires a separately reviewed deletion/migration action.

The Act I interstitial transition is `act1_interstitial_complete`, a campaign-state flag set by the authored time-passage sequence after ACT-ROME-004. It is not a mission ID. The YAML `prerequisites` field contains mission IDs only; `required_flags` contains campaign flags.

`GDD.md` is the root master GDD; there is no `docs/GDD.md`. Validate the manifest path before building any importer. Existing Act IV state files are excluded from runtime import pending resolution of their contradictory evacuation rules.
