# Unreal Project Generation Specification

## Project identity

- Project name: `BreakingChainsRome`.
- Product title: `Breaking Chains: Rome`.
- Project type: C++ Unreal Engine 5 game.
- Primary game module: `BreakingChains`.
- Primary test module: `BreakingChainsTests`.
- Root content folder: `/Game/BreakingChains/`.

## Required folders

```text
BreakingChainsRome/
├── BreakingChainsRome.uproject
├── Config/
├── Content/
│   └── BreakingChains/
│       ├── Maps/
│       ├── Data/
│       ├── Blueprints/
│       ├── UI/
│       ├── Audio/
│       ├── VFX/
│       ├── Materials/
│       ├── Characters/
│       └── World/
├── Source/
│   ├── BreakingChains/
│   └── BreakingChainsTests/
├── Scripts/
├── Tools/
└── Tests/
```

## Initial project settings

- C++ project.
- Third-person template only as temporary controller scaffolding.
- Enhanced Input enabled.
- World Partition enabled for the main world.
- Niagara enabled.
- Level Sequence enabled.
- Gameplay Tags enabled.
- Asset Manager enabled.
- Automation tests enabled.
- Localization dashboard enabled.

## Project-generation rule

The LLM must first generate the `.uproject`, module descriptors, build targets, Config files, empty module classes, and validation command. It must not begin with art assets or complex Blueprints.

## Initial maps

- `L_Bootstrap`: test map and debug shell.
- `L_Ashgrove_VS`: vertical-slice World Partition map.
- `L_Test_Missions`: isolated mission-system test map.

## Initial plugins

Enable only plugins required by the specification. Any third-party plugin requires a source, license, pinned version, compatibility statement, and fallback plan.
