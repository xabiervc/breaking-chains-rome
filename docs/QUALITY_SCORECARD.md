# Quality Scorecard

Score each category 0–4 at every gate:

- 0: absent or contradicted.
- 1: concept only.
- 2: implemented inconsistently.
- 3: production-ready with evidence.
- 4: distinctive, polished, and externally playtested.

| Category | Gate target | Evidence |
|---|---:|---|
| Creative identity | 3 before vertical slice, 4 before release candidate | art/audio bible, slice review |
| Core gameplay | 3 before vertical slice, 4 before content lock | teach-use-master telemetry and playtests |
| Narrative | 3 before vertical slice, 4 before content lock | script review, choice matrix, sensitivity review |
| Accessibility | 3 before vertical slice, 4 before release candidate | feature matrix and disabled playtests |
| Historical integrity | 3 before vertical slice, 4 before release candidate | source ledger and specialist sign-offs |
| UX/readability | 3 before vertical slice, 4 before release candidate | task tests, subtitle and HUD review |
| Technical stability | 3 before vertical slice, 4 before release candidate | CI, crash-free sessions, soak tests |
| Performance | 3 before vertical slice, 4 before release candidate | target-hardware captures and frame-time reports |
| Audio/visual polish | 3 before vertical slice, 4 before release candidate | mix review, art review, accessibility review |
| Emotional coherence | 3 before vertical slice, 4 before release candidate | external playtest synthesis |

Release-candidate rule: no category below 3, no blocker open, and all required specialist reviews complete.
