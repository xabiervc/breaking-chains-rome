# Narrative State Machine

## State dimensions

- Campaign act: I, II, III, IV, epilogue.
- Network pressure: low, rising, coordinated, crisis.
- Cell status: forming, active, compromised, autonomous, dispersed, lost.
- Relationship: unknown, cautious, trusted, strained, broken, repaired, independent.
- Person outcome: sheltered, relocated, hidden, autonomous, separated, dead, unknown.
- Evidence: unverified, partial, corroborated, exposed, lost, contested.
- Historical label: FACT, RECONSTRUCTION, FICTION, OPEN QUESTION.

## Transition rules

Every transition has an authored trigger, visible feedback, affected variables, and a recovery or irreversible consequence statement. Hidden random transitions are prohibited for canon-critical outcomes.

## Save-facing state

Save files must include a schema version, campaign timestamp, network variables, node/link/cell state, companion states, evidence status, settings, localization key version, and migration history.

## Acceptance tests

- Same seed and input sequence produces the same state hash.
- Reloading at a checkpoint preserves the intended state.
- An interrupted save cannot silently revert a completed consequence.
- Unknown historical outcomes remain unknown rather than being fabricated as certainty.
