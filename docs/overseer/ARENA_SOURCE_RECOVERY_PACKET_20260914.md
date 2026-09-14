# GemVerse Arena Source Recovery Packet — 2026-09-14 AEST

**Purpose:** Define the exact evidence needed to move GemVerse Arena implementation readiness from AMBER/RED toward GREEN without recreating missing source from assumptions.

## Accepted source classes

### A. Native Construct source
Required evidence:
- original source location and owner/custodian;
- `.c3p` and/or full Construct project directory;
- `project.json` or equivalent project metadata where applicable;
- event sheets and layouts;
- referenced asset set;
- Construct version/runtime/export target;
- source hash or immutable commit/ref;
- known missing dependencies;
- build/export/run instructions.

### B. Browser vertical-slice source
Required evidence:
- authoritative repository or source directory;
- source commit/hash;
- dependency/application manifests;
- lockfile if used;
- runtime/toolchain versions;
- build command;
- run command;
- test command and expected result;
- asset/license provenance where relevant;
- known issues.

### C. Historical migration/parity contract
If `CONSTRUCT_3_MIGRATION.md` or an equivalent migration record is recovered:
- verify provenance and date;
- identify source and target implementation versions;
- map each Arena interaction/puzzle to corresponding Construct layout/event sheet;
- separate aspirational requirements from tested parity results.

## Minimum verification sequence

1. Receipt — identify provenance, immutable ref/hash, file inventory, and toolchain.
2. Integrity — confirm source is internally consistent and required files are present.
3. Reproduction — perform a clean build/export/run from documented steps.
4. Functional smoke test — first arrival, navigation, representative puzzle flow, completion/recovery path.
5. Mapping — compare behavior to Arena readiness matrix and locked puzzle/canon design.
6. Safety review — privacy, accessibility, non-combat/restorative framing, no hidden live-service dependencies.
7. Evidence receipt — retain commands/results/artifact references and verifier identity.

## Fail-closed conditions

Remain AMBER/RED if any of the following apply:
- source exists only as screenshots, prose, or chat claims;
- executable artifact exists without reproducible source/build instructions;
- source cannot be tied to an immutable version;
- required dependencies are unavailable;
- build/run fails and failure is unexplained;
- implementation behavior materially diverges from locked canon/design without creator approval;
- verifier cannot independently reproduce claimed behavior.

## Recovery search targets

Highest-value targets to locate externally or in prior machines/workspaces:
- `/home/ubuntu/gemverse-arena`;
- `CONSTRUCT_3_MIGRATION.md`;
- `.c3p` files;
- `project.json`;
- event-sheet exports/spec assets;
- `package.json` and lockfiles;
- README/runbook describing Arena build/run/test;
- archived ZIPs containing executable source rather than documentation-only material.

## Prohibition

Do not reconstruct a new Arena codebase and label it as the recovered implementation. A newly created implementation may later be proposed as a replacement build, but it must remain explicitly distinct from historical source recovery.
