# V1 Definition of Done

The agent may not call the project "V1 complete" until all gates below pass.

## Gate 1 - Project integrity

- Godot project opens from a clean checkout.
- Main scene loads.
- No script parse errors.
- No missing critical resources.
- No broken scene references.
- No Godot console spam during normal play.

## Gate 2 - No-placeholder gate

The playable V1 route must have zero visible placeholder content.

Fail if any normal player-facing scene contains:
- grey cube aircraft
- default Godot icon as gameplay asset
- missing texture checkerboard
- text saying placeholder, temp, test, TODO, stub, WIP, or not implemented
- debug labels visible in release mode
- dummy menu buttons that do nothing
- mute gameplay due to missing audio

The source repo may contain documentation about placeholders, but the game itself may not present placeholder content to players.

## Gate 3 - Campaign completeness

- Title screen starts campaign.
- Missions 1-5 are playable.
- Each mission has multiple enemy waves.
- Each mission ends with a boss or major set-piece.
- Mission complete flow works.
- Campaign complete flow works after final mission.
- Restart after death works.
- Return to title works.

## Gate 4 - Core gameplay

- Player movement works with keyboard.
- Player movement supports gamepad where possible.
- Player shooting works.
- Enemy spawning works from data files.
- Enemy bullets work.
- Player damage/lives work.
- Game over works.
- Score works.
- High score persists.
- Power-ups work.
- Bomb/special attack works.
- Boss phases work.

## Gate 5 - Aircraft asset gate

- All six uploaded aircraft assets are imported as real V1 aircraft.
- Player uses silver twin-boom aircraft.
- Basic enemy uses dark green fighter.
- Elite enemy uses camo fighter.
- Fast interceptor uses pale grey fighter.
- Heavy bomber uses green twin-engine bomber.
- Final boss uses six-engine aircraft.
- All aircraft face upward.
- All aircraft are centered and scaled consistently.
- All aircraft have shadows.
- All aircraft have fair hitboxes.

## Gate 6 - Visual and readability gate

- Bullets remain readable over ocean/cloud/island backgrounds.
- Enemy bullets are visually distinct from player bullets.
- Power-ups are visible.
- Player hitbox is fair.
- Explosions do not hide unavoidable bullets unfairly.
- UI remains readable during combat.

## Gate 7 - Audio gate

- Menu music or ambience exists.
- Stage music or ambience exists.
- Fire/explosion/hit/power-up/menu sounds exist.
- Missing audio files do not crash the game.
- V1 release is not silent.

## Gate 8 - Performance gate

- Bullet/effect cleanup works.
- No unbounded spawning/leaking entities.
- Object pooling or safe cleanup exists for heavy repeated entities.
- FPS remains acceptable in dense combat on a normal development machine.

## Gate 9 - Export gate

- Export preset exists for at least one desktop target.
- Release checklist exists.
- Build instructions exist.
- Version number is set to 1.0.0 or 0.1.0-V1 according to project decision.

## Gate 10 - Final audit

The agent must produce:
- RELEASE_NOTES_V1.md
- FINAL_V1_AUDIT.md
- KNOWN_LIMITATIONS_V1.md
- TEST_RESULTS_V1.md

Known limitations are allowed only if they do not break the V1 promise.
