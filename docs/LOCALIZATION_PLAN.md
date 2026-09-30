# Localization Plan

## Scope

English source plus Spanish, French, German, Italian, and Brazilian Portuguese as planned localization targets; final languages remain a production decision subject to budget and specialist availability.

## Pipeline

Stable string IDs -> source context -> speaker and register metadata -> translation -> linguistic QA -> historical/language review -> in-game length and subtitle QA -> regression.

## Requirements

No hard-coded dialogue, no concatenation that breaks grammar, plural/gender handling, fallback language, missing-key errors, font coverage, right-to-left readiness where later languages require it, and subtitle expansion testing.

Ancient-language lines need intended-language metadata, translation, pronunciation guidance, and specialist status before recording.
