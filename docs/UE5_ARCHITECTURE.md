# Unreal Engine 5 Architecture

## Module layout

```text
Source/BreakingChains/
├── Core/
│   ├── BCGameInstance
│   ├── BCGameMode
│   ├── BCGameState
│   ├── BCWorldSubsystem
│   └── BCDeterminismSubsystem
├── Content/
│   ├── BCContentRegistry
│   ├── BCDataValidation
│   └── BCLocalization
├── Missions/
│   ├── BCMissionSubsystem
│   ├── BCMissionState
│   ├── BCObjectiveComponent
│   └── BCMissionDependencyResolver
├── World/
│   ├── BCTravelSubsystem
│   ├── BCScheduleSubsystem
│   ├── BCRegionSubsystem
│   └── BCFactionSubsystem
├── Player/
│   ├── BCDamaCharacter
│   ├── BCInventoryComponent
│   ├── BCSkillComponent
│   └── BCIdentityComponent
├── Evidence/
│   ├── BCEvidenceSubsystem
│   └── BCEvidenceRecord
├── Rescue/
│   ├── BCRescueLedgerSubsystem
│   └── BCRescueRecord
├── Fire/
│   ├── BCFireSubsystem
│   ├── BCFireZoneActor
│   └── BCEvacuationSubsystem
└── Save/
    ├── BCSaveGame
    ├── BCSaveSerializer
    └── BCSaveMigration
```

## Authority rule

If a value can alter a mission outcome, save file, named-character status, reward, historical date, route availability, evidence state, rescue count, or fire transition, it is authoritative C++ state or validated data. Blueprint-only state must never be the sole source of a gameplay-critical fact.

## Subsystems

Use `UGameInstanceSubsystem` for campaign-lifetime services and `UWorldSubsystem` for world/session services. Do not store persistent campaign state in level actors.

## Event model

Authoritative systems publish typed events: `FBCMissionCompleted`, `FBCEvidenceVerified`, `FBCFactionStateChanged`, `FBCRescueAssigned`, `FBCRouteDiscovered`, `FBCFireZoneTransitioned`, and `FBCSaveCommitted`. Presentation systems may subscribe but cannot mutate canonical state without calling an authoritative subsystem API.
