# Breaking Chains: Rome

Production bible and Unreal Engine 5 preimplementation package for a deterministic, historically grounded open-world action-adventure set across the Roman Empire during AD 54–64.

## Core premise

Dama, a fictional Thracian-born enslaved blacksmith, escapes a Campanian estate after his sister Livia is sold into the imperial trafficking network. Over ten years he travels through the empire, builds a resistance network, dismantles the four power centers that protect the trade, and initiates the Great Fire of Rome on 18 July AD 64 as the canonical climax.

## Repository status

This repository contains the narrative bible, mission and world specifications, structured content, schemas, deterministic validation tools, Unreal Engine 5 architecture, and the LLM implementation contract. It is ready for project generation and vertical-slice implementation, but it is not itself a compiled or playable Unreal project.

## Technical decision

- Unreal Engine 5.
- Native C++ for authoritative runtime systems.
- Blueprints for authored presentation and composition.
- Python for editor/content automation only.
- YAML → validation → Unreal Data Assets/Data Tables.
- World Partition for open-world streaming.
- Git LFS for binary Unreal assets.

C# is not the canonical runtime language. It may be evaluated in an isolated experimental branch through a pinned third-party plugin, but production must not depend on it.

## Start here

1. Read `docs/LLM_CONTEXT_INDEX.md`.
2. Read `CLAUDE.md` and `docs/LLM_IMPLEMENTATION_CONTRACT.md`.
3. Run `python tools/run_all_validators.py`.
4. Follow `docs/PROJECT_GENERATION_SPEC.md`.
5. Follow `docs/CODE_GENERATION_ORDER.md`.
6. Implement `docs/VERTICAL_SLICE_IMPLEMENTATION.md`.

## Historical disclaimer

Ancient sources disagree about the Great Fire's cause and do not establish the game's explanation. The project presents Dama's secret role as historical fiction, not as a claim about what actually happened.
