# AGENTS.md - Pacific Firestorm

## Project Summary

Pacific Firestorm is an original Godot 4 vertical-scrolling aerial shooter inspired by classic arcade air-combat shooters, but with a modern ultra-realistic visual direction.

The game should feel like a simple, fast, readable arcade shooter. It should not become a realistic flight simulator.

## Core Design Rule

Arcade gameplay. Realistic visuals. Original identity.

## Legal / Creative Boundaries

Do not copy:
- Capcom branding
- 1942 name
- original 1942 sprites
- original 1942 sound effects
- original 1942 music
- exact 1942 enemy waves
- exact 1942 level layouts
- exact 1942 UI
- recognizable direct clones of copyrighted assets

Create original aircraft designs, enemy waves, UI, effects, levels, names, music, and sounds.

## Engine

Use Godot 4.x.

## Language

Use GDScript unless specifically instructed otherwise.

## Game Type

Top-down / slight-tilt orthographic 3D vertical shooter.

Gameplay is 2D arcade logic on the X/Z plane. Visuals use 3D models, lighting, particles, and shaders.

## Camera

Use Camera3D with orthographic projection. The camera looks downward at the battlefield. The gameplay plane is X/Z. Y is used for height/visual layering if needed.

## Code Style

- Keep scripts small and readable.
- Prefer composition over giant manager scripts.
- Keep gameplay logic separated from rendering/effects.
- Use signals for major events where appropriate.
- Use data files for stages, enemies, waves, weapons, and power-ups.
- Keep the project runnable after every phase.
- Do not add advanced features before the core loop works.
- Do not over-engineer.

## Required Core Systems

- Main scene
- Player aircraft
- Player movement
- Player shooting
- Player damage/lives
- Enemy base class
- Enemy spawner
- Enemy movement patterns
- Bullet system
- Collision detection
- Score system
- HUD
- Game states
- JSON wave loading
- Stage manager
- Effects manager
- Audio manager
- Menus
- Export documentation

## Gameplay Feel

The game should be responsive and arcade-like.

Do not implement realistic:
- lift
- drag
- stalls
- fuel
- limited ammunition
- complex aerodynamics
- long turning radius

The player should move instantly and precisely.

## Hitboxes

Use fair arcade-style hitboxes. The visual model may be large, but the actual player damage hitbox should be small and readable.

## Readability

Even with realistic graphics, bullets, enemy fire, power-ups, and hazards must remain visible.

Use:
- tracer glow
- clear silhouettes
- UI highlights
- readable contrast
- consistent bullet colours

## Performance Rules

Use object pooling for:
- player bullets
- enemy bullets
- explosions
- smoke trails
- hit sparks

Avoid:
- excessive real-time lights
- excessive transparent particles
- huge uncompressed textures
- high-poly models for small screen objects

## Data-Driven Design

Use JSON for:
- enemy types
- weapon types
- power-up types
- stages
- enemy waves

Do not hard-code whole stages in scripts.

## Development Discipline

For every task:
1. Make the smallest useful change.
2. Keep the project runnable.
3. Update documentation if behaviour changes.
4. Add clear notes to docs/known_issues.md if something is unfinished.
5. Do not silently remove existing functionality.

## Acceptance Criteria for Every Phase

A phase is complete only when:
- the project opens in Godot
- there are no script parse errors
- the main scene runs
- the implemented feature works in a basic way
- obvious errors are documented or fixed
