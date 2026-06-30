# V1 Automated and Manual Test Plan

## Agent must create tests where practical

Godot games need both automated checks and manual play checks.

## Automated checks

The agent should add scripts/tests for:
- JSON file load validity.
- Enemy type definitions have required fields.
- Wave files reference existing enemy types.
- Weapon definitions have required fields.
- Power-up definitions have required fields.
- Stage list references existing stage/wave files.
- Scene paths in data files exist.
- No player-facing placeholder strings in release scenes.
- High score save/load works.

## Runtime smoke checks

The agent should create a headless smoke test scene or script that checks:
- Main scene loads.
- GameState initializes.
- StageManager can load all stages.
- EnemySpawner can parse all wave files.
- Player scene can instantiate.
- Each enemy scene can instantiate.
- Each bullet scene can instantiate.
- HUD scene can instantiate.

## Manual play checks

The final human/agent review should confirm:
- Mission 1 can be completed.
- Mission 2 can be completed.
- Mission 3 can be completed.
- Mission 4 can be completed.
- Mission 5 can be completed.
- Player can die and restart.
- Player can pause and resume.
- Campaign complete screen appears.
- No placeholder content appears.

## Suggested command discipline

The agent should first inspect local Godot command support:

```bash
godot --help || godot4 --help || true
```

Then use whichever executable exists. Do not assume a specific binary name. Common names are `godot`, `godot4`, or an editor-specific executable.

If Godot is unavailable, the agent must still validate data files, scripts, paths, and docs, then create `BLOCKERS.md` explaining that engine runtime testing could not be performed.
