# Risk Ownership and Validation

| Risk | Owner | Early signal | Mitigation | Validation gate | Status |
|---|---|---|---|---|---|
| Network becomes a dashboard instead of play | Design | players ignore variables or cannot explain tradeoffs | reduce visible variables per moment; preserve underlying state | slice usability test | OPEN |
| Historical context becomes cosmetic | Narrative/design | systems-off and systems-on plans are identical | require historical knowledge to alter available approaches | slice comparison test | OPEN |
| Fail-forward feels arbitrary | Narrative/engineering | players reload instead of adapting | authored recovery states and clear debrief | slice playtest | OPEN |
| Accessibility overloads UI | UX/accessibility | confusion or missed signals | progressive disclosure and user-configurable density | accessibility test | OPEN |
| Scope expands beyond slice | Production | assets or systems outside mandatory matrix enter sprint | change-control review and cut rules | weekly scope review | OPEN |
| Ancient-language claims exceed evidence | Historical consultant | uncertain line treated as fact | placeholder metadata and specialist gate | content lock | OPEN |
| Sensitive content causes harm | Sensitivity lead | playtest distress or exploitative framing | warnings, alternatives, controls, revision | content review | OPEN |
| Conda/CI remains unstable | Technical | workflow failure or environment drift | pin environment, archive logs, rerun on PR | foundation gate | OPEN |

Open means actively managed, not ignored. No open risk is hidden behind a completion label.
