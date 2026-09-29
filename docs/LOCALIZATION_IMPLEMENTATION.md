# Localization Implementation

## Voice and text separation

In-universe voices remain historically researched languages. Repository source dialogue is English with voice-language metadata. Modern subtitle and interface languages are English, Spanish, French, German, Italian, Brazilian Portuguese, Japanese, Simplified Chinese, and Korean.

## Unreal localization

Use Unreal's Localization Dashboard for UI, subtitles, codex, mission text, and accessibility strings. Stable string keys must never be derived from translated text.

## Dialogue record

Every line includes stable scene ID, stable line ID, speaker ID, intended voice language, register, translation mode, subtitle text key, historical review status, and localization review status.

## Ancient-language rule

Do not generate final Latin, Greek, Aramaic, Egyptian, Punic, Thracian, Celtic, or Iberian dialogue without qualified linguistic review. The LLM may produce English placeholder lines and metadata.
