# GemVerse Asset and Duplicate Stewardship Register

**Version:** 1.0  
**Date:** 19 August 2026 (AEST)  
**Status:** Inventory and stewardship record  
**Scope:** Visual assets and duplicate document families visible in the active shared workspace and supplied archive.  
**Change policy:** Read-only classification. No asset approval, deletion, renaming, or canonical claim is made by this register.

## Stewardship Rules Applied

Each asset is classified by visible provenance, intended reference use, duplication state, and review need. A transferred or locally present asset is **not** treated as approved final art, confirmed canon, or proof of rights ownership. No asset should be used in production or promotional material until source ownership/licensing, creator approval, and canon alignment are documented.

| Status | Meaning |
|---|---|
| `Transferred / unreviewed` | Present in the project files or archive, but not approved for production use. |
| `Reference only` | May support internal discussion or visual direction; not approved art. |
| `Duplicate group` | Byte-identical copies that should be retained until an approved archive/retention decision is made. |
| `Classification needed` | The relationship to GemVerse, intended use, provenance, or rights is not documented. |

## Active Shared Workspace — Visual Asset Inventory

| Asset group | Exact filenames | Hash group | Source/provenance | Intended use inferred from filename | Current safe status |
|---|---|---|---|---|---|
| Lantern & Archive first-arrival concept | `Realistic fantasy Lantern site and Archive corner as GemVerse’s first arrival space.png`; `...-2.png`; `...-3.png` | `6469e5f5…084f4` (3 identical files) | Active shared workspace | Arena first-arrival / Lantern site / Archive-corner visual reference | `Transferred / unreviewed`; `Duplicate group` |
| Sky Citadel observation-terrace concept | `Realistic fantasy Sky Citadel observation terrace as a realm of discovery.png`; `...-2.png` | `32c811f4…03728` (2 identical files) | Active shared workspace | Sky Citadel discovery-oriented visual reference | `Transferred / unreviewed`; `Duplicate group` |
| Starter Console mockup | Four `Hero mockup of the Starter Console...` PNG variants | `60148370…a2590` (4 identical files) | Active shared workspace and supplied archive | Possible documentation/tooling UI reference; GemVerse relationship is not documented | `Classification needed`; `Duplicate group` |

## Supplied Archive — Additional Visual Assets

| Asset | Hash | Source/provenance | Intended use inferred from filename | Current safe status |
|---|---|---|---|---|
| `Four GemVerse character illustrations Guardian, Companion, Kael, and Arena Lantern Keeper in civic, restorative settings.png` | `65513e84…6b93` | Supplied `Gemversezip.zip` archive | Internal character/role visual-direction reference | `Transferred / unreviewed`; do not treat as approved character art. |
| `Lineup illustration of GemVerse Guardian, Kael, and three Companions in the Arena civic square.png` | `d4de1ab2…f406` | Supplied `Gemversezip.zip` archive | Arena civic-square relationship/composition reference | `Transferred / unreviewed`; review against Kael/companion canon before use. |

## Duplicate Document Families in the Archive

The archive contains numerous byte-identical numbered copies of working documents. These copies are historical evidence, not automatically redundant content. They must not be deleted or overwritten without a documented retention decision.

| Duplicate family | Verified condition | Safe treatment |
|---|---|---|
| `01-canon-map` and `(1)` variant | Byte-identical | Keep the unnumbered copy as the active archival reference; retain numbered copy as historical duplicate. |
| Tier 1 canon files `03`–`09` and `(1)` variants | Byte-identical | Preserve; do not silently remove. |
| Arena/companion/implementation packets and `(1)` variants | Byte-identical | Preserve until a controlled archive move is authorized. |
| `puzzle-meta-proposals` base, `(1)`, `(2)` | Byte-identical | Preserve all copies; flag for later archive consolidation. |
| `GemVerse_AI_Handover_Document` variants | Byte-identical | Preserve for handover provenance; do not use as the current authority without a status check. |
| Four Starter Console images | Byte-identical | Retain all pending a creator/maintainer decision on relevance and archival location. |
| Lantern & Archive concept images | Byte-identical | Retain all pending asset registry/provenance review. |
| Sky Citadel concept images | Byte-identical | Retain all pending asset registry/provenance review. |

## Required Asset Metadata Before Use

| Field | Required value |
|---|---|
| Source | Originating creator, tool, contributor, or acquisition path. |
| Rights/permission | Ownership, license, internal-use restriction, and attribution requirement where applicable. |
| Intended use | Concept reference, marketing, UI, in-game art, temporary placeholder, or archive only. |
| Canon relationship | Related realm, companion, character, system, or not canon-adjacent. |
| Status | Concept, Draft, Transferred, Flagged, Approved, or Archived. |
| Version/provenance | Original filename, date received, derivative relationships, and duplicate group hash. |
| Accessibility note | Descriptive alt text and whether color, motion, or text creates an accessibility concern. |

## Safe Actions Completed

- Calculated exact duplicate groups using file hashes.
- Separated active shared-workspace assets from archive-only assets.
- Recorded inferred intended reference use without labeling any asset approved or canonical.
- Preserved all duplicate files and historical variants unchanged.

## Deferred Actions

- No asset was removed, renamed, copied, edited, or marked approved.
- No ownership, license, artist approval, or final-production status was assumed.
- No visual asset was used to settle a character, realm, roster, or game-mechanic decision.

## Recommended Next Autonomous Work

Create a dedicated asset-intake form and archive manifest for newly uploaded source material. When the archived `asset-registry.md` is deliberately activated, merge this hash-level duplicate data into that registry through a versioned, reviewable update.

## References

[1]: Active shared workspace visual-asset hash manifest, 19 August 2026
[2]: Supplied `Gemversezip.zip` visual-asset hash manifest, 19 August 2026
[3]: `00_ARCHIVE_TRANSFER_GAP_REGISTER_20260819.md`
[4]: `02-conflicts-log.md`
[5]: `RISK_REGISTER.md`
