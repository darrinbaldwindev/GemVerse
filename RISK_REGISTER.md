# Project Risk Register

## Project Metadata
- **Project Name:** GemVerse
- **Register Version:** v1.1
- **Created:** 2026-08-04
- **Last Updated:** 2026-08-19
- **Maintained By:** Assistant(s) / Human
- **Source of Truth Location:** This file in project root
- **Review Cadence:** Per session / at major milestones

---

## Purpose
Capture, assess, and track risks that could impact project delivery, quality, or canon integrity. Each risk has an owner, mitigation, and status.

**Reading Order:** After `ScanMe.md`, `SESSION-LOG.md`, `DECISION_LOG.md`, and `01-canon-map.md` when assessing project health.

---

## Risk Scoring Matrix

| Likelihood | Impact | Score | Priority |
|------------|--------|-------|----------|
| Very High (5) | Critical (5) | 25 | 🔴 **CRITICAL** |
| High (4) | High (4) | 16–20 | 🟠 **HIGH** |
| Medium (3) | Medium (3) | 9–12 | 🟡 **MEDIUM** |
| Low (2) | Low (2) | 4–6 | 🟢 **LOW** |
| Very Low (1) | Very Low (1) | 1–2 | ⚪ **MINIMAL** |

**Priority = Likelihood × Impact**

---

## Active Risks

| ID | Risk Description | Category | Likelihood | Impact | Score | Priority | Owner | Status | Mitigation / Notes | Related Files |
|----|------------------|----------|------------|--------|-------|----------|-------|--------|-------------------|---------------|
| RISK-002 | "Game-ification drift" — outsourced assets use combat/power tropes | Canon/Visuals | 4 | 5 | 20 | 🟠 **HIGH** | Assistant | **Active** | Aggressive filtering via `asset-registry.md` and `canon-risk-report-20260601.md` | `asset-registry.md`, `canon-risk-report-20260601.md` |
| RISK-012 | Executable Construct event-sheet parity remains unverified | Technical/Mechanics | 3 | 4 | 12 | 🟡 **MEDIUM** | Assistant | **Active** | Archive review located a canon-aligned specification for eight event sheets, but no `.c3p`, Construct export, `project.json`, or executable event-sheet assets. Verify against the actual project when access is available. | `construct3-event-sheet-specs.md`, `puzzle-catalog.md`, `GemVerse_AI_Handover.md` |
| RISK-013 | Gem type count discrepancy: Dev Bible shows 7, Art Bible shows 6 | Visuals/Mechanics | 2 | 3 | 6 | 🟢 **LOW** | Assistant | **Monitoring** | Verify final gem set; align with Dark Gem decision | `canon-risk-report-20260601.md`, `puzzle-catalog.md` |
| RISK-014 | 30+ unpreviewed Space files may contain critical context | Governance | 3 | 3 | 9 | 🟡 **MEDIUM** | Assistant | **Active** | Expand repository inventory; audit all files | `SESSION-LOG.md`, `GemVerse_AI_Handover_Document.md` |
| RISK-015 | Duplicate/overlapping Kael decision files (`decision-01-kael-reframe.md` vs `decision-kael-arena-champion-v1.md`) | Governance | 2 | 3 | 6 | 🟢 **LOW** | Assistant | **Monitoring** | Archive older; keep newer as authoritative | `decision-01-kael-reframe.md`, `decision-kael-arena-champion-v1.md` |
| RISK-016 | Generated `output/` artifacts not verified as integrated into Space | Continuity | 3 | 3 | 9 | 🟡 **MEDIUM** | Assistant | **Active** | Verify upload status of 7 generated files | `GemVerse_AI_Handover_Document.md`, `SESSION-LOG.md` |
| RISK-017 | No launch/implementation checklist for Arena first slice | Process/Production | 2 | 4 | 8 | 🟡 **MEDIUM** | Assistant | **Active** | Create checklist based on `implementation-checklist-arena-first-slice-v1.md` | `implementation-checklist-arena-first-slice-v1.md` |
| RISK-018 | Transfer tool website referenced but code/URL/infrastructure unverified | Technical/Ops | 2 | 3 | 6 | 🟢 **LOW** | Human | **Monitoring** | Document if exists; else archive reference | `weekly-brief-template.md`, `GemVerse_AI_Handover_Document.md` |

---

## Resolved / Closed Risks

| ID | Risk Description | Resolution | Date Closed |
|----|------------------|------------|-------------|
| RISK-OLD-001 | No standardized continuity log | Created `SESSION-LOG.md` with full migration from `gemverse-session-continuity-log.md` | 2026-08-04 |
| RISK-OLD-002 | No decision log existed | Created `DECISION_LOG.md` consolidating canon-map, conflicts-log, session-log | 2026-08-04 |
| RISK-OLD-003 | Kael combat framing | Resolved: Option A (Champion of Contribution) applied | 2026-08-04 |
| RISK-OLD-004 | No risk register existed | Created this `RISK_REGISTER.md` | 2026-08-04 |
| RISK-001 | Creator-decision blocker cluster | Closed after creator selected the Conflict Log as authoritative; all eight formerly deferred decisions have recorded creator-confirmed resolutions. | 2026-08-19 |
| RISK-003 | Dark Gem terminology unresolved | Closed: Dusk/Twilight terminology is locked in Conflict 7. | 2026-08-19 |
| RISK-004 | Companion launch list undecided | Closed: Lumi, Ember, and Frosty are locked launch companions in Conflict 6. | 2026-08-19 |
| RISK-005 | Forestkin/Verdankin inconsistency | Closed: common/formal usage split is locked in Conflict 9. | 2026-08-19 |
| RISK-006 | Guardian canon/proposal boundary unclear | Closed: split is locked in Conflict 10. | 2026-08-19 |
| RISK-007 | Puzzle tool/combo framing unresolved | Closed: canon-safe puzzle-tool reframing is locked in Conflict 8. | 2026-08-19 |
| RISK-008 | Tagline variants unresolved | Closed: both alternates retired in Conflict 13. | 2026-08-19 |
| RISK-009 | Heart of the Core naming unresolved | Closed: renamed/recontextualized as Memory Ocean in Conflict 14. | 2026-08-19 |
| RISK-010 | First Harmony duration/Threshold unconfirmed | Closed: 3–4 centuries and gradual drift model locked in Conflict 11. | 2026-08-19 |
| RISK-011 | Book of Harmony authorship unconfirmed | Closed: Solana authorship and Principles 10/12 locked in Conflict 12. | 2026-08-19 |

---

## Risk Trends (Session-over-Session)

| Session Date | New Risks | Resolved | Active Critical | Active High | Active Medium | Active Low |
|--------------|-----------|----------|-----------------|-------------|---------------|------------|
| 2026-08-04 | 18 | 4 | 1 | 3 | 10 | 4 |
| 2026-08-19 | 0 | 10 | 0 | 1 | 4 | 3 |

---

## Maintenance Rules
1. **Update in place** — modify existing risk rows; don't duplicate
2. **Re-score at each session** — likelihood/impact may change
3. **Escalate** 🔴🟠 risks to human immediately
4. **Link to decisions** — when a risk drives a decision, cross-reference `DECISION_LOG.md` ID
5. **Link to canon** — when a risk affects canon, cross-reference `01-canon-map.md` and `02-conflicts-log.md`
6. **Archive closed risks** — move to "Resolved" section with closure note
7. **Keep filename unchanged** — always `RISK_REGISTER.md`

---

## Change Log
| Date | Version | Changes | Author |
|------|---------|---------|--------|
| 2026-08-04 | v1.0 | Created initial risk register from project analysis | Assistant |
| 2026-08-19 | v1.1 | Closed the stale creator-decision risks after the creator selected the creator-confirmed Conflict Log as authoritative; no technical or asset verification risks were closed. | Assistant |
| 2026-08-19 | v1.2 | Updated RISK-012 with archive evidence: an eight-event-sheet specification exists, but executable Construct implementation evidence is absent. | Assistant |

---

*Template adapted from BabyPetSafety `RISK_REGISTER_v1.md`*