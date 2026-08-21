# GemVerse Arena First-Slice Implementation Readiness Matrix

**Version:** 1.0  
**Date:** 19 August 2026 (AEST)  
**Status:** Pre-implementation acceptance-criteria draft  
**Scope:** Arena Realm first slice, based on active governance records and the archived launch-readiness checklist.  
**Important:** This is not a build plan, implementation confirmation, or release approval. The Construct 3 source project was not supplied.

## Purpose

This matrix converts the current design and governance evidence into small, testable conditions for any future Arena first-slice implementation. It creates a common handoff language for the creator, narrative/design, visual, QA, and implementation roles while avoiding unapproved mechanics or scope commitments.

## Current Readiness

| Dimension | Status | Evidence available | What is still missing |
|---|---|---|---|
| Core product framing | **Ready for reference** | Arena is a civic/community hub; Guardian is a contributor; Kael’s civic reframe is consistently recorded. | Final narrative copy and implemented dialogue. |
| Canon decision closure | **Blocked** | Decision reconciliation packet records disputed items. | Creator-confirmed resolution snapshot and synchronized governance files. |
| Game source | **Missing** | Construct 3 is documented as intended engine. | Project source, event sheets, assets, export config, test build. |
| UI/gameplay evidence | **Unverified** | Mockups and specifications exist in archive. | Actual scenes, strings, state logic, and accessibility settings. |
| Asset readiness | **Unverified** | Transferred visual references and hash inventory exist. | Rights/provenance, approval, optimized production assets, alt-text/accessibility metadata. |
| Release readiness | **Not ready** | Archive launch checklist lists the required gates. | All Phase 0–5 evidence, builds, test results, and approved content. |

## First-Slice Definition of Done — Draft

The first slice may be presented as ready for internal verification only when every applicable row has recorded evidence. Items requiring creator approval must remain blocked until the approval is documented.

| Area | Acceptance criterion | Evidence required | Status now |
|---|---|---|---|
| Entry | A Guardian can enter an Arena civic arrival space with clear orientation and non-combat framing. | Screen/video capture plus source/scene path. | Unverified. |
| Tone | Player-facing Arena copy contains no villain, combat, chosen-one, power-fantasy, urgency/scarcity, or energy-gating language. | Versioned string/dialogue audit. | Unverified. |
| Kael | Kael is described through civic contribution, organization, restoration, or community stewardship—not martial achievement. | Dialogue/script audit and visual-framing review. | Unverified. |
| Companion role | Spark or any featured companion appears as a partner/witness, not a puzzle-solving tool or collectible stat unit. | Dialogue, UI, and interaction audit. | Unverified. |
| Puzzle purpose | The first playable interaction has an in-world civilizational purpose and makes clear what it helps understand, reconnect, or restore. | Event-sheet/design note cross-reference and recorded playtest observation. | Unverified. |
| Mechanics terminology | Any special-gem, guidance, combo, scoring, or resource language follows a confirmed creator decision. | Decision ID plus UI/event-sheet audit. | Blocked by DR-003. |
| Resources | No resource bar blocks or meters access to play. Any collection/cosmetic resource is explained clearly and cannot be mistaken for stamina/energy gating. | UI behavior test and copy audit. | Unverified. |
| Progression | Progress feedback recognizes contribution/understanding instead of rank, dominance, or power accumulation. | UI copy, state logic, and playtest evidence. | Unverified. |
| Accessibility foundation | Text is readable, color meaning is not the sole puzzle signal, essential audio has an alternative cue, and reduced-motion/custom-control needs are considered. | Accessibility test notes and settings review. | Unverified. |
| Local resilience | Core first-slice progress can be saved and restored without an assumed cloud dependency. | Save/load test and documented data location. | Unverified. |
| Privacy | No player data collection, analytics, or third-party SDK is added without an explicit approved requirement and privacy review. | Dependency inventory and data-flow note. | Unverified. |

## Canon Guardrails for Implementation Review

| Review category | Reject or flag immediately | Preferred implementation language |
|---|---|---|
| Threat framing | Enemy, villain, battle, attack, defeat, boss, darkness spreading | Drift, fracture, reconnection, restoration, community care |
| Player framing | Hero, savior, chosen one, destiny, domination | Guardian, contributor, participant, steward, witness |
| Mechanics | Power-up, destruction, blast, damage, pay-to-win, energy gate, loot box | Guidance, resonance, reveal, attunement, optional cosmetic, accessible support |
| Companion framing | Pet, collectible, equip, ability/stat unit, tool | Partner, witness, memory-keeper, friend, relationship |
| Progress feedback | Victory, conquer, rank supremacy, strength escalation | Restoration complete, contribution recorded, understanding deepened |

## Required Source-to-Spec Mapping on Arrival

When the implementation archive is supplied, create the following mapping before editing code/event sheets:

| Source element | Required mapping target |
|---|---|
| Construct 3 scene/project file | Arena first-arrival scene, main menu, gameplay, story, and navigation paths. |
| Event sheet | Puzzle type, intended in-world purpose, unresolved-decision dependencies, and test case. |
| UI string/data table | Canon audit status, copy owner, and decision source. |
| Asset reference | File path, source/rights status, canon relationship, and approved/placeholder status. |
| Data/save variable | Player-facing meaning, privacy impact, reset behavior, and persistence scope. |
| External dependency | Vendor, purpose, data transmitted, owner, configuration placeholder, and approval status. |

## Test Evidence Pack — Draft Structure

```text
evidence/
├── environment.md
├── build-log.txt
├── scene-map.md
├── event-sheet-map.md
├── canon-copy-audit.md
├── asset-provenance-audit.md
├── accessibility-test-notes.md
├── save-load-test.md
├── privacy-and-dependency-inventory.md
└── known-issues.md
```

## Explicit Boundaries

This readiness matrix does not authorize changes to the Harmony Index, progression rules, monetization, moderation, analytics, live player data, store release settings, or platform/account configurations. It also does not settle the decision-reconciliation items recorded in `10_DECISION_RECONCILIATION_PACKET_20260819.md`.

## References

[1]: `LAUNCH_READINESS_CHECKLIST.md` (archive-only at time of this record)
[2]: `01-canon-map.md`
[3]: `02-conflicts-log.md`
[4]: `DECISION_LOG.md`
[5]: `RISK_REGISTER.md`
[6]: `10_DECISION_RECONCILIATION_PACKET_20260819.md`
[7]: `03_Engineering_Handover_Intake_and_Readiness_20260819.md` (external handover working output)
