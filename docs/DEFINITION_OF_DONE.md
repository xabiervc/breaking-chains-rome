# Definition of Done

## Documentation

- Canonical design documents are updated.
- Stable IDs are unique.
- Historical claims are labeled.
- Cross-references resolve.
- Deterministic behavior is specified.

## Runtime code

- C++ compiles in the locked Unreal version.
- Public APIs have comments and validation.
- Gameplay-critical state is authoritative.
- Save/load behavior is versioned.
- Automation tests pass.
- No hidden gameplay-critical constants exist in Blueprints.

## Content

- YAML validates.
- Data Assets import successfully.
- Asset IDs match source IDs.
- Localization keys exist.
- Historical and sensitivity review status is recorded.

## Vertical slice

- L_Ashgrove_VS opens.
- ACT-ROME-001 can be started and completed.
- Save/load restores state.
- ACT-ROME-008 is locked before ACT-ROME-007.
- Repeated input produces the same authoritative outcome.
- Debug tools expose state without changing it.

## Reporting

Every LLM task reports what was generated, what was executed, what passed, what was not verified, and what remains blocked.
