# Uploaded Plane Assets

These six top-down aircraft images were added as reference/placeholder planes for **Pacific Firestorm**.

Folders:

- `raw_jpg/` — original uploaded images, unchanged.
- `transparent_png/` — background-removed PNG versions for Godot placeholder sprites/billboards.
- `preview_512_png/` — 512×512 transparent previews for quick UI/testing use.

Recommended Godot usage:

1. Import the transparent PNGs as `Texture2D` assets.
2. Use them first as billboard/sprite placeholders in a top-down orthographic 3D scene.
3. Later replace them with optimized 3D models or pre-rendered sprite sheets.
4. Keep arcade hitboxes simple and fair. Do **not** use exact silhouette collision.
5. Add a small outline/glow if the aircraft becomes hard to read over ocean, islands, clouds, or explosions.

Suggested roles:

| Asset | Suggested Role |
|---|---|
| pf_plane_01_player_twin_boom_p38_style | Player aircraft |
| pf_plane_02_enemy_light_fighter_dark | Enemy light fighter / ace |
| pf_plane_03_enemy_twin_engine_bomber | Bomber / mini-boss |
| pf_plane_04_enemy_camo_fighter | Elite camo fighter |
| pf_plane_05_enemy_light_fighter_white | Alternate light fighter |
| pf_plane_06_boss_super_bomber | Boss / heavy bomber |

See `data_examples/plane_assets/plane_asset_manifest.json` for structured metadata.
