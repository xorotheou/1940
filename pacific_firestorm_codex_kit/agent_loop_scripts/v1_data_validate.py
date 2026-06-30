#!/usr/bin/env python3
"""Basic V1 data validator for stage/wave/enemy JSON files.

This is a generic helper. Codex should adapt paths to the actual Godot project.
"""
from pathlib import Path
import json, sys

errors = []

def load_json(path):
    try:
        return json.loads(Path(path).read_text(encoding='utf-8'))
    except Exception as e:
        errors.append(f'{path}: {e}')
        return None

for p in Path('data').rglob('*.json') if Path('data').exists() else []:
    load_json(p)

# Optional semantic checks if expected files exist.
enemy_path = Path('data/enemies/enemy_types.json')
wave_dir = Path('data/waves')
if enemy_path.exists():
    enemies = load_json(enemy_path) or {}
    enemy_ids = set(enemies.keys()) if isinstance(enemies, dict) else set()
    if not enemy_ids:
        errors.append('enemy_types.json has no enemy ids')
    if wave_dir.exists():
        for w in wave_dir.glob('*.json'):
            waves = load_json(w)
            if not isinstance(waves, list):
                errors.append(f'{w}: expected list of wave entries')
                continue
            for idx, entry in enumerate(waves):
                et = entry.get('enemy_type') if isinstance(entry, dict) else None
                if et and et not in enemy_ids:
                    errors.append(f'{w}[{idx}]: unknown enemy_type {et}')

if errors:
    print('V1 DATA VALIDATION FAILED')
    for e in errors:
        print('-', e)
    sys.exit(1)
print('V1 data validation passed.')
