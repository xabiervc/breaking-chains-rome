# Build and CI

## Pull-request checks

Every pull request must run YAML parsing, JSON schema validation, cross-reference validation, mission dependency validation, determinism declaration validation, final-state invariant validation, C++ compilation when the Unreal project exists, and Unreal automation tests when the target is available.

## Branch policy

The `main` branch must reject changes that fail content validation or canonical invariant tests.

## Artifacts

CI stores the validation report, content manifest, schema version, test summary, and a packaged development build when available.

## Commands

```text
python tools/run_all_validators.py
python tools/validate_cross_references.py
```

Once Unreal is initialized:

```text
RunUAT BuildCookRun ...
```

The exact engine version and build command must be locked in the repository before C++ implementation begins.
