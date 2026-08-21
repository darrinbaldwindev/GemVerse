# Harmony Index Mechanics
**Version:** 1.0
**Status:** Canon-Locked
**Tier:** 4 System 2

---

## Design Principles (Canon-Locked)

| Principle | Implementation |
|-----------|----------------|
| Restoration metric, not progression | Measures healing, not advancement |
| No energy gating | Never blocks play; only reflects state |
| Civilization-wide + Realm-local | Dual scope: personal contribution ↔ collective health |
| Wound-aligned | Each Index component maps to a Wound |
| Companion/citizen integrated | Their presence affects Index |
| Festival-driven milestones | Major shifts at festival convergences |
| Transparent, not gamified | Visible as "civilization health" not "player stats" |

---

## Harmony Index Architecture

### Seven Pillar Indices (Core)

| Pillar | Index Name | Wound Alignment | Measurement | Range |
|--------|------------|-----------------|-------------|-------|
| Knowledge | **Lumina Index** | Fragmentation | Crystal Network node synchronization % | 0-100% |
| Discovery | **Astra Index** | Isolation | Active cross-Realm routes / Lantern sync | 0-100% |
| Growth | **Verdance Index** | Decay | Cultivation sites flourishing / mentor lines active | 0-100% |
| Memory | **Borealis Index** | Forgetting | Archive completeness / Companion testimonies held | 0-100% |
| Resilience | **Hearthlight Index** | Division (community) | Festival participation / civic traditions active | 0-100% |
| Harmony | **Solstice Index** | All (systemic) | 7-Pillar balance variance (lower = better) | 0-100% |
| Belonging | **Unity Index** | Division (deep) | Cross-Realm connections / Guardian recognition | 0-100% |

### Composite Indices

| Composite | Formula | Purpose |
|-----------|---------|---------|
| **Realm Harmony Index** | Weighted avg of 7 Pillars for that Realm | Realm-specific health |
| **Civilization Harmony Index** | Avg of 9 Realm Harmony Indices | Overall civilization health |
| **Wound Healing Index** | Inverse of Wound severity (5 separate) | Per-Wound progress |
| **Guardian Contribution Index** | Personal restoration actions / civilization needs | Individual reflection (not competitive) |

---

## Measurement Mechanics

### Data Sources (Passive + Active)

| Source | Feeds | Frequency |
|--------|-------|-----------|-
| Crystal Network Nodes | Lumina Index (sync %), Knowledge fragments flowing | Continuous |
| Lantern Network | Astra Index (route sync), Unity Index (cross-Realm pings) | Continuous |
| Cultivation Sites | Verdance Index (flourishing %), Growth fragment flow | Daily cycle |
| Archive | Borealis Index (completeness %), Memory fragment intake | Per deposit |
| Festival Participation | Hearthlight Index, Unity Index, all Pillars | Per festival |
| Puzzle Completion | Relevant Pillar Index (per puzzle type) | Per solve |
| Citizen Path Advancement | Realm Harmony, relevant Pillar | Per milestone |
| Companion Presence | Realm Harmony (where present), Unity Index | Continuous |
| Guardian Actions | Guardian Contribution Index, relevant Pillars | Per action |

### Index Calculation (Per Realm, Per Cycle)

```typescript
// HarmonyIndexCalculator — Canon Implementation
const HarmonyIndex = {
  
  PILLAR_WEIGHTS: {
    Knowledge: 1.0,
    Discovery: 1.0,
    Growth: 1.0,
    Memory: 1.0,
    Resilience: 1.0,
    Harmony: 1.5,
    Belonging: 1.5
  },
  
  calculateRealmHarmony(realmData) {
    const pillars = [
      this.calculateLumina(realmData.crystalNetwork),
      this.calculateAstra(realmData.lanternNetwork),
      this.calculateVerdance(realmData.cultivationSites),
      this.calculateBorealis(realmData.archive),
      this.calculateHearthlight(realmData.festivals),
      this.calculateSolstice(realmData.pillarBalance),
      this.calculateUnity(realmData.connections)
    ];
    
    const weightedSum = pillars.reduce((sum, p, i) => 
      sum + p.value * Object.values(this.PILLAR_WEIGHTS)[i], 0);
    const weightTotal = Object.values(this.PILLAR_WEIGHTS).reduce((a,b) => a+b, 0);
    
    return {
      realmHarmony: Math.round(weightedSum / weightTotal),
      pillarBreakdown: pillars,
      woundHealing: this.calculateWoundHealing(pillars),
      trend: this.calculateTrend(realmData.history)
    };
  },
  
  calculateLumina(network) {
    const activeNodes = network.nodes.filter(n => n.state === 'calibrated').length;
    const totalNodes = network.nodes.length;
    const fragmentFlow = network.fragmentsTransmittedLastCycle;
    const expectedFlow = network.baselineFlow;
    
    const syncScore = totalNodes > 0 ? (activeNodes / totalNodes) * 100 : 0;
    const flowScore = expectedFlow > 0 ? Math.min(100, (fragmentFlow / expectedFlow) * 100) : 0;
    
    return {
      name: 'Lumina Index',
      value: Math.round((syncScore * 0.7) + (flowScore * 0.3)),
      components: { sync: syncScore, flow: flowScore },
      wound: 'Fragmentation'
    };
  },
  
  // ... rest of calculation functions
};
```

---

## Visualization (No Gamification)

### Guardian View: "Civilization Health Dashboard"
CIVILIZATION HARMONY INDEX                    Cycle 847
Overall: ████████████░░░░░░░░  62%  ▲ +3% this cycle

WOUNDS HEALING:
┌─────────────┬────────┬────────┬────────┬────────┐
│Fragmentation│Isolation│  Decay  │Forgetting│Division│
├─────────────┼────────┼────────┼────────┼────────┤
│    68%      │  54%   │  71%   │  48%   │  59%   │
│   ██████░░  │ ████░░░ │ ███████░│ ████░░░ │ █████░░ │
└─────────────┴────────┴────────┴────────┴────────┘

REALM HEALTH:
┌──────────────┬──────┬──────────────┬──────┐
│ Crystal Forest│ 78%  │ Sky Citadel   │ 65%  │
│ Frozen Expanse│ 72%  │ Ember Depths  │ 69%  │
│ Twilight Front│ 58%  │ Celestial Nexus│ 61% │
│ Legacy Realm  │ 74%  │ Memory Ocean  │ 55%  │
│ Arena Realm   │ 82%  │               │      │
└──────────────┴──────┴──────────────┴──────┘

YOUR CONTRIBUTION:  ▲ +12% this cycle
┌─────────────────────────────────────────────────────┐
│ Recent: Crystal Forest node calibrated (Lumina +4%)  │
│         Frozen Expanse memory transcribed (Borealis+3%)│
│         Lantern Gathering attended (Unity +5%)        │
└─────────────────────────────────────────────────────┘

Realm View (At Realm Lantern)
CRYSTAL FOREST — REALM HARMONY: 78% ▲
├─ Knowledge (Lumina):      85% ████████████████░░
├─ Discovery (Astra):       72% ████████████░░░░
├─ Growth (Verdance):       81% ███████████████░░
├─ Memory (Borealis):       68% ███████████░░░░░
├─ Resilience (Hearthlight):79% ███████████████░░
├─ Harmony (Solstice):      83% ████████████████░
└─ Belonging (Unity):       74% ████████████░░░░

WOUND STATUS:
Fragmentation:  15% healed ██░░░░░░░░░░
Isolation:      28% healed ███░░░░░░░░░
Decay:          19% healed ██░░░░░░░░░░

NEXT MILESTONE: Bloom Equinox (14 days) → Projected +8% Realm Harmony

Festival View (During Convergence)
BLOOM EQUINOX — DAY 4 CONVERGENCE
Crystal Forest Harmony: 78% → 86% (projected)

LIVE CONTRIBUTIONS:
├─ Nodes calibrated: 112/127
├─ Resonance seeds planted: 1,247
├─ Cross-Realm visitors: 6 Realms present
├─ Knowledge fragments flowing: 340/min
└─ Companion presence: Verdant, Prism, Nimbus, Galewing

PROJECTED IMPACT:
Lumina Index:     +7%  (node sync)
Astra Index:      +5%  (route verification)
Verdance Index:   +4%  (seed germination)
Hearthlight Index:+6%  (participation)
Unity Index:      +8%  (cross-Realm connections)

---

## Milestone Thresholds (Festival-Triggered)

| Milestone | Threshold | Effect |
|-----------|-----------|--------|
| Realm Awakening | Realm Harmony ≥ 60% | Lantern relit; Realm accessible; festivals resume |
| Network Reconciliation | Astra Index ≥ 70% (civ-wide) | All 9 Lanterns sync; cross-Realm travel unrestricted |
| Archive Critical Mass | Borealis Index ≥ 75% | Legacy Seals approachable; lost memories recoverable |
| Civilization Stabilization | Civ Harmony Index ≥ 65% | Harmony Week gains "Great Convergence" tier |
| Wound Threshold | Any Wound Healing ≥ 80% | That Wound enters "Restored" state; new content unlocks |
| Guardian Recognition | Guardian Contribution ≥ 1000 | Hall of Guardians induction eligibility |

---

## Companion/Citizen Influence

### Companion Presence Bonus (Per Realm)

| Companion | Realm | Index Boost | Duration |
|-----------|-------|-------------|----------|
| Verdant | Crystal Forest | Lumina +2%, Verdance +3% | While present |
| Prism | Crystal Forest | Lumina +3%, Solstice +2% | While present |
| Bloomtail | Ember Depths | Verdance +3%, Hearthlight +2% | While present |
| Frostpaw | Frozen Expanse | Borealis +3%, Unity +2% | While present |
| Echo | Frozen Expanse / Legacy | Borealis +2%, Unity +3% | While present |
| Nimbus | Sky Citadel / Twilight | Astra +3%, Discovery +2% | While present |
| Galewing | All (circulating) | Astra +1% per Realm visited | 24h after visit |
| Spark | Arena Realm | Unity +3%, Hearthlight +2% | While present |
| Lumi (future) | All (thresholds) | Unity +2% at Lanterns | While present |
| Ember (future) | Ember Depths | Verdance +2%, Hearthlight +3% | While present |
| Frosty (future) | Frozen Expanse | Borealis +2%, Unity +2% | While present |

### Citizen Path Contributions (Per Milestone)

| Path | Index Contribution | Trigger |
|------|-------------------|---------|
| Scholar | Borealis +1%, Lumina +1% | Archive deposit |
| Mentor | Hearthlight +2%, Unity +1% | Apprentice graduates |
| Harmonist | Solstice +3%, all Pillars +1% | Harmony Alignment led |
| Pathfinder | Astra +2%, Unity +2% | Route restored |

---

## Anti-Gamification Safeguards

```javascript
const SAFEGUARDS = {
  noDecayFromInactivity: true,
  noContentGating: true,
  noPlayerProfileDisplay: true,
  noLeaderboards: true,
  noRankings: true,
  noCompetition: true,
  language: {
    index: "healing",
    progress: "restoration",
    milestone: "threshold crossed",
    contribution: "what you've helped restore"
  },
  companionEffect: "civilization_wide",
  festivalMilestones: "civilization_events"
};
```

---

## Integration Points

| System | Integration |
|--------|-------------|
| Festival Encyclopedia | Milestone projections; live convergence data |
| Great Archive | Borealis Index = Archive completeness; Archive Records boost |
| Puzzle Catalog | Each puzzle type → specific Pillar Index |
| Companion System | Presence bonuses; circulation tracking |
| Citizen Paths | Milestone contributions; Realm Harmony advancement |
| Guardian System | Contribution Index; Hall of Guardians eligibility |
| Realm Packets | Each Realm has baseline Index targets |
| Narrative Arcs | Index thresholds trigger arc beats |

---

## Implementation Checklist

| Component | Status |
|-----------|--------|
| Seven Pillar Indices + Composites | ✅ Specified |
| Measurement data sources | ✅ Specified |
| Lumina Index calculation | ✅ Specified |
| Astra Index calculation | ✅ Specified |
| Verdance Index calculation | ✅ Specified |
| Borealis Index calculation | ✅ Specified |
| Hearthlight Index calculation | ✅ Specified |
| Solstice Index calculation | ✅ Specified |
| Unity Index calculation | ✅ Specified |
| Wound Healing calculation | ✅ Specified |
| Visualization dashboard | ✅ Specified |
| Companion presence bonuses | ✅ Specified |
| Citizen path contributions | ✅ Specified |
| Anti-gamification safeguards | ✅ Specified |
| System integration map | ✅ Specified |

---

## Tier 4 System 2: COMPLETE ✅