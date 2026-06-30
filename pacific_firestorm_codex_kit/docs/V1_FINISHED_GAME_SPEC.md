# Pacific Firestorm - Finished Game V1 Specification

## Product goal

Pacific Firestorm V1 is a complete vertical-scrolling aerial shooter built in Godot 4 using GDScript. It is inspired by classic arcade air-combat shooters, but it is an original game. It must be playable from title screen to campaign completion.

## V1 content floor

The finished V1 must include at least:

### Campaign
- 5 complete missions.
- Each mission has a beginning, middle, end, escalating waves, and a boss or major set-piece.
- Mission complete screen after each mission.
- Campaign complete screen after Mission 5.

### Missions
1. Open Pacific - tutorial-grade combat over calm ocean.
2. Island Chain - islands, AA guns, elite fighters.
3. Carrier Raid - ships, carrier deck hazards, torpedo/bomber waves.
4. Storm Front - rain/cloud visibility pressure, faster enemy patterns.
5. Final Assault - mixed waves and super-bomber final boss.

### Aircraft roles from uploaded assets
- Silver twin-boom aircraft: player aircraft.
- Dark green single fighter: basic enemy fighter.
- Pale grey single fighter: fast interceptor.
- Camo single fighter: elite fighter.
- Green twin-engine bomber: heavy bomber.
- Large six-engine aircraft: boss / super-bomber.

### Core systems
- Title screen.
- Options screen.
- Controls screen.
- Pause menu.
- Game over screen.
- Mission complete screen.
- Campaign complete screen.
- Score and high score.
- Lives / health.
- Bomb or special attack.
- Weapon upgrades.
- Power-ups.
- Enemy wave system.
- Boss system.
- Stage manager.
- Audio manager.
- Save/settings manager.
- Debug/dev scene hidden from normal play.
- Export presets/documentation.

### Gameplay
- Responsive arcade movement.
- Player remains inside playfield bounds.
- Player shoots forward/up-screen.
- Enemy bullets are visible and readable.
- Player hitbox is smaller than the aircraft sprite.
- Enemies use fair simplified hitboxes.
- Weapon upgrades noticeably change the fire pattern.
- Boss phases escalate clearly.
- Game can be completed without developer cheats.

### Visuals
- Uploaded plane sprites are used as final V1 aircraft art.
- No placeholder cube aircraft in shipped route.
- Ocean scrolls continuously and has finished V1 material/texture treatment.
- Islands, clouds, ships, carrier, bullets, explosions, smoke, shadows, and UI must be visually present and coherent.
- Visual style can be simple but must look intentional.
- Aircraft shadows must be present.
- Propeller blur or equivalent motion treatment must be present for propeller aircraft.

### Audio
- Music or ambient loop for menus and gameplay.
- Player fire sound.
- Enemy fire sound.
- Explosion sound.
- Player hit sound.
- Power-up sound.
- Boss warning sound.
- Menu navigation sounds.
- Mission complete/game over sounds.

Audio may be generated procedurally or synthesized in-repo if no external audio assets are available. Silence is not acceptable for V1.

### Export
- Desktop export target must be configured.
- Release package instructions must exist.
- The project must run from a clean checkout.

## V1 quality target

This is not a AAA commercial game. It is a finished independent V1 release with complete gameplay, coherent art, no placeholder content in the playable route, and a stable release package.
