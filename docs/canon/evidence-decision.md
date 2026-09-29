# Canonical Evidence Decision

## Evidence authority

`data/evidence-definitions.yaml` is the only canonical evidence registry. Mission briefs describe how evidence is obtained; the registry records identity, target, category, and acquisition mission.

## Acquisition rules

- `EVID-OST-001` is acquired by ACT-ROME-010 and identifies the Alexandria route.
- `EVID-AEG-001` is acquired by ACT-ROME-014 and links Livia's textile cipher to Aulus Secundus.
- `EVID-AEG-002`, `EVID-AEG-003`, and `EVID-AEG-004` complete Aulus's Act III dossier.
- `EVID-SYR-002`, `EVID-SYR-003`, and `EVID-SYR-004` complete Crispus's dossier.
- `EVID-THR-002`, `EVID-THR-003`, and `EVID-THR-004` complete Drusus's dossier.
- `EVID-ROM-002`, `EVID-ROM-003`, and `EVID-ROM-004` complete Fabius's dossier.
- `EVID-HIS-001` is acquired by ACT-ROME-018 and is optional supporting evidence; it reduces Act IV supply cost but cannot replace a target dossier.

## Dossier rule

Every target requires exactly three categories: operational, personal_link, and public_leverage. A resolution mission requires all three verified records for that target.
