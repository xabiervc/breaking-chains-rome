# Performance and Memory Budget

## Initial budgets

These are engineering targets, not achieved results.

- Primary PC target: 60 FPS target, 16.67 ms frame budget; 30 FPS floor for supported low settings.
- Handheld target: 30 FPS locked target with stable frame pacing.
- Main menu to playable load: <= 12 seconds on reference SSD; checkpoint load: <= 8 seconds.
- Save operation: <= 2 seconds median, <= 5 seconds p95.
- Memory: define per-platform working-set budgets before vertical slice; initial ceiling 8 GB for PC/handheld content profile, with streaming and peak capture required.
- Streaming hitch target: no hitch above 100 ms during validated traversal on reference hardware.

## Measurement rules

Report p50/p95 frame time, memory peak, shader compilation impact, streaming hitches, load/save latency, and crash-free session duration. A target is not evidence until captured on the declared hardware.
