# C++ and Blueprint Boundaries

## C++ owns

Campaign state and save/load; mission prerequisites and transitions; objective completion; date and time; gameplay-critical NPC schedules; travel graph; faction state and reputation; evidence; rescue capacity; fire transitions; reward idempotency; deterministic seed handling; validation and error reporting.

## Blueprints own

Authored interaction presentation; animation montages and notify reactions; cinematic cameras; audio and VFX triggers; UI composition; non-critical ambient reactions; mission-specific visual staging that calls C++ objective APIs.

## Blueprint rule

A Blueprint may request a transition, but only C++ validates and commits it. A Blueprint must not directly modify a saved mission flag, final-state invariant, named-character survival state, or evidence state.

## C++ API style

Expose narrow `UFUNCTION(BlueprintCallable)` methods such as `TryCompleteObjective(FName ObjectiveId)`, `CanStartMission(FName MissionId)`, `DiscoverRoute(FName RouteId)`, `AssignRescue(FName RescueId, FName DestinationId)`, and `RequestFireTransition(FName ZoneId)`. Each returns a structured result containing success, failure reason, and resulting state.
