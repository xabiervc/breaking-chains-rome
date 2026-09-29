# Data Asset Architecture

## Source hierarchy

1. Markdown defines design intent.
2. YAML is the repository source for content tables.
3. A deterministic import step converts YAML into versioned Unreal assets.
4. Runtime consumes validated `UPrimaryDataAsset` and `UDataTable` assets.
5. Save data stores stable IDs and state, never editor object paths as identity.

## Asset classes

`UBCMissionDataAsset`; `UBCCharacterDataAsset`; `UBCLocationDataAsset`; `UBCFactionDataAsset`; `UBCEvidenceDataAsset`; `UBCTravelRouteDataAsset`; `UBCFireZoneDataAsset`; `UBCEvacuationRouteDataAsset`; `UBCLanguageDataAsset`.

## Stable identity

Every asset has a stable `FName` ID matching the repository data ID. Asset paths may change; IDs may not.

## Import requirements

The importer must parse YAML, validate schemas and cross-references, fail the build on missing required fields, produce a deterministic manifest, refuse to overwrite an asset with a different semantic ID, and record content version and source hash.

Use Data Tables for homogeneous tabular records and Primary Data Assets for authored entities with references and editor-facing metadata. Do not store mission-critical values only in Blueprint defaults.
