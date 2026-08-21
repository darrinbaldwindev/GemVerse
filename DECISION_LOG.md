# Project Decision Log

## Project Metadata
- **Project Name:** GemVerse
- **Log Version:** v1.1
- **Created:** 2026-08-04
- **Last Updated:** 2026-08-19
- **Maintained By:** Assistant(s) / Human
- **Source of Truth Location:** This file in project root

---

## Purpose
This file captures **durable project decisions** — choices that change direction, lock canon, resolve ambiguity, or establish conventions. Unlike the chronological `SESSION-LOG.md`, this register is organized by **topic** and reflects the **current stable decision** for each area.

**Reading Order:** After `ScanMe.md`, `SESSION-LOG.md`, and `01-canon-map.md` when you need the current decision baseline quickly.

**Note:** This file consolidates decisions from `02-conflicts-log.md`, `01-canon-map.md`, and session history into a single topic-organized register.

---

## Decision Categories

| Category | Description |
|----------|-------------|
| **Canon/Worldbuilding** | Pillars, Wounds, Networks, Eras, Realms, Characters |
| **Tone/Philosophy** | Exclusions, framing rules, narrative voice |
| **Structure/Process** | Tier system, PRS contexts, scan workflow, versioning |
| **Assets/Visuals** | Asset registry, canon risk report, visual framing |
| **Characters/Companions** | Kael, Spark, Companions, Guardians, Citizens |
| **Game/Mechanics** | Puzzle types, gem system, power-ups, combat exclusion |

---

## Active Decisions

### Canon / Worldbuilding
| ID | Decision | Context / Alternatives Considered | Status | Date | Related Files |
|----|----------|-----------------------------------|--------|------|---------------|
| CANON-001 | Eight Pillars as foundational cosmology | Considered fewer/more pillars | **Locked** | 2026-06-02 | `01-canon-map.md`, `04-book-of-harmony.md` |
| CANON-002 | Five Wounds: Knowledge—Fragmentation; Discovery—Isolation; Growth—Decay; Memory—Forgetting; Belonging—Division | Creator selected the prior working set as final; replaces the inconsistent legacy Identity/Purpose listing | **Locked** | 2026-08-19 | `01-canon-map.md`, `02-conflicts-log.md` (Conflict 4), `03-tier1-readiness.md` |
| CANON-003 | The Shattering = structural drift (not war/villain event) | Considered catastrophic war, villain-driven | **Locked** | 2026-06-02 | `01-canon-map.md`, `05-first-harmony.md`, `09-restoration-era.md` |
| CANON-004 | Crystal Network ↔ Wound of Knowledge; Lantern Network ↔ Wound of Belonging | Considered other pairings | **Locked** | 2026-06-02 | `07-crystal-network.md`, `08-lantern-network.md` |
| CANON-005 | Tier 1 foundations as concepts: Book of Harmony, First Harmony, Five Wounds, Crystal Network, Lantern Network, Restoration Era | Considered more granular tiers | **Locked** | 2026-06-02 | `03-tier1-readiness.md`, `tier-roadmap-tracker.md` |
| CANON-006 | Arena Realm = civic assembly (Community theme), first realm Guardians enter | Considered combat arena, later realm | **Locked** | 2026-06-02 | `Arena_Realm_PRS_Context_v1.md`, `arena-realm-production-brief.md` |
| CANON-007 | Guardian Role Bible Vol 1 = details Guardian/Paths/Citizens/Wounds integration (awaiting review) | Considered separate Guardian doc | **Draft** | 2026-06-03 | `guardian_role_bible_volume_1.md` |

### Tone / Philosophy
| ID | Decision | Context / Alternatives Considered | Status | Date | Related Files |
|----|----------|-----------------------------------|--------|------|---------------|
| TONE-001 | No villains, dark lords, or "darkness spreading" | Standard fantasy tropes | **Locked** | 2026-06-02 | `01-canon-map.md`, `SESSION-LOG.md` |
| TONE-002 | No combat, no chosen-one narratives, no power fantasy, no grimdark | Standard RPG/game tropes | **Locked** | 2026-06-02 | `01-canon-map.md`, `GemVerse_AI_Handover.md` |
| TONE-003 | No energy systems that gate/block play (Rule 1.6) | Standard mobile stamina/energy | **Locked** | 2026-06-02 | `GemVerse_AI_Handover.md` |
| TONE-004 | No gacha framing for companions | Standard mobile collection | **Locked** | 2026-06-02 | `GemVerse_AI_Handover.md` |
| TONE-005 | Primary tagline: "Restore Realms. Build Your Legacy." (sole primary) | Considered multiple taglines | **Locked** | 2026-06-02 | `GemVerse_AI_Handover.md` |
| TONE-006 | Puzzles = archaeological fragments of civilization (not arbitrary roadblocks) | Standard puzzle-game framing | **Locked** | 2026-06-02 | `GemVerse_AI_Handover.md`, `puzzle-catalog.md` |

### Structure / Process
| ID | Decision | Context / Alternatives Considered | Status | Date | Related Files |
|----|----------|-----------------------------------|--------|------|---------------|
| PROC-001 | `ScanMe.md` + `Assistant Workflow Template Global` as mandatory first-read | Considered README-first | **Locked** | 2026-06-02 | `ScanMe.md` |
| PROC-002 | Space files = live source of truth; prefer newest versioned file | Considered chat history as truth | **Locked** | 2026-06-02 | `ScanMe.md`, `SESSION-LOG.md` |
| PROC-003 | Filename stability: update content, don't rename maintained files | Considered versioned filenames | **Locked** | 2026-08-04 | `SESSION-LOG.md`, `ScanMe.md` |
| PROC-004 | Default mode: MAIN PROJECT MODE (canon, packets, specs); RESEARCH only when requested | Considered all modes always available | **Locked** | 2026-06-02 | `SESSION-LOG.md` |
| PROC-005 | Non-GemVerse files removed/ignored for Space hygiene | Considered mixed workspace | **Locked** | 2026-06-02 | `SESSION-LOG.md` |
| PROC-006 | `SESSION-LOG.md` as single continuity log (standardized across projects) | Project-specific log names | **Locked** | 2026-08-04 | `SESSION-LOG.md`, `gemverse-session-continuity-log.md` |

### Assets / Visuals
| ID | Decision | Context / Alternatives Considered | Status | Date | Related Files |
|----|----------|-----------------------------------|--------|------|---------------|
| ASSET-001 | Asset registry v2 tracks visual/audio/UI/text assets with risk flags | Considered simple asset list | **Locked** | 2026-06-02 | `asset-registry.md` |
| ASSET-002 | Canon risk report (2026-06-01) as primary audit of Task 10 visual intake | Considered per-asset review | **Locked** | 2026-06-02 | `canon-risk-report-20260601.md` |
| ASSET-003 | Visual framing notes for Arena/Kael as safe reference (`gemverse-visual-framing-notes-arena-kael-v1.md`) | Considered using raw transferred assets | **Locked** | 2026-08-04 | `gemverse-visual-framing-notes-arena-kael-v1.md` |

### Characters / Companions
| ID | Decision | Context / Alternatives Considered | Status | Date | Related Files |
|----|----------|-----------------------------------|--------|------|---------------|
| CHAR-001 | Kael reframe: Option A (Champion of Contribution) — civic/community, not combat | Option B: Void; Option C: Reframe Dark | **Locked** | 2026-08-04 | `02-conflicts-log.md`, `decision-kael-arena-champion-v1.md`, `gemverse-visual-framing-notes-arena-kael-v1.md` |
| CHAR-002 | Spark role: Witness and companion, not puzzle-solving narrator/mechanic | Considered mechanic-integrated narrator | **Locked** | 2026-06-02 | `companion-packet-spark.md`, `SESSION-LOG.md` |
| CHAR-003 | Five Wounds names in `06-five-wounds.md` treated as locked for this Space | Considered flexible naming | **Locked** | 2026-06-02 | `06-five-wounds.md` |
| CHAR-004 | Companion Encyclopedia drafting: Spark, Frostpaw, Verdant, Nimbus in progress | Considered all 7+ at once | **Draft** | 2026-08-04 | `companion-encyclopedia-*.md`, `companion-packet-*.md` |
| CHAR-005 | Companion launch list (Lumi, Ember, Frosty, etc.): launch vs future vs concept | **Decision: A - Launch Companions** (Lumi, Ember, Frosty added to launch roster) | **Locked** | 2026-08-06 | `SESSION-LOG.md` (Open Questions resolved), `asset-registry.md` |

### Game / Mechanics
| ID | Decision | Context / Alternatives Considered | Status | Date | Related Files |
|----|----------|-----------------------------------|--------|------|---------------|
| MECH-001 | 8 puzzle types implemented via Construct 3 event sheets (cascade + Match-3 primary) | Considered other engines/mechanics | **Locked** | 2026-06-02 | `puzzle-catalog.md`, `GemVerse_AI_Handover.md` |
| MECH-002 | Resource bars = collection/cosmetic only (no energy-gating) | Standard mobile energy/stamina | **Locked** | 2026-06-02 | `GemVerse_AI_Handover.md` |
| MECH-003 | "Heart of the Core" deprecated → mapped to Legacy Realm | Considered keeping as separate realm | **Locked** | 2026-06-02 | `SESSION-LOG.md`, `asset-registry.md` |
| MECH-004 | Seventh gem terminology: **Dusk** in mechanical/UI contexts and **Twilight** in narrative/realm contexts; replaces “Dark” | Option A selected; no darkness/corruption framing | **Locked** | 2026-08-04 | `02-conflicts-log.md` (Conflict 7), `puzzle-catalog.md`, `asset-registry.md` |
| MECH-005 | Power-ups, boosters, special gems, and combo feedback reframed as canon-safe puzzle tools and Harmony Flow | Option A selected; no destruction, power escalation, or progression advantage | **Locked** | 2026-08-04 | `02-conflicts-log.md` (Conflict 8), `puzzle-catalog.md` |

---

## Former Deferred Decisions — Resolved
| ID | Confirmed Resolution | Former Blocking Effect | Authority / Date |
|----|----------------------|------------------------|------------------|
| DEF-001 | First Harmony lasted 3–4 centuries; the Threshold was gradual generational drift, not a sudden catastrophe. | Era framing consistency | Creator confirmation in `02-conflicts-log.md` (Conflict 11), 2026-08-04 |
| DEF-002 | Solana the First Harmonist authored all seven original Volumes; Principles 10 and 12 are locked. | Canon depth | Creator confirmation in `02-conflicts-log.md` (Conflict 12), 2026-08-04 |
| DEF-003 | Reframe mechanics as canon-safe puzzle tools and Harmony Flow; no destructive or power-escalation framing. | Game mechanics design | Creator confirmation in `02-conflicts-log.md` (Conflict 8), 2026-08-04 |
| DEF-004 | Retire both alternate taglines; retain only “Restore Realms. Build Your Legacy.” and “A world worth belonging to.” | Brand messaging | Creator confirmation in `02-conflicts-log.md` (Conflict 13), 2026-08-04 |
| DEF-005 | “Heart of the Core” is the former working title for Memory Ocean; no tenth Realm is added. | Environment naming | Creator confirmation in `02-conflicts-log.md` (Conflict 14), 2026-08-04 |
| DEF-006 | Lumi, Ember, and Frosty are launch companions, bringing the launch roster to 11. | Companion production | Creator confirmation in `02-conflicts-log.md` (Conflict 6), 2026-08-04 |
| DEF-007 | Forestkin is the common name; Verdankin is the formal/scholarly name. | Species naming consistency | Creator confirmation in `02-conflicts-log.md` (Conflict 9), 2026-08-04 |
| DEF-008 | Guardian canon/proposal split is complete; core Guardian role is locked and exploratory mechanics remain proposals. | Guardian system canonization | Creator confirmation in `02-conflicts-log.md` (Conflict 10), 2026-08-04 |

---

## Rejected / Superseded Decisions
| ID | Original Decision | Replacement | Reason | Date |
|----|-------------------|-------------|--------|------|
| REJ-001 | Kael as warrior/combat leader | Option A: Champion of Contribution | Combat drift violation | 2026-08-04 |
| REJ-002 | "Heart of the Core" as active realm name | Legacy Realm mapping | Canon consistency | 2026-06-02 |
| REJ-003 | Multiple primary taglines | Single primary tagline | Brand focus | 2026-06-02 |
| REJ-004 | Energy-gating resource bars | Cosmetic/collection only | Violates Rule 1.6 | 2026-06-02 |
| REJ-005 | `gemverse-session-continuity-log.md` as log name | `SESSION-LOG.md` (standardized) | Cross-project consistency | 2026-08-04 |

---

## Maintenance Rules
1. **Update in place** — modify the decision row above; don't create new rows for changes to same decision
2. **Status values:** `Locked` / `Draft` / `Deferred` / `Blocked` / `Rejected` / `Superseded`
3. **Cross-reference** `SESSION-LOG.md` for chronological context when a decision was made
4. **Cross-reference** `02-conflicts-log.md` for conflict resolution history
5. **Cross-reference** `01-canon-map.md` for canon authority status
6. **Keep filename unchanged** — always `DECISION_LOG.md`
7. **Review quarterly** — audit for stale `Draft`/`Blocked` items

---

## Change Log
| Date | Version | Changes | Author |
|------|---------|---------|--------|
| 2026-08-04 | v1.0 | Created standardized decision log from canon-map, conflicts-log, session-log, handover docs | Assistant |
| 2026-08-19 | v1.1 | Reconciled stale Draft, Blocked, and Deferred entries to creator-confirmed Conflict Log resolutions after the creator selected the Conflict Log as the authoritative record. | Assistant |
| 2026-08-19 | v1.2 | Recorded creator confirmation of the official Five Wounds names and descriptors; replaced an inconsistent legacy name set. | Assistant |

---

*Template adapted from BabyPetSafety `DECISION_LOG_v1.md` and Amazon `working-decisions-register.md`*