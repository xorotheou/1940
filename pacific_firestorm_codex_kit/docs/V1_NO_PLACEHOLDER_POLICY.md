# V1 No-Placeholder Policy

## Principle

V1 may be small, but it must be real. Every player-facing element must look intentional.

## Development placeholders

The agent may temporarily use placeholders while building a feature, but it must not ship them. Before V1 completion, all temporary content must be replaced by V1-quality original content.

## What counts as V1-quality

V1-quality does not require expensive assets. It requires coherent, intentional assets.

Acceptable:
- Uploaded plane sprites.
- Procedural ocean material.
- Procedural islands made from simple meshes/textures.
- Procedural/generated WAV sound effects.
- Simple original UI drawn with Godot controls and materials.
- Simple particle explosions that are tuned and polished.

Not acceptable:
- Grey cubes as final planes.
- Missing textures.
- Default Godot icons.
- Menus with disabled dummy buttons.
- Audio hooks with no sound.
- One test level marketed as a campaign.
- Unimplemented systems hidden behind UI.

## Asset naming rule

During V1 audit, player-facing assets/scenes should not be named:
- placeholder
- temp
- test
- dummy
- stub

Internal debug scenes may include debug naming but must not be accessible in normal release flow.
