#!/usr/bin/env python3
"""Scan likely player-facing Godot files for placeholder indicators.

Use from the actual Godot project root:
    python3 agent_loop_scripts/v1_no_placeholder_scan.py
"""
from pathlib import Path
import re

PAT = re.compile(r"placeholder|TODO|stub|dummy|temp|not implemented|missing texture", re.I)
SKIP_DIRS = {'.git', 'docs', 'pdfs', 'prompts', 'agent_loop_scripts'}
CHECK_EXT = {'.gd', '.tscn', '.tres', '.json', '.cfg', '.godot', '.import'}

hits = []
for p in Path('.').rglob('*'):
    if any(part in SKIP_DIRS for part in p.parts):
        continue
    if not p.is_file() or p.suffix not in CHECK_EXT:
        continue
    try:
        text = p.read_text(encoding='utf-8', errors='ignore')
    except Exception:
        continue
    for i, line in enumerate(text.splitlines(), 1):
        if PAT.search(line):
            hits.append((str(p), i, line.strip()))

if hits:
    print('PLAYER-FACING PLACEHOLDER CANDIDATES FOUND:')
    for path, line, text in hits:
        print(f'{path}:{line}: {text}')
    raise SystemExit(1)
else:
    print('No player-facing placeholder indicators found in scanned files.')
