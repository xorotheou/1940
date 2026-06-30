# START HERE - Pacific Firestorm V1 Agent Coding Pack

This pack upgrades the earlier prompt kit from a staged prototype plan into a strict Codex coding programme for a finished playable Version 1.

## New target

Build a complete playable V1 game, not a demo, not a toy, and not a placeholder prototype.

V1 means:
- The player can start from a title screen.
- The player can play a complete campaign from beginning to end.
- The game has final V1 aircraft sprites using the uploaded plane assets.
- The game has final V1 original/procedural environment, UI, effects, and audio.
- The game has no visible placeholder assets, no broken placeholder labels, and no unfinished placeholder scenes in the playable route.
- The project can be exported as a desktop release build.

## Important clarification

"No placeholders" does not mean the game must use expensive AAA models. It means the shipped V1 must not contain temporary grey boxes, missing art, TODO menus, dummy sounds, broken placeholder scenes, or obvious prototype content.

Allowed V1 assets:
- Uploaded aircraft sprites included in this kit.
- Original procedural ocean, clouds, islands, ships, bullets, explosions, UI, and generated audio.
- Simple but polished original art created inside the repo.
- Code-generated materials, particles, wave patterns, and sounds.

Not allowed in V1:
- Placeholder cube planes.
- Missing textures.
- Text saying "placeholder", "TODO", "stub", "temp", or "not implemented" in the playable game.
- Silent gameplay because audio was not implemented.
- A single test wave pretending to be a full game.
- A one-screen toy prototype.

## How to use

Give Codex the file:

`prompts/22_MASTER_V1_FINISHED_GAME_AGENT_PROMPT.txt`

Then instruct it to follow:

`docs/V1_AGENT_LOOP.md`

and pass all gates in:

`docs/V1_DEFINITION_OF_DONE.md`

The agent should iterate until all gates pass or it creates a clear blocker report.
