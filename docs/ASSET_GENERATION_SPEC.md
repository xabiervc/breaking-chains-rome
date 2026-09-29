# Asset Generation Specification

## Principle

The LLM may generate implementation-ready asset briefs, placeholder geometry, material instances, UI mockups, data assets, and editor scripts. It must not claim that generated assets are historically verified or production quality without review.

## Asset brief fields

- Stable asset ID.
- Asset type.
- Location/region.
- Historical classification.
- Dimensions or scale.
- Materials.
- Required LODs.
- Nanite suitability.
- Collision requirements.
- Texture budget.
- Animation requirements.
- Audio/VFX dependencies.
- License/provenance.
- Review status.

## Generation order

1. Blockout geometry.
2. Collision and navigation.
3. Gameplay interaction points.
4. Material and lighting pass.
5. Historical prop pass.
6. Character and animation pass.
7. VFX/audio pass.
8. Optimization and LOD/HLOD pass.

## Historical asset rule

Every asset inspired by the ancient world receives `[FACT]`, `[RECONSTRUCTION]`, or `[FICTION]` metadata and a research note.
