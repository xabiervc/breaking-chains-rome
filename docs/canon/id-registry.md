# Stable ID Registry

## Rules

- IDs are immutable.
- Display names may be localized; IDs may not.
- An ID cannot change entity type.
- Deleted entities remain reserved.
- Every structured reference must resolve through this registry.

## Entity ranges

| Type | Pattern | Example |
|---|---|---|
| Main mission | `ACT-ROME-###` | ACT-ROME-042 |
| Side mission | `SIDE-REGION-###` | SIDE-ITA-001 |
| Character | `CHAR-###` | CHAR-001 |
| Location | `LOC-REGION-###` | LOC-ITA-003 |
| Faction | `FACTION-###` | FACTION-001 |
| Evidence | `EVID-REGION-###` | EVID-AEG-004 |
| Route | `ROUTE-###` | ROUTE-001 |
| Fire zone | `FIRE-ZONE-###` | FIRE-ZONE-001 |
| Evacuation route | `EVAC-###` | EVAC-001 |
| Dialogue scene | `SCENE-REGION-###` | SCENE-ITA-001 |

## Canonical character IDs

CHAR-001 Dama; CHAR-002 Livia; CHAR-003 Vindex Varro; CHAR-004 Cassia Varro; CHAR-005 Aulus Secundus; CHAR-006 Gaius Valerius Crispus; CHAR-007 Marcus Laelius Drusus; CHAR-008 Lucius Fabius Varro; CHAR-009 Nicanor; CHAR-010 Tertia; CHAR-011 Bato; CHAR-012 Eirene; CHAR-013 Publius Caecilius.

## Reserved supporting IDs

Nera, Silvanus, Otho, Vara, Herennius, Lucan, Silia, Sura, Menon, Ptolemy, and Marius Pell must receive stable `CHAR-###` IDs before runtime integration.
