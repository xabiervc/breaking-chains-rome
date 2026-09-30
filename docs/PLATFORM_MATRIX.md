# Platform Matrix

## Target tiers

| Tier | Target | Priority | Gate |
|---|---|---:|---|
| Primary | Windows PC, keyboard/mouse and controller | P0 | vertical slice and release candidate |
| Secondary | Steam Deck-class handheld | P1 | vertical slice compatibility and release candidate performance |
| Later | Current-generation console equivalent | P2 | only after platform-specific dev kits and certification planning |

## Rationale

The primary tier keeps the first implementation testable while preserving controller and keyboard parity. Handheld validation protects readability, performance, suspend/resume, and battery-sensitive behavior. Console support is not assumed until platform requirements are known.

## Matrix evidence

Record OS, GPU/CPU/RAM, display scale, input device, graphics settings, frame-time capture, memory, load/save latency, crash result, and accessibility result per platform.
