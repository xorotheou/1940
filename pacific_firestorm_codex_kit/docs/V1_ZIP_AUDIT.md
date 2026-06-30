# V1 ZIP Audit

## What the existing ZIP already contains

The current ZIP is useful. It contains:
- Master Codex prompt.
- Phase prompts 0-21.
- Debug prompts.
- Plane asset folders.
- Transparent PNG aircraft sprites.
- Plane asset manifest.
- PDF planning documents.
- Data examples for enemies, weapons, power-ups, waves, and stage 1.

## Main weakness found

The current ZIP is still written like a staged prototype kit. It repeatedly permits placeholder work and stops at "first complete stage" / "import uploaded plane assets". That is useful for a prototype, but it is not strict enough for the requested goal: a complete playable Version 1.

## Required upgrade

The agent must now be given a hard V1 release target:
- Full campaign, not one wave test.
- Final V1 art treatment, not placeholders.
- Build/test/fix loops.
- Acceptance gates.
- Exportable release build.
- Final audit pass.

This V1 extension pack adds those missing constraints.
