# Asset Pipeline

## Source control

Git stores source, configuration, Markdown, YAML, JSON, C++, and Blueprint text exports. Git LFS stores Unreal binary assets such as `.uasset`, `.umap`, large textures, audio, animation caches, and cinematics. Generated build, intermediate, derived-data, and local-user folders are ignored.

## Asset naming

`DA_` Primary Data Assets; `DT_` Data Tables; `BP_` Blueprints; `WBP_` Widgets; `L_` Levels; `DL_` Data Layers; `SM_` Static Meshes; `SK_` Skeletal Meshes; `M_` Materials; `MI_` Material Instances; `NS_` Niagara Systems; `S_` Sounds; `VO_` Voice assets.

## Import rule

Every authored asset requires a source, owner, stable ID where relevant, license/provenance note, target quality tier, and validation status. Architecture, costume, language, props, signage, and audio assets require historical classification and review status before production lock.
