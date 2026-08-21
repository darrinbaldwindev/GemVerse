# Project Next Priorities

## Project Metadata
- **Project Name:** GemVerse
- **Version:** v1.1
- **Created:** 2026-08-04
- **Last Updated:** 2026-08-19
- **Maintained By:** Assistant(s) / Human
- **Source of Truth Location:** This file in project root
- **Review Cadence:** Start of each session / after major milestones

---

## Purpose
Define the **execution order** for upcoming work. This is the "what's next" companion to `SESSION-LOG.md` (what happened), `DECISION_LOG.md` (what's decided), and `01-canon-map.md` (canon authority).

**Reading Order:** After `ScanMe.md`, `SESSION-LOG.md`, `DECISION_LOG.md`, `01-canon-map.md` when planning a session.

---

## Priority Framework

| Priority | Meaning | SLA |
|----------|---------|-----|
| **P0 — Blocking** | Creator-only decisions that unblock all dependent work | Immediate |
| **P1 — Critical** | Canon stability, conflict resolution, asset governance | This session |
| **P2 — High** | Packet production (Companion, Realm), puzzle catalog finalization | Next 1–2 sessions |
| **P3 — Medium** | Visual framing, onboarding, technical verification | Backlog |
| **P4 — Low** | Exploratory, future realms, extended lore | Icebox |

---

## Current Priority Stack (Ranked)

### Resolved Creator Decisions (2026-08-04; reconciled 2026-08-19)
| ID | Confirmed Outcome | Former Blocking Area | Authority | Status |
|----|-------------------|----------------------|-----------|--------|
| P0-001 | “Dark” gem terminology replaced by **Dusk** (mechanical/UI) and **Twilight** (narrative/realm). | Mechanics, visuals, asset registry | `02-conflicts-log.md` Conflict 7 | Resolved |
| P0-002 | Lumi, Ember, and Frosty are launch companions; launch roster totals 11. | Content production, asset needs | `02-conflicts-log.md` Conflict 6 | Resolved |
| P0-003 | Puzzle mechanics are canon-safe puzzle tools and Harmony Flow, not power-ups or destructive combos. | Game mechanics, UI framing | `02-conflicts-log.md` Conflict 8 | Resolved |
| P0-004 | Forestkin is common usage; Verdankin is formal/scholarly usage. | Citizen/companion packets | `02-conflicts-log.md` Conflict 9 | Resolved |
| P0-005 | Guardian canon/proposal split is complete; core role is locked and exploratory mechanics remain proposals. | Guardian system canonization | `02-conflicts-log.md` Conflict 10 | Resolved |

### P1 — Critical
| ID | Item | Description | Blocking | Owner | Target |
|----|------|-------------|----------|-------|--------|
| P1-001 | Apply locked First Harmony duration/Threshold model to dependent drafts | Era framing consistency | Tier 1 canon stability | Assistant | Planned verification |
| P1-002 | Apply Solana authorship and Principles 10/12 to dependent Book of Harmony materials | Canon depth for core text | Tier 1 canon stability | Assistant | Planned verification |
| P1-003 | Audit for retired tagline variants and retain only approved brand lines | Brand messaging consistency | Marketing, UI copy | Assistant | Planned verification |
| P1-004 | Apply Memory Ocean naming to any legacy “Heart of the Core” references | Environment naming consistency | Realm packets, visual assets | Assistant | Planned verification |
| P1-005 | Create or obtain a Construct 3 implementation for parity review | A playable browser vertical slice now exists at `/home/ubuntu/gemverse-arena`, but the native Construct project remains absent. Compare any future Construct build against `CONSTRUCT_3_MIGRATION.md`. | Technical implementation | Assistant / Creator | Requires Construct project or implementation decision |
| P1-006 | Audit 30+ unpreviewed Space files | Hidden critical context | Governance, completeness | Assistant | Next session |
| P1-007 | Verify generated `output/` artifacts integration | 7 files may be orphaned | Continuity integrity | Assistant | Next session |

### P2 — High
| ID | Item | Description | Blocking | Owner | Target |
|----|------|-------------|----------|-------|--------|
| P2-001 | Complete Companion Encyclopedia (Spark, Frostpaw, Verdant, Nimbus) | Tier 3 production | Launch content | Assistant | 1–2 sessions |
| P2-002 | Draft Sky Citadel Realm Packet | Tier 2 production (Wound of Discovery) | Realm expansion | Assistant | 2 sessions |
| P2-003 | Draft Frozen Expanse Realm Packet | Tier 2 production (Wound of Memory) | Realm expansion | Assistant | 2 sessions |
| P2-004 | Apply confirmed Dusk/Twilight terminology and canon-safe tool mapping to the Puzzle Catalog | Canon is resolved; dependent content needs reconciliation | Mechanics, visuals | Assistant | 1 session |
| P2-005 | Build Wounds–Realms–Companions–Puzzles matrix using the locked Five Wounds model | Cross-system coherence | All production | Assistant | 2 sessions |
| P2-006 | Arena first slice implementation checklist | Production readiness | Arena launch | Assistant | 1 session |

### P3 — Medium
| ID | Item | Description | Blocking | Owner | Target |
|----|------|-------------|----------|-------|--------|
| P3-001 | Crystal Forest Realm Packet (existing draft → final) | Tier 2 production | Realm expansion | Assistant | 2 sessions |
| P3-002 | Arena onboarding environment visual notes → final | Visual framing | Player experience | Assistant | 1 session |
| P3-003 | Arena festival visual notes → final | Visual framing | Live ops | Assistant | 1 session |
| P3-004 | Companion Visual Bible Vol 1/2 review | Asset canonization | Art direction | Assistant | 1 session |
| P3-005 | Citizen Encyclopedia (6 named citizens) | Tier 3 production | World depth | Assistant | 2 sessions |

### P4 — Low / Exploratory
| ID | Item | Description | Blocking | Owner | Target |
|----|------|-------------|----------|-------|--------|
| P4-001 | Ember Depths Realm Packet (draft exists) | Tier 2 | Future realm | Assistant | Icebox |
| P4-002 | Celestial Nexus Realm Packet (draft exists) | Tier 2 | Future realm | Assistant | Icebox |
| P4-003 | Legacy Realm Packet (draft exists) | Tier 2 | Future realm | Assistant | Icebox |
| P4-004 | Twilight Frontier Realm Packet (draft exists) | Tier 2 | Future realm | Assistant | Icebox |
| P4-005 | Open Mysteries deepening (Memory Ocean, Missing Realm, etc.) | Narrative | Long-term lore | Assistant | Icebox |
| P4-006 | Transfer tool website documentation/verification | Ops | Tooling | Human | Icebox |

---

## Work Queue (Session-Ready Tasks)

### Next Session Recommended Tasks
Based on current `SESSION-LOG.md` unresolved items and this priority stack:

| Task | Priority | Est. Effort | Dependencies |
|------|----------|-------------|--------------|
| 1. **Reconcile downstream materials**: Apply confirmed Conflict Log decisions to the Puzzle Catalog, companion records, brand copy, and relevant Realm packets. | P1 | Assistant work | Active continuity baseline |
| 2. **Verify decision traceability**: Confirm that every dependent document reflects the locked resolutions without overwriting drafts prematurely. | P1 | Assistant work | Active continuity baseline |
| 3. Verify the actual Construct 3 project against the recovered eight-event-sheet specification | P1 | 2–3 hrs | Access to Construct project/export or source repository |
| 4. Expand repository inventory: audit all 50+ Space files | P1 | 1–2 hrs | File access |
| 5. Verify 7 generated `output/` artifacts uploaded to Space | P1 | 30 min | File access |

### Following Session Candidates (Post Creator Decisions)
| Task | Priority | Est. Effort | Dependencies |
|------|----------|-------------|--------------|
| 6. Update `puzzle-catalog.md` Section 3 with the confirmed Dusk/Twilight terminology and puzzle-tool reframing | P2 | 1 hr | Canon resolution verified |
| 7. Complete Companion Encyclopedia for 4 companions | P2 | 3–4 hrs | P0-002 resolved |
| 8. Draft Sky Citadel Realm Packet (Wound of Discovery) | P2 | 3–4 hrs | P1-001, P1-002 |
| 9. Draft Frozen Expanse Realm Packet (Wound of Memory) | P2 | 3–4 hrs | P1-001, P1-002 |
| 10. Build Wounds–Realms–Companions–Puzzles matrix | P2 | 2–3 hrs | P2-001, P2-002, P2-003 |

---

## Roadmap (from `tier-roadmap-tracker.md`)

| Tier | Theme | Status | Key Deliverables |
|------|-------|--------|------------------|
| **Tier 1** | Foundational Canon | **Stable** | Book of Harmony, First Harmony, Five Wounds, Crystal Network, Lantern Network, Restoration Era |
| **Tier 2** | Realm Packets | **Pending** | Crystal Forest (draft), Sky Citadel, Frozen Expanse, Ember Depths, Celestial Nexus, Legacy, Twilight Frontier |
| **Tier 3** | Companion Packets | **In Progress** | Spark, Frostpaw, Verdant, Nimbus (drafts); Lumi, Ember, Frosty (confirmed launch companions; packets pending) |
| **Tier 4** | Citizen Life | **Draft** | 6 named citizens, Paths lens |
| **Tier 5** | Mystery Governance | **Draft** | Open Mysteries, governance map |
| **Tier 6** | Game Systems | **Blocked** | Puzzle catalog, gem system, Construct 3 alignment |

---

## Completed Priorities (Archive)

| ID | Item | Completed | Outcome |
|----|------|-----------|---------|
| DONE-001 | Create `SESSION-LOG.md` | 2026-08-04 | Migrated full history from `gemverse-session-continuity-log.md` |
| DONE-002 | Create `DECISION_LOG.md` | 2026-08-04 | Consolidated canon-map, conflicts-log, session-log |
| DONE-003 | Create `RISK_REGISTER.md` | 2026-08-04 | Identified 18 active risks |
| DONE-004 | Create `NEXT_PRIORITIES.md` | 2026-08-04 | This file |
| DONE-005 | Kael reframe resolved (Option A) | 2026-08-04 | Arena narrative unblocked |
| DONE-006 | Update `ScanMe.md` to prioritize `SESSION-LOG.md` | 2026-08-04 | Priority #2 after ScanMe |

---

## Maintenance Rules
1. **Re-rank at session start** — priorities shift; update this file
2. **Move completed items to Archive** — don't delete
3. **Link to decisions** — when a priority becomes a decision, cross-ref `DECISION_LOG.md`
4. **Link to risks** — when a priority mitigates a risk, cross-ref `RISK_REGISTER.md`
5. **Link to canon** — when a priority affects canon, cross-ref `01-canon-map.md` and `02-conflicts-log.md`
6. **Keep filename unchanged** — always `NEXT_PRIORITIES.md`

---

## Change Log
| Date | Version | Changes | Author |
|------|---------|---------|--------|
| 2026-08-04 | v1.0 | Created standardized priorities from tier-roadmap-tracker, session-log, handover docs | Assistant |
| 2026-08-19 | v1.1 | Reconciled stale creator-decision blockers to creator-confirmed Conflict Log outcomes after the creator selected the Conflict Log as authoritative. | Assistant |
| 2026-08-19 | v1.2 | Updated Five Wounds dependent work to use the creator-locked names and descriptors. | Assistant |
| 2026-08-19 | v1.3 | Recorded archive discovery of the eight-event-sheet Construct specification; retained implementation verification as blocked pending executable project evidence. | Assistant |
| 2026-08-19 | v1.4 | Created the playable browser-based Arena vertical slice and a Construct 3 migration contract; native Construct implementation remains unverified. | Assistant |

---

*Template adapted from Amazon `amazon-top-100-next-3-priorities.md` and GemVerse `tier-roadmap-tracker.md`*
