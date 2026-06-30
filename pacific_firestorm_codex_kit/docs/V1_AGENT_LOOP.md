# V1 Agent Loop

This file defines the loops the coding agent must follow. The goal is a complete V1 game, not a partial implementation.

## Outer loop - start to finish

The agent repeats this cycle until V1 gates pass:

1. Inspect current repo state.
2. Compare repo against `docs/V1_DEFINITION_OF_DONE.md`.
3. Identify the highest-priority missing gate.
4. Make the smallest complete implementation that moves the project toward V1.
5. Run checks.
6. Fix errors.
7. Update docs/test results.
8. Continue to the next missing gate.

The agent should not stop merely because one feature works. It stops only when V1 is complete or a true blocker prevents execution.

## Inner coding loop

For every task:

1. Read relevant files.
2. Create a short plan.
3. Modify code/assets/data.
4. Run Godot import/check/run commands when available.
5. Run project-specific tests.
6. Fix parse errors, missing paths, broken signals, collision issues.
7. Manually reason through acceptance criteria.
8. Record results in `docs/TEST_RESULTS_V1.md`.

## Error-fix loop

When an error appears:

1. Copy exact error.
2. Identify file and line.
3. Fix smallest root cause.
4. Re-run the same check.
5. Repeat until the error is gone.
6. Only then move on.

Do not rewrite unrelated systems while fixing one error.

## No-placeholder loop

Before V1 release:

1. Search the repo for player-facing placeholder indicators:
   - placeholder
   - temp
   - TODO
   - stub
   - dummy
   - test asset
   - not implemented
2. Decide which occurrences are documentation-only and which affect the game.
3. Remove or replace all player-facing placeholder content.
4. Run the game and visually inspect the playable route.
5. Create `docs/NO_PLACEHOLDER_AUDIT_V1.md`.

## Campaign completion loop

For each mission:

1. Confirm mission can start.
2. Confirm waves spawn.
3. Confirm boss or set-piece appears.
4. Confirm mission can be completed.
5. Confirm next mission loads.
6. Confirm death/game over/restart works inside that mission.
7. Record result in `docs/TEST_RESULTS_V1.md`.

## Release loop

1. Freeze V1 feature list.
2. Run all gates.
3. Fix failures.
4. Export build.
5. Package release.
6. Write release notes.
7. Write final audit.
8. Stop.

## Blocker rule

The agent may stop early only if blocked by something it cannot reasonably solve, such as:
- Godot executable is not installed in the environment.
- Export templates are missing and cannot be downloaded.
- Required file permissions are unavailable.
- A requested external asset is absent and cannot be generated procedurally.

If blocked, the agent must create:
- `BLOCKERS.md`
- exact missing requirement
- exact command that failed
- what the user must provide
- what work was completed anyway
