# V1 Release Build Plan

## Goal

Create a playable packaged desktop build of Pacific Firestorm V1.

## Required release outputs

- Exported game build.
- README with controls and install/run instructions.
- RELEASE_NOTES_V1.md.
- KNOWN_LIMITATIONS_V1.md.
- TEST_RESULTS_V1.md.
- FINAL_V1_AUDIT.md.
- LICENSES_ASSETS.md.

## Versioning

Use one of:
- `1.0.0` if calling it full public V1.
- `0.1.0-v1` if treating it as first playable internal V1.

The user requested playable full Version 1, so the agent should target `1.0.0` unless told otherwise.

## Export targets

Minimum:
- Linux or Windows desktop export depending on environment.

Optional:
- Web export.
- Android export.

Do not block V1 on Android/web unless specifically requested. Desktop first.

## Final release audit

Before packaging, the agent must produce a final audit with:
- gates passed
- gates failed
- known limitations
- exact test commands run
- exact export command run
- final build path
