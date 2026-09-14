# Arena Source Intake Manifest

Status date: 2026-09-09
Issue: #3

Purpose: prepare deterministic intake for the missing Construct 3 source without inventing game logic, canon, assets, or creator decisions.

## Artifact classes

Each incoming item must be classified as exactly one of:
- VERIFIED — directly inspected current source/artifact
- REFERENCE-ONLY — useful context but not implementation authority
- STALE — superseded/outdated
- CONFLICTED — contradictory evidence exists
- MISSING — required artifact not present

## Required Construct 3 intake

| Artifact | Required | Current state | Intake checks |
|---|---:|---|---|
| Project file(s) | yes | MISSING | version, project identity, last modified, export compatibility |
| Layout/scene files | yes | MISSING | names, entry scene, transitions, object dependencies |
| Event sheets | yes | MISSING | sheet map, include relationships, unresolved decision dependencies |
| UI strings/copy | yes | MISSING | canon source, localization readiness, accessibility labels |
| Sprite/image/audio assets | yes | MISSING | provenance, licence, filename map, dimensions/formats |
| Save/data variables | yes | MISSING | variable list, persistence behavior, schema/versioning |
| Export/build config | yes | MISSING | target platforms, plugins/addons, build settings |
| External dependencies | yes | MISSING | plugin/addon name, version, licence/source |
| Accessibility settings | yes | MISSING | keyboard/touch, contrast, text sizing, motion/audio alternatives |
| Privacy/analytics hooks | if present | MISSING | provider, data collected, environment, consent boundary |

## Creator-decision blockers

Do not implement any mechanic, copy, progression, economy, Harmony Index behavior, moderation behavior or Arena rule whose controlling decision is unresolved. Every such dependency must remain explicitly BLOCKED with its decision reference.

## Evidence-pack skeleton

When source arrives, produce:
1. environment/tool-version record
2. reproducible build log
3. layout/scene map
4. event-sheet dependency map
5. canon-copy audit
6. asset provenance/licensing table
7. accessibility review
8. save/load behavior report
9. privacy/dependency inventory
10. known-issues register

## Deterministic first verification path

`source intake → artifact classification → dependency check → unresolved-canon gate → clean internal build → entry-scene launch → bounded Arena navigation smoke test → save/load smoke test (if present) → evidence pack`

A successful build alone is not release readiness.

## Guardrails

No invented source, canon, assets, mechanics, progression, monetization, analytics, moderation changes, Harmony Index changes, live player data, store settings or release claims are authorised by this manifest.
