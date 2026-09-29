# Technical Stack Decision

## Decision

Use **Unreal Engine 5** as the official runtime and authoring platform for Breaking Chains: Rome.

## Rationale

Unreal Engine 5 is the best fit for this project's visual ambition and open-world scope. Nanite is designed for highly detailed geometry and supports fine-grained streaming; Lumen provides dynamic global illumination and reflections; World Partition is appropriate for streaming a large continuous world. These capabilities are official Unreal technologies, but they increase hardware, asset-production, profiling, and optimization requirements.[web:71][web:75]

This decision optimizes for high-fidelity historical environments, dense cities and interiors, large outdoor regions, cinematic fire, smoke and water, and a long-lived production pipeline. It does not imply that Unreal automatically produces better graphics: final visual quality still depends on art direction, assets, lighting, animation, optimization, and team capability.

## Official baseline

- Engine: Unreal Engine 5.x; exact minor version locked when implementation begins.
- Primary target: PC and current-generation consoles.
- Development rendering: DirectX 12 on Windows.
- Open-world streaming: World Partition.
- High-detail static geometry: Nanite where technically appropriate.
- Dynamic lighting: Lumen where performance targets permit.
- Scripting: native C++ plus Blueprints.
- Source control: Git with Git LFS for binary assets.

## Why not Blueprint-only

Blueprints are a complete node-based gameplay scripting system, but this project has many deterministic, persistent, cross-region systems. Core rules should live in testable C++ and data assets; Blueprints should compose authored missions, presentation, animation, cameras, VFX, and designer-facing interactions.[web:70]

## Why not C++-only

C++-only authoring would slow narrative iteration and make cinematic and mission assembly unnecessarily rigid. Designers need Blueprint-exposed components, Data Assets, and event hooks.

## Language decision

Use **C++ for authoritative runtime systems** and **Blueprints for presentation and composition**.

C++ owns save state, mission state, deterministic clock, schedules, travel, faction state, evidence, rescue ledger, validation hooks, and fire-state transitions. Blueprints own level scripting, cinematic sequences, authored interaction graphs, animation events, UI composition, and non-authoritative audiovisual reactions.

## Licensing and hardware note

Unreal's visual features impose a higher development and performance budget than a lightweight engine. The project must establish a performance budget and target hardware before art production lock.
