# World Partition Plan

## World model

The ten gameplay regions remain a design abstraction, not one real-scale map of the whole Roman Empire. Unreal World Partition manages the continuous playable world while data-driven travel connects distant region cells.

## Initial cell strategy

- Rome: 1 km grid cells with high-density city layers.
- Italia rural corridors: 2 km cells.
- Major cities outside Rome: 1 km cells.
- Rural and frontier regions: 2–4 km cells.
- Interiors: Data Layers or instanced sublevels where profiling requires isolation.

These are initial implementation defaults, not final shipping values.

## Data Layers

Use Data Layers for mission-specific blockouts, Act IV fire states, construction or destruction states, temporary patrol lockdowns, cinematic staging, and historical versus gameplay-abstraction variants.

## HLOD and streaming

Generate HLOD for distant city blocks, roads, vegetation, and static architecture. Nanite and HLOD settings must be profiled together; enabling Nanite does not remove all streaming or memory costs.

The player cell is always loaded; gameplay-critical adjacent cells are prefetched; mission cells are prefetched before cinematic transitions; fire cells are loaded deterministically from the fire-zone graph. Save state never depends on whether an actor happened to be streamed in.

World Partition is a runtime streaming mechanism, not a narrative authority. Mission and campaign state remain in C++ subsystems and save data.
