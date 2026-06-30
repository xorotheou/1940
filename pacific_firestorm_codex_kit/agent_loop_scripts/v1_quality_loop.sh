#!/usr/bin/env bash
set -euo pipefail

# Pacific Firestorm V1 quality loop helper.
# This script is intended to be copied into the actual Godot project root.
# It does not guarantee a release by itself; it gives Codex/human testers a repeatable check loop.

ROOT="$(pwd)"
LOG_DIR="$ROOT/docs"
mkdir -p "$LOG_DIR"
LOG="$LOG_DIR/TEST_RESULTS_V1.md"

{
  echo "# V1 Test Results"
  echo ""
  echo "Run time: $(date -Is)"
  echo ""
} > "$LOG"

find_godot() {
  if command -v godot >/dev/null 2>&1; then echo godot; return 0; fi
  if command -v godot4 >/dev/null 2>&1; then echo godot4; return 0; fi
  return 1
}

if GODOT_BIN="$(find_godot)"; then
  echo "Using Godot: $GODOT_BIN" | tee -a "$LOG"
  "$GODOT_BIN" --version | tee -a "$LOG" || true
  echo "" | tee -a "$LOG"

  echo "## Godot help available" >> "$LOG"
  "$GODOT_BIN" --help >/tmp/godot_help.txt 2>&1 || true

  echo "## Project import/load smoke check" | tee -a "$LOG"
  # Different Godot versions support different CLI flags. Keep this conservative.
  "$GODOT_BIN" --headless --path "$ROOT" --quit-after 3 >> "$LOG" 2>&1 || {
    echo "Godot headless load failed. Inspect log above." | tee -a "$LOG"
    exit 1
  }
else
  echo "Godot executable not found. Non-engine checks only." | tee -a "$LOG"
  echo "Create BLOCKERS.md explaining that runtime/export testing requires Godot installation." | tee -a "$LOG"
fi

echo "## Placeholder string scan" | tee -a "$LOG"
# This scan is intentionally broad; docs/prompts may contain these words, but game-facing resources must be reviewed.
grep -RInE "placeholder|TODO|stub|dummy|temp|not implemented" . \
  --exclude-dir=.git \
  --exclude-dir=pdfs \
  --exclude='*.pdf' \
  >> "$LOG" || true

echo "## JSON validity" | tee -a "$LOG"
python3 - <<'PY_INNER_QUALITY' >> "$LOG" 2>&1
import json, pathlib, sys
ok = True
for p in pathlib.Path('.').rglob('*.json'):
    try:
        json.loads(p.read_text(encoding='utf-8'))
        print('OK', p)
    except Exception as e:
        ok = False
        print('FAIL', p, e)
if not ok:
    sys.exit(1)
PY_INNER_QUALITY

echo "Quality loop completed. Review docs/TEST_RESULTS_V1.md" | tee -a "$LOG"
