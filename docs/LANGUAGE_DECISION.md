# Programming Language Decision

## Decision

Use **native Unreal C++** for authoritative runtime systems and **Blueprints** for authored presentation and composition. Do not make C# a production dependency.

## Why not C# as the default

Unreal Engine's first-party development workflow is centered on C++ and Blueprints. Epic's official documentation describes Blueprints as a complete gameplay scripting system and documents C++ as the native programming route.[web:70][web:75] C# is possible through third-party plugins such as UnrealSharp, but that introduces an additional dependency, version-compatibility risk, reflection constraints, plugin maintenance, and CI complexity.[web:104][web:107]

For a long-lived, open-world project with deterministic save state, World Partition, Data Assets, automation tests, and a future production team, native C++ is the safer canonical base. C# would not automatically produce better code or better performance inside Unreal; it would mainly change the syntax and dependency model.

## Recommended split

- **C++:** campaign state, mission state machine, objective validation, deterministic clock, schedules, travel graph, faction state, evidence, rescue ledger, fire transitions, save/load, migration, validation hooks, automation tests.
- **Blueprints:** cinematic staging, authored mission presentation, UI composition, animation/VFX/audio hooks, designer-tunable parameters that do not bypass C++ validation.
- **Python:** editor automation, asset import/export, YAML-to-Data-Asset conversion, validation reports, batch naming, metadata updates. Python does not run authoritative gameplay logic.

## C# contingency

If C# becomes a hard requirement, use UnrealSharp only in a separate experimental branch after the native C++ vertical slice is working. Do not mix C# gameplay authority with the canonical C++ systems. Pin the UnrealSharp version, .NET version, Unreal minor version, and plugin source commit before testing. Keep a C++ fallback for every reflected boundary.

## Final rule

The project may use C# for external tools, content pipelines, or editor utilities, but the game runtime remains C++ plus Blueprints.
