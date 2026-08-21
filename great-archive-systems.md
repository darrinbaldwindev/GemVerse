# Great Archive Systems
**Version:** 1.0
**Status:** Canon-Locked
**Tier:** 4 System 3

---

## Design Principles (Canon-Locked)

| Principle | Implementation |
|-----------|----------------|
| Preservation, not collection | Archive receives; doesn't "unlock" |
| Testimony over data | Companion memories > text fragments |
| Living chronicle | Grows through commentary (Talmud model) |
| Seven Sections | Fixed architecture from Conflict 2 |
| No completionism | Mysteries remain open; gaps are meaningful |
| Cross-reference as discovery | Connections reveal themselves |
| Guardian as Chronicler | Contributing = chronicling |

---

## Great Archive Architecture

### Seven Sections (Fixed — Conflict 2)

| Section | Purpose | In-World Origin | Content Type |
|---------|---------|-----------------|--------------|
| **1. Crystal Network Records** | Knowledge flow history | Lumina scholars, First Harmony | Node calibrations, research transmissions, cross-Realm communications |
| **2. Pathfinder Expeditions** | Discovery distribution | Astra Pathfinders, First Harmony | Route logs, waypoint maps, discovery reports, failed returns |
| **3. Verdance Cultivation** | Growth conditions | Verdance Stewards, First Harmony | Field records, mentorship lineages, cultivation protocols |
| **4. Borealis Testimonies** | Memory preservation | Borealis Chroniclers + Companions | Companion memories, citizen oral histories, ice-formations |
| **5. Hearthlight Traditions** | Belonging practices | Hearthlight communities, First Harmony | Festival records, civic agreements, community patterns |
| **6. Solstice Harmonies** | Systemic balance | Solstice Harmonists, First Harmony | Pillar assessments, balance records, drift warnings |
| **7. Book of Guardians** | Contribution chronicle | Archive Chroniclers, ongoing | Guardian names, deeds, legacies — living record |

### Physical/Digital Structure
```
GREAT ARCHIVE (Arena Realm - Central Spire)
├── Level 1: Public Reading Hall
│   ├── Crystal Network Terminal (Section 1)
│   ├── Pathfinder Map Table (Section 2)
│   ├── Verdance Garden-Archive (Section 3)
│   ├── Borealis Listening Chamber (Section 4)
│   ├── Hearthlight Festival Gallery (Section 5)
│   ├── Solstice Balance Observatory (Section 6)
│   └── Guardian Chronicle Alcove (Section 7)
│
├── Level 2: Chronicler Workrooms (Restored access)
│   ├── Lumina Calibration Desks
│   ├── Astra Route Verification
│   ├── Verdance Seed Vault
│   ├── Borealis Transcription Cells
│   ├── Hearthlight Pattern Looms
│   ├── Solstice Alignment Instruments
│   └── Guardian Induction Registry
│
├── Level 3: Deep Archive (Threshold access)
│   ├── Fragmented Records (awaiting assembly)
│   ├── Sealed Legacies (Legacy Seals)
│   ├── Open Mysteries (never resolved)
│   └── Volume VIII: On Belonging (citizen voices)
│
└── Level 4: Lantern Core (Network heart)
    ├── 9 Realm Lantern synchronization
    ├── Civilization Harmony Index live feed
    └── Book of Harmony original manuscript display
```

---

## Archive Record Types (Canon)

### Fragment Types (Puzzle Rewards)

| Fragment Type | Source Puzzle | Archive Section | Canon Purpose |
|---------------|---------------|-----------------|---------------|
| **Knowledge Fragment** | Crystal Resonance | 1. Crystal Network | Node history, research in transit, cross-Realm comms |
| **Expedition Record** | Pathfinder's Mark | 2. Pathfinder Expeditions | Route logs, discoveries, failed returns |
| **Companion Testimony** | Echo Sequence | 4. Borealis Testimonies | Living memory, first-person history |
| **Festival Record** | Community Pattern | 5. Hearthlight Traditions | Civic agreements, tradition status, participation |
| **Steward Field Record** | Verdance Cultivation | 3. Verdance Cultivation | Growth trajectories, mentor lines, protocols |
| **Harmonist Balance Record** | Harmony Alignment | 6. Solstice Harmonies | Pillar states, balance actions, drift warnings |
| **Cross-Realm Discovery** | Fragment Assembly | 1, 2, or 3 (context) | Parallel research, connected fragments |
| **Sealed Legacy** | Legacy Seal | 7. Book of Guardians / Deep Archive | Complete testimonies, community pledges, Time Capsules |

### Record States (Not "Rarity")

| State | Meaning | Visual |
|-------|---------|--------|
| **Intact** | Complete record, fully transcribed | Full color, readable |
| **Partial** | Fragmented, awaiting assembly | Ghosted sections, fragment icons |
| **Sealed** | Legacy Seal protected | Gold lock, requires readiness |
| **Living** | Companion testimony (ongoing) | Pulse animation, Companion-linked |
| **Open Mystery** | Never resolved (Memory Ocean, Missing Realm, etc.) | Question-mark, soft glow |
| **Commentary** | Later generation's reflection | Margin notes, linked to original |

---

## Archive Mechanics

### Deposit Flow (Guardian as Chronicler)

```javascript
// ArchiveDepositSystem — Canon Implementation
const ArchiveDeposit = {
  
  depositFragment(fragment, guardian, companion, realm) {
    const deposit = {
      fragment: fragment,
      chronicler: guardian.id,
      witness: companion?.id,
      realm: realm.id,
      cycle: currentCycle(),
      context: this.gatherContext(fragment, guardian, companion, realm),
      crossReferences: this.findConnections(fragment),
      state: 'intact',
      commentary: [],
      restorationConfirmation: {
        pillarBoosted: fragment.pillar,
        woundHealed: fragment.wound,
        archiveCompleteness: this.calculateCompleteness(fragment.section),
        civilizationImpact: this.calculateImpact(fragment)
      }
    };
    
    this.addToSection(fragment.section, deposit);
    this.notifyConnections(deposit.crossReferences);
    HarmonyIndex.updateBorealis(archive);
    
    return deposit;
  },
  
  gatherContext(fragment, guardian, companion, realm) {
    return {
      puzzleType: fragment.puzzleType,
      inWorldOrigin: fragment.civilizationalOrigin,
      originalPurpose: fragment.originalPurpose,
      whatItReveals: fragment.reveals,
      whatItRestores: fragment.restores,
      guardianAction: 'chronicled',
      companionWitness: companion?.role || 'none',
      realmState: realm.harmonyIndexSnapshot()
    };
  },
  
  findConnections(fragment) {
    return archive.sections.flatMap(section => 
      section.records
        .filter(r => this.sharesElements(fragment, r))
        .map(r => ({
          recordId: r.id,
          connectionType: this.classifyConnection(fragment, r),
          strength: this.calculateStrength(fragment, r)
        }))
    ).filter(c => c.strength > 0.3);
  }
};
```

### Cross-Reference Discovery (Passive, Not Push)

| Trigger | Discovery | Presentation |
|---------|-----------|--------------|
| Deposit shares 2+ keywords with existing record | "A connection stirs in the Archive" | Soft glow on related section tab |
| Fragment completes a partial record | "The record breathes whole again" | Partial → Intact transition animation |
| Companion testimony matches historical fragment | "A voice remembers what was written" | Testimony links to fragment |
| Festival record matches past tradition | "The pattern returns" | Festival record links to historical |
| Legacy Seal relates to open mystery | "The seal acknowledges the mystery" | Seal glows near mystery tab |

---

## Seven Section Deep Specs

### Section 1: Crystal Network Records
- **Node Calibration Logs** (per node, per cycle)
- **Research Transmissions** (Lumina scholarship, cross-Realm collaborations, fragmented transmissions)
- **Network Topology Maps** (Original Design, Threshold State, Current Restoration)
- **Knowledge Fragment Index** (by Realm, Discipline, Era)
- **Key Records:** First Calibration Protocol (Legacy Seal), Parallel Discovery Fragments (REV-004 + REV-010), Threshold Drift Logs

### Section 2: Pathfinder Expeditions
- **Route Maps** (Original Waypoint Sequences, Threshold Closure Logs, Restored Routes)
- **Expedition Reports** (Successful Returns, Failed Returns, One-Way Journeys)
- **Waypoint Stones** (Carved Inscriptions, Seasonal Markings, Guardian Restoration Notes)
- **Discovery Registry** (by Realm, Type, Era)
- **Key Records:** Lyra's Seven Winds Expedition (REV-003, REV-011), Last Complete Cross-Realm Circuit (Year 340), Unfinished Route Maps

### Section 3: Verdance Cultivation
- **Site Field Records** (Soil/Environment Baselines, Seasonal Growth Logs, Mentor-Apprentice Lineages, Guardian Restoration Protocols)
- **Cultivation Protocols** (By Environment Type, Cross-Realm Adaptations, Threshold Loss Records)
- **Mentorship Registry** (Active Lines, Broken Lines, Restored Lines)
- **Growth Fragment Index** (Steward Field Records, cross-referenced)
- **Key Records:** Mossbloom's Ember Depths Protocol (REV-005), Rootwhisper's Node Installation Log, Broken Mentor Lines (47 fractured, 12 restored)

### Section 4: Borealis Testimonies
- **Companion Memories** (all 11 companions with themes)
- **Citizen Oral Histories** (by Realm, Generation, By Path)
- **Ice-Formation Transcriptions** (Frozen Expanse)
- **Memory Fragment Index** (by Witness, Era, Wound)
- **Key Records:** Frostpaw's First Festival Memory (REV-002), Frostpaw's Literacy Memory (REV-009), Echo's Lost Voices Collection (200+ unmatched)

### Section 5: Hearthlight Traditions
- **Festival Records** (10 festivals × cycles with participants, patterns, records, cross-Realm attendance)
- **Civic Agreements** (Community Pattern Designs, Cross-Realm Pacts, Threshold Fractures)
- **Community Pattern Index** (by Realm, Tradition, Era)
- **Tradition Vitality Metrics** (Participation rates, Cross-Realm continuity)
- **Key Records:** Last Pan-Realm Harmony Week (REV-006), First Lantern Gathering Charter, Fractured Agreements (23 broken, 8 restored)

### Section 6: Solstice Harmonies
- **Pillar Balance Records** (7-Pillar State Snapshots, Drift Trajectories, Harmonist Interventions, Guardian-Supported Alignments)
- **Harmony Protocols** (Assessment Methodologies, Rebalancing Techniques, Threshold Early-Warning Signs)
- **Convergence Records** (Great Convergence Cycles, Threshold Missed Convergences, Restoration Era Convergences)
- **Systemic Fragment Index** (Harmonist Balance Records, cross-referenced to ALL sections)
- **Key Records:** Celestial Nexus Peak Balance (REV-007), First Missed Convergence (Year 382), Drift Warning Catalog (14 precursors)

### Section 7: Book of Guardians
- **Guardian Entries** (Name/Title/Era, Contribution Summary, Realms/Pillars/Wounds, Companion Witnesses, Citizen Testimonies)
- **Induction Registry** (Annual Legacy Promise inductees, Great Convergence contributors, Anonymous contributors)
- **Guardian Legacy Seals** (Personal seals opened, Time Capsules deposited, Deep Archive cross-references)
- **Civilization Impact Index** (Per Guardian Harmony Index contribution, Aggregate Guardian Contribution Index)
- **Key Records:** Kael — Champion of Contribution, First Guardian (unnamed), Solana the First Harmonist

---

## Archive Access Tiers (Restoration-Gated, Not Level-Gated)

| Tier | Access | Requirement | Canon Frame |
|------|--------|-------------|-------------|
| Public Reading Hall | Sections 1-6 (intact records), Section 7 (recent) | None — always open | "The Archive remembers for everyone" |
| Chronicler Workrooms | Partial records, Fragment Assembly, Commentary tools | 1+ Fragment deposited | "You have chronicled; you may study" |
| Deep Archive | Sealed Legacies, Open Mysteries, Volume VIII | Wound Healing threshold (any ≥ 60%) | "The civilization trusts your restoration" |
| Lantern Core | Live Harmony Index, Book of Harmony original | Civilization Harmony ≥ 65% | "The network recognizes your contribution" |

---

## Open Mysteries (Never Resolved — Protected)

| Mystery | Archive Location | Guardian Interaction |
|---------|------------------|---------------------|
| The Memory Ocean | Section 4 (referenced), Deep Archive (guarded) | Tides surface fragments; never fully mapped |
| The Missing Realm | Section 2 (failed expeditions), Deep Archive | Route fragments hint; never located |
| The Lost Harmonists | Section 6 (last records), Deep Archive | Convergence records end; fate unknown |
| The Seventh Lantern | Section 1 (referenced), Section 7 (First Guardian) | Memory tide brought fragment; location unknown |
| The Sleeping Gate | Section 3 (cultivation references), Deep Archive | Seed legends; never found |
| The Forgotten Door | Section 5 (civic pact mentions), Deep Archive | Civic pact mentions; never opened |

**Stop Rule 1 Enforcement:** No puzzle, festival, or narrative beat resolves these. They deepen.

---

## Integration with Other Systems

| System | Archive Touchpoint |
|--------|-------------------|
| Festival Encyclopedia | Festival Records → Section 5; Festival participation → Borealis Index |
| Harmony Index | Borealis Index = Archive completeness; All deposits → Pillar Indices |
| Puzzle Catalog | Each puzzle type → specific Fragment Type → specific Section |
| Companion System | Testimonies → Section 4; Presence → cross-reference discovery |
| Citizen Paths | Scholar deposits → Section 1-6; Harmonist alignments → Section 6 |
| Guardian System | Book of Guardians = Section 7; Contribution Index = Archive deposits |
| Realm Packets | Each Realm has Archive terminal showing its records |
| Narrative Arcs | Aurora Arc = Archive mystery; Spark Arc = First Chronicle |

---

## Implementation Checklist

| Component | Status |
|-----------|--------|
| Seven Sections architecture | ✅ Specified |
| Fragment Types (8) + States (6) | ✅ Specified |
| Deposit Flow (Chronicler model) | ✅ Specified |
| Cross-Reference Discovery (passive) | ✅ Specified |
| Seven Section Deep Specs | ✅ Specified |
| Access Tiers (4) | ✅ Specified |
| Open Mysteries (6) protected | ✅ Specified |
| Key Records identified | ✅ Specified |
| System Integration Map | ✅ Specified |

---

## Tier 4 System 3: COMPLETE ✅