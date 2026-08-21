# GemVerse Archive Transfer Gap Register

**Version:** 1.0  
**Date:** 19 August 2026 (AEST)  
**Status:** Active handover stewardship record  
**Purpose:** Identify which records exist in the supplied `Gemversezip.zip` archive but are not present as active shared project files.  
**Change policy:** Informational and additive. This register does not copy, supersede, or approve any archived record.

## Scope

The active shared project workspace contains the seven core governance files required for session continuity. The uploaded archive is substantially broader and contains product, asset, technical, and handover records that are not active shared files. This gap is important because the current `ScanMe.md` rule treats active shared files as the live assistant-readable workspace.

> **Interpretation:** A file’s absence from the active workspace does not invalidate the archived evidence. It means that the material should not be treated as a current active source until it is deliberately reviewed, versioned, and added through the project-file workflow.

## Core Governance Baseline

| Record | Active shared workspace | Archive | Comparison result | Working treatment |
|---|---|---|---|---|
| `ScanMe.md` | Present | Present | Byte-identical | Active workflow source. |
| `SESSION-LOG.md` | Present | Present | Active copy has a newer 19 August continuity entry | Active continuity source. |
| `NEXT_PRIORITIES.md` | Present | Present | Byte-identical | Active priority source. |
| `DECISION_LOG.md` | Present | Present | Byte-identical | Active decision source, subject to known stale/contradictory status records. |
| `01-canon-map.md` | Present | Present | Byte-identical | Active canon baseline for consistently corroborated locked foundations. |
| `02-conflicts-log.md` | Present | Present | Byte-identical | Active conflict evidence; not a sole source for closure where internal contradictions exist. |
| `RISK_REGISTER.md` | Present | Present | Byte-identical | Active risk source. |

## High-Priority Archived Records Not Active in Shared Workspace

| Archived record | Why it matters | Current status | Safe next action |
|---|---|---|---|
| `asset-registry.md` | Holds transferred-asset status, visual canon risks, and multiple unresolved decision references. | **Not active** | Review and add only as a clearly dated, non-destructive import after creator/maintainer approval. |
| `LAUNCH_READINESS_CHECKLIST.md` | Defines explicit Arena first-slice release gates, all currently unchecked. | **Not active** | Add as an imported release-control record only after confirming it remains the desired active checklist. |
| `technical-architecture-draft-20260804.md` | Documents intended Construct 3/platform/data architecture. | **Not active** | Preserve as draft reference; do not rely on it as proof of an implemented architecture. |
| `construct3-event-sheet-specs.md` | Describes proposed puzzle event sheets and terminology. | **Not active** | Add only after checking creator-gated mechanics terminology. |
| `mvp-scope-document-draft-20260804.md` | Contains Arena MVP scope assumptions and roster references. | **Not active** | Keep as archive evidence until companion/realm decision conflicts are reconciled. |
| `guardian_role_bible_volume_1.md` | Draft Guardian framing and system detail. | **Not active** | Import only as a `Draft` record; do not treat an alleged canon/proposal split as delivered. |
| `GemVerse_AI_Handover.md` | Earlier handover narrative. | **Not active** | Preserve as historical handover evidence, not a current authority source. |

## Other Archived Materials Requiring Deliberate Review

| Group | Examples | Stewardship requirement |
|---|---|---|
| Canon and lore | Book of Harmony, First Harmony, Five Wounds, Crystal Network, Realm packets | Verify status and dependent conflicts before activation. |
| Product and systems | Puzzle catalog, Harmony Index, community system, monetization design, technical drafts | Label as draft/proposed unless a current creator decision confirms otherwise. |
| Assets and visual references | Companion, Arena, and realm image assets; visual framing notes | Preserve provenance and transferred/approved distinction. |
| Historical packages | Handover v1, handover v2, duplicate and dated drafts | Retain for audit; do not replace current files without a mapping record. |
| Implementation references | Construct 3 specs, PRS Console README, run/setup scripts | Treat as specifications or administrative artifacts; no runnable source is presently active. |

## Activation Criteria for an Archived File

Before an archived file is added to the active shared workspace, record the following:

| Criterion | Required evidence |
|---|---|
| Provenance | Original archive path and, where known, version/date. |
| Intended active role | Canon, decision, asset registry, technical draft, reference, or archive. |
| Authority/status | Locked, Draft, Proposed, Transferred, Flagged, or Historical. |
| Dependency review | Any decisions, risks, assets, or other documents it depends on. |
| Conflict check | Whether it contradicts the active canon map, decision log, conflict log, or risk register. |
| Registration note | A dated session-log entry and a project-file configuration update. |

## Explicitly Not Performed

No archived record was copied into the active workspace by this assessment. No prior version was deleted, no file was renamed, no canon state was changed, and no asset was marked approved.

## Recommended Autonomous Next Work

Maintain this register while preparing neutral decision briefs and a source-to-archive inventory. When an authoritative creator-approved decision snapshot exists, update the corresponding active governance records in a single traceable change set.

## References

[1]: `Gemversezip.zip` — supplied project archive
[2]: `ScanMe.md` — active shared-workspace scan rules
[3]: `SESSION-LOG.md` — active continuity record
[4]: `DECISION_LOG.md` — active decision register
[5]: `01-canon-map.md` — active canon map
[6]: `02-conflicts-log.md` — active conflict record
[7]: `RISK_REGISTER.md` — active risk register
