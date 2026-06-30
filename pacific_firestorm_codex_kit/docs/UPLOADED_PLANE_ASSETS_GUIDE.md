# Uploaded Plane Assets Guide

Six aircraft images have been added to the kit as top-down placeholders/references for the Godot game.

## Asset Locations

- Raw source JPGs: `assets/plane_assets/raw_jpg/`
- Background-removed PNGs: `assets/plane_assets/transparent_png/`
- 512×512 previews: `assets/plane_assets/preview_512_png/`
- Structured manifest: `data_examples/plane_assets/plane_asset_manifest.json`

## Suggested In-Game Mapping

| Manifest ID | Suggested Game Role | Notes |
|---|---|---|
| PF_PLANE_01_PLAYER_TWIN_BOOM | Player aircraft | Most distinctive and readable player silhouette. |
| PF_PLANE_02_ENEMY_LIGHT_FIGHTER_DARK | Light fighter / ace | Dark aircraft; good enemy contrast. |
| PF_PLANE_03_ENEMY_TWIN_ENGINE_BOMBER | Bomber | Use larger health and score value. |
| PF_PLANE_04_ENEMY_CAMO_FIGHTER | Elite camo fighter | Add outline/glow if camouflage reduces readability. |
| PF_PLANE_05_ENEMY_LIGHT_FIGHTER_WHITE | Alternate fighter | Works as early enemy or escort. |
| PF_PLANE_06_BOSS_SUPER_BOMBER | Boss super bomber | Use multi-phase boss logic and boss HP bar. |

## Godot Implementation Notes

For the first Godot implementation, use these as **sprite/billboard placeholders** in the orthographic 3D scene rather than trying to model full 3D aircraft immediately.

Recommended setup:

```text
AircraftVisualRoot
  └── Sprite3D or MeshInstance3D plane-card using transparent PNG
AircraftCollisionRoot
  └── Area3D
      └── CollisionShape3D
```

Gameplay should remain independent of image dimensions:

- Each aircraft type should have exported visual scale.
- Hitboxes should be hand-tuned, not derived from the sprite silhouette.
- Boss aircraft should use multiple optional weak points later.
- Add outlines or lighting separation where realistic assets become hard to see.

## Codex Prompt

Use `prompts/21_phase_21_import_uploaded_plane_assets.txt` after the core player/enemy systems exist.
