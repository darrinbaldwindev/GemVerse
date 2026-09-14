# Vertical Batch Adoption

This repository adopts the portfolio-wide canonical batch standard maintained in `darrinbaldwindev/Overseer` while preserving GemVerse's established `docs/overseer/VERTICAL_BATCH_*.md` history.

Read in order before every vertical execution cycle:
1. `darrinbaldwindev/Overseer/.overseer/doctrine/PORTFOLIO-BATCH-ENGINE.md`
2. `darrinbaldwindev/Overseer/.overseer/profiles/PROJECT-BATCH-PROFILES.md` — GemVerse profile
3. `darrinbaldwindev/Overseer/.overseer/doctrine/VERTICAL-BATCH-EXECUTION.md`
4. current GemVerse vertical batch/history under `docs/overseer/`
5. current repo/PR/issue/CI evidence and Overseer #49.

The central engine is the procedure. The project profile is the customization layer. Existing GemVerse batch files remain project state/history, not a fork of the common procedure. Central engine/profile changes apply on the next fresh cycle.

Owner `cont` / `continue autonomously` triggers the full fresh-scan → reconcile → execute → verify → fresh-scan → replenish → durable-log cycle.