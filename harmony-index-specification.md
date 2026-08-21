# Harmony Index System Specification
**Version:** 1.0  
**Status:** Implementation Ready  
**Authority:** Canon-locked (Tier 4 specification)

---

## Overview
The Harmony Index is the civilization's systemic health measure — not a player score, not a progression metric. It reflects the **state of the Seven Pillars across all Nine Realms**. Guardians don't "increase" the Index; they **restore balance** that allows the civilization to heal itself.

---

## Seven Pillar Definitions

### Pillar Data Structure
```javascript
const PILLAR_DEFINITIONS = {
  knowledge: {
    id: 'knowledge',
    name: 'Knowledge',
    house: 'Lumina',
    realmAnchor: 'crystal-forest',
    color: '#1F4E79', // Archive Blue
    gemType: 'Light',
    companionFamily: 'Crystalkin',
    indicators: [
      { id: 'node_connectivity', name: 'Node Connectivity %', weight: 0.3 },
      { id: 'fragment_recovery', name: 'Fragment Recovery Rate', weight: 0.25 },
      { id: 'knowledge_flow', name: 'Cross-Realm Knowledge Flow', weight: 0.25 },
      { id: 'scholar_activity', name: 'Scholar Activity', weight: 0.2 }
    ],
    restorationActions: [
      'Crystal Resonance puzzles',
      'Fragment Assembly puzzles',
      'Archive contributions'
    ],
    companionStabilization: ['Spark', 'Prism']
  },
  
  discovery: {
    id: 'discovery',
    name: 'Discovery',
    house: 'Astra',
    realmAnchor: 'sky-citadel',
    color: '#C9A227', // Lantern Gold
    gemType: 'Air',
    companionFamily: 'Skykin',
    indicators: [
      { id: 'route_restoration', name: 'Route Restoration %', weight: 0.3 },
      { id: 'lantern_sync', name: 'Lantern Sync Quality', weight: 0.25 },
      { id: 'pathfinder_activity', name: 'Pathfinder Activity', weight: 0.25 },
      { id: 'realm_contact', name: 'New Realm Contact', weight: 0.2 }
    ],
    restorationActions: [
      'Pathfinder\'s Mark puzzles',
      'Lantern Network calibration',
      'Whisper Wind participation'
    ],
    companionStabilization: ['Nimbus', 'Galewing']
  },
  
  growth: {
    id: 'growth',
    name: 'Growth',
    house: 'Verdance',
    realmAnchor: 'ember-depths',
    color: '#2E8B57', // Emerald Green
    gemType: 'Earth',
    companionFamily: 'Forestkin',
    indicators: [
      { id: 'cultivation_health', name: 'Cultivation Site Health', weight: 0.3 },
      { id: 'mentorship_continuity', name: 'Mentorship Lineage Continuity', weight: 0.25 },
      { id: 'seed_exchange', name: 'Seed Exchange Diversity', weight: 0.25 },
      { id: 'community_dev', name: 'Community Development', weight: 0.2 }
    ],
    restorationActions: [
      'Verdance Cultivation puzzles',
      'Bloom Equinox participation',
      'Steward record recovery'
    ],
    companionStabilization: ['Verdant', 'Bloomtail']
  },
  
  memory: {
    id: 'memory',
    name: 'Memory',
    house: 'Borealis',
    realmAnchor: 'frozen-expanse',
    color: '#9370DB', // Amethyst Purple
    gemType: 'Water',
    companionFamily: 'Frostkin',
    indicators: [
      { id: 'companion_memory', name: 'Companion Memory Contribution', weight: 0.3 },
      { id: 'archive_completeness', name: 'Archive Completeness %', weight: 0.25 },
      { id: 'ancestor_lanterns', name: 'Ancestor Lantern Relighting', weight: 0.25 },
      { id: 'oral_tradition', name: 'Oral Tradition Preservation', weight: 0.2 }
    ],
    restorationActions: [
      'Echo Sequence puzzles',
      'Frost Commemoration festival',
      'Legacy Seal opening'
    ],
    companionStabilization: ['Frostpaw', 'Echo']
  },
  
  resilience: {
    id: 'resilience',
    name: 'Resilience',
    house: 'Hearthlight',
    realmAnchor: 'arena-realm',
    color: '#FF6B35', // Sunset Orange
    gemType: 'Fire',
    companionFamily: 'Emberkin',
    indicators: [
      { id: 'gathering_frequency', name: 'Community Gathering Frequency', weight: 0.3 },
      { id: 'festival_participation', name: 'Festival Participation %', weight: 0.25 },
      { id: 'mutual_aid', name: 'Mutual Aid Network Strength', weight: 0.25 },
      { id: 'hearth_connectivity', name: 'Hearth Connectivity', weight: 0.2 }
    ],
    restorationActions: [
      'Community Pattern puzzles',
      'Ember Warmth festival',
      'Warmth Exchange'
    ],
    companionStabilization: ['Ember (future)', 'Frosty (future)']
  },
  
  harmony: {
    id: 'harmony',
    name: 'Harmony',
    house: 'Solstice',
    realmAnchor: 'celestial-nexus',
    color: '#FFD700', // Pure Gold
    gemType: 'Rainbow',
    companionFamily: 'Solstice (primary) / Legacy (Belonging)',
    indicators: [
      { id: 'pillar_balance', name: 'Pillar Balance Variance', weight: 0.35 },
      { id: 'convergence_depth', name: 'Convergence Celebration Depth', weight: 0.25 },
      { id: 'harmonist_activity', name: 'Harmonist Activity', weight: 0.2 },
      { id: 'systemic_equilibrium', name: 'Systemic Equilibrium', weight: 0.2 }
    ],
    restorationActions: [
      'Harmony Alignment puzzles',
      'Convergence Celebration festival',
      'Harmonist record recovery'
    ],
    companionStabilization: ['Prism']
  },
  
  belonging: {
    id: 'belonging',
    name: 'Belonging',
    house: 'Legacy',
    realmAnchor: 'legacy-realm',
    color: '#FFFFFF', // Pure White
    gemType: 'Rainbow',
    companionFamily: 'All (cross-cutting)',
    indicators: [
      { id: 'cross_realm_attendance', name: 'Cross-Realm Festival Attendance', weight: 0.3 },
      { id: 'citizen_path_engagement', name: 'Citizen Path Engagement', weight: 0.25 },
      { id: 'hall_of_guardians', name: 'Hall of Guardians Recognition', weight: 0.25 },
      { id: 'intergenerational', name: 'Intergenerational Continuity', weight: 0.2 }
    ],
    restorationActions: [
      'All festival participation',
      'Legacy Promise sealing',
      'Book of Guardians entries'
    ],
    companionStabilization: ['Bloomtail']
  }
};
```

---

## Nine Realm Definitions

```javascript
const REALM_DEFINITIONS = {
  'arena-realm': {
    id: 'arena-realm',
    name: 'Arena Realm',
    pillarFocus: ['resilience', 'belonging', 'harmony'],
    lanternNode: 'harmony-plaza',
    connectedRealms: ['crystal-forest', 'sky-citadel', 'ember-depths'],
    state: 'restoration-active'
  },
  'crystal-forest': {
    id: 'crystal-forest',
    name: 'Crystal Forest',
    pillarFocus: ['knowledge', 'growth'],
    lanternNode: 'lumina-grove',
    connectedRealms: ['arena-realm', 'sky-citadel', 'twilight-frontier'],
    state: 'drift-noticed'
  },
  'sky-citadel': {
    id: 'sky-citadel',
    name: 'Sky Citadel',
    pillarFocus: ['discovery', 'harmony'],
    lanternNode: 'astra-spire',
    connectedRealms: ['arena-realm', 'crystal-forest', 'celestial-nexus'],
    state: 'drift-noticed'
  },
  'frozen-expanse': {
    id: 'frozen-expanse',
    name: 'Frozen Expanse',
    pillarFocus: ['memory', 'resilience'],
    lanternNode: 'borealis-keep',
    connectedRealms: ['twilight-frontier', 'memory-ocean', 'legacy-realm'],
    state: 'deep-drift'
  },
  'ember-depths': {
    id: 'ember-depths',
    name: 'Ember Depths',
    pillarFocus: ['growth', 'resilience'],
    lanternNode: 'hearthlight-core',
    connectedRealms: ['arena-realm', 'celestial-nexus', 'twilight-frontier'],
    state: 'restoration-active'
  },
  'twilight-frontier': {
    id: 'twilight-frontier',
    name: 'Twilight Frontier',
    pillarFocus: ['discovery', 'knowledge'],
    lanternNode: 'dusk-threshold',
    connectedRealms: ['crystal-forest', 'frozen-expanse', 'ember-depths', 'memory-ocean'],
    state: 'deep-drift'
  },
  'celestial-nexus': {
    id: 'celestial-nexus',
    name: 'Celestial Nexus',
    pillarFocus: ['harmony', 'discovery'],
    lanternNode: 'solstice-convergence',
    connectedRealms: ['sky-citadel', 'ember-depths', 'legacy-realm'],
    state: 'deep-drift'
  },
  'legacy-realm': {
    id: 'legacy-realm',
    name: 'Legacy Realm',
    pillarFocus: ['belonging', 'memory'],
    lanternNode: 'founders-hall',
    connectedRealms: ['celestial-nexus', 'frozen-expanse', 'memory-ocean'],
    state: 'restoration-active'
  },
  'memory-ocean': {
    id: 'memory-ocean',
    name: 'Memory Ocean',
    pillarFocus: ['memory', 'knowledge'],
    lanternNode: 'deep-archive',
    connectedRealms: ['frozen-expanse', 'twilight-frontier', 'legacy-realm'],
    state: 'deep-drift'
  }
};
```

---

## Harmony Index Calculation

### Core Formula
```
Harmony Index = Σ(Realm Pillar Score × Realm Weight) / Total Realms
```

Where:
- **Realm Pillar Score** = Average of 4 indicators (0-100 each)
- **Realm Weight** = 1.0 (all Realms equal — civilization is holistic)
- **Overall Index** = Average across all 7 Pillars across all 9 Realms

### Implementation
```javascript
function calculateHarmonyIndex(worldState) {
  const pillarScores = {};
  const realmCount = Object.keys(REALM_DEFINITIONS).length;
  
  // Initialize pillar accumulators
  Object.keys(PILLAR_DEFINITIONS).forEach(pillarId => {
    pillarScores[pillarId] = { total: 0, count: 0 };
  });
  
  // Calculate per-realm pillar scores
  Object.values(REALM_DEFINITIONS).forEach(realm => {
    Object.keys(PILLAR_DEFINITIONS).forEach(pillarId => {
      const pillarDef = PILLAR_DEFINITIONS[pillarId];
      const realmIndicators = getRealmIndicators(worldState, realm.id, pillarId);
      
      if (realmIndicators.length > 0) {
        const pillarScore = realmIndicators.reduce((sum, ind) => sum + ind.value * ind.weight, 0);
        pillarScores[pillarId].total += pillarScore;
        pillarScores[pillarId].count += 1;
      }
    });
  });
  
  // Average across realms
  const finalPillarScores = {};
  Object.keys(pillarScores).forEach(pillarId => {
    finalPillarScores[pillarId] = pillarScores[pillarId].count > 0 
      ? pillarScores[pillarId].total / pillarScores[pillarId].count 
      : 0;
  });
  
  // Overall index
  const overallIndex = Object.values(finalPillarScores).reduce((sum, v) => sum + v, 0) / 7;
  
  return {
    overall: Math.round(overallIndex),
    pillars: finalPillarScores,
    realms: calculateRealmStates(worldState)
  };
}
```

---

## Drift & Restoration Model (Threshold Mechanics)

### Weekly Update Cycle
```javascript
const DRIFT_FACTOR = 0.98; // 2% decay per week without restoration
const FESTIVAL_BONUS = {
  primary: 5,   // Primary pillar boost during festival week
  secondary: 2  // Secondary pillar boost
};

function weeklyHarmonyUpdate(worldState) {
  const updatedState = { ...worldState };
  
  Object.values(REALM_DEFINITIONS).forEach(realm => {
    Object.keys(PILLAR_DEFINITIONS).forEach(pillarId => {
      const indicatorKey = `${realm.id}.${pillarId}`;
      let currentValue = worldState.indicators[indicatorKey] || 50; // Default midpoint
      
      // Apply natural drift (Threshold model - generational decay)
      currentValue *= DRIFT_FACTOR;
      
      // Apply restoration contributions from this week
      const contributions = getWeeklyContributions(worldState, realm.id, pillarId);
      currentValue += calculateRestorationImpact(contributions, pillarId);
      
      // Apply festival bonuses
      const activeFestival = getActiveFestival(worldState.cycle);
      if (activeFestival && activeFestival.affectsPillar(pillarId)) {
        const isPrimary = activeFestival.primaryPillar === pillarId;
        currentValue += isPrimary ? FESTIVAL_BONUS.primary : FESTIVAL_BONUS.secondary;
      }
      
      // Apply Lantern Network resonance
      currentValue += calculateLanternResonance(worldState, realm.id, pillarId);
      
      // Apply companion stabilization
      currentValue += calculateCompanionStabilization(worldState, realm.id, pillarId);
      
      // Clamp
      currentValue = Math.max(0, Math.min(100, currentValue));
      
      updatedState.indicators[indicatorKey] = currentValue;
    });
  });
  
  // Update derived values
  updatedState.harmonyIndex = calculateHarmonyIndex(updatedState);
  updatedState.lanternSync = calculateLanternSync(updatedState);
  updatedState.cycle += 1;
  
  return updatedState;
}
```

### Restoration Impact Table
```javascript
const RESTORATION_IMPACTS = {
  // Puzzle completions (scaled by puzzle type → pillar alignment)
  'crystal-resonance': { knowledge: 1.5, discovery: 0.5 },
  'pathfinders-mark': { discovery: 1.5, knowledge: 0.5 },
  'echo-sequence': { memory: 1.5, belonging: 0.5 },
  'community-pattern': { belonging: 1.5, resilience: 1.0 },
  'verdance-cultivation': { growth: 1.5, knowledge: 0.5 },
  'fragment-assembly': { knowledge: 1.5, memory: 0.5 },
  'harmony-alignment': { harmony: 2.0, all: 0.3 },
  'legacy-seal': { memory: 2.0, belonging: 1.5, harmony: 1.0 },
  
  // Festival participation
  'festival-participation': { primary: 3, secondary: 1 },
  
  // Archive contributions
  'archive-fragment': { pillar: 1.5 },
  'archive-connection': { all: 0.5 },
  
  // Citizen Path milestones
  'mentor-graduate': { growth: 1.0, resilience: 1.0 },
  'scholar-publish': { knowledge: 1.5 },
  'harmonist-colead': { harmony: 1.0, belonging: 1.0 },
  'pathfinder-restore': { discovery: 1.5 },
  
  // Companion memories
  'companion-testimony': { memory: 1.5, pillar: 0.5 }
};

function calculateRestorationImpact(contributions, targetPillar) {
  let impact = 0;
  contributions.forEach(c => {
    const impacts = RESTORATION_IMPACTS[c.type] || {};
    if (impacts[targetPillar]) {
      impact += impacts[targetPillar];
    } else if (impacts.all) {
      impact += impacts.all;
    } else if (impacts.pillar && c.pillar === targetPillar) {
      impact += impacts.pillar;
    }
  });
  return impact;
}
```

---

## Companion Stabilization System

```javascript
const COMPANION_STABILIZATION = {
  'Spark': { pillar: 'knowledge', realm: 'crystal-forest', driftReduction: 0.5 },
  'Verdant': { pillar: 'growth', realm: 'crystal-forest', driftReduction: 0.5 },
  'Nimbus': { pillar: 'discovery', realm: 'sky-citadel', driftReduction: 0.5 },
  'Frostpaw': { pillar: 'memory', realm: 'frozen-expanse', driftReduction: 0.5 },
  'Prism': { pillar: 'harmony', realm: 'celestial-nexus', driftReduction: 0.25, allPillarsVariance: 0.25 },
  'Bloomtail': { pillar: 'belonging', realm: 'arena-realm', driftReduction: 0.5 },
  'Galewing': { pillar: 'discovery', realm: 'sky-citadel', lanternSyncBoost: 0.1 },
  'Echo': { pillar: 'memory', realm: 'frozen-expanse', memoryContributionBoost: 0.25 }
};

function calculateCompanionStabilization(worldState, realmId, pillarId) {
  let stabilization = 0;
  Object.values(COMPANION_STABILIZATION).forEach(comp => {
    if (comp.realm === realmId && comp.pillar === pillarId) {
      // Companion presence reduces drift for their pillar in their realm
      const baseDrift = worldState.indicators[`${realmId}.${pillarId}`] * (1 - DRIFT_FACTOR);
      stabilization += baseDrift * comp.driftReduction;
    }
    if (comp.allPillarsVariance && pillarId === 'harmony') {
      stabilization += 0.1; // Prism reduces harmony variance
    }
    if (comp.lanternSyncBoost && pillarId === 'discovery') {
      stabilization += 0.2; // Galewing boosts lantern sync
    }
    if (comp.memoryContributionBoost && pillarId === 'memory') {
      stabilization += 0.3; // Echo boosts memory contributions
    }
  });
  return stabilization;
}
```

---

## Lantern Network Visualization

### Lantern Sync Calculation
```javascript
function calculateLanternSync(worldState) {
  const syncLevels = {};
  
  Object.values(REALM_DEFINITIONS).forEach(realm => {
    // Lantern sync = average of Discovery + Knowledge pillars for that realm
    const discovery = worldState.harmonyIndex.pillars.discovery || 0;
    const knowledge = worldState.harmonyIndex.pillars.knowledge || 0;
    const realmDiscovery = worldState.indicators[`${realm.id}.discovery`] || 0;
    const realmKnowledge = worldState.indicators[`${realm.id}.knowledge`] || 0;
    
    syncLevels[realm.id] = Math.round((realmDiscovery + realmKnowledge) / 2);
  });
  
  // Global convergence = all 9 lanterns within 10 points of each other
  const values = Object.values(syncLevels);
  const variance = Math.max(...values) - Math.min(...values);
  const isConvergence = variance <= 10;
  
  return {
    perRealm: syncLevels,
    globalConvergence: isConvergence,
    variance: variance
  };
}
```

### Pulse Visualization Spec
```javascript
const LANTERN_PULSE_VISUALS = {
  // Pulse frequency based on sync level
  getPulseInterval: (syncLevel) => {
    // 90-100: steady (2s interval)
    // 75-89: strong (1.5s)
    // 60-74: visible (1s)
    // 40-59: flickering (0.7s)
    // 20-39: dim (0.5s)
    // 0-19: barely visible (0.3s)
    if (syncLevel >= 90) return 2000;
    if (syncLevel >= 75) return 1500;
    if (syncLevel >= 60) return 1000;
    if (syncLevel >= 40) return 700;
    if (syncLevel >= 20) return 500;
    return 300;
  },
  
  // Pulse color based on dominant pillar
  getPulseColor: (realmId, worldState) => {
    const pillars = ['knowledge', 'discovery', 'growth', 'memory', 'resilience', 'harmony', 'belonging'];
    let maxPillar = 'knowledge';
    let maxValue = 0;
    
    pillars.forEach(p => {
      const val = worldState.indicators[`${realmId}.${p}`] || 0;
      if (val > maxValue) {
        maxValue = val;
        maxPillar = p;
      }
    });
    
    return PILLAR_DEFINITIONS[maxPillar].color;
  },
  
  // Convergence effect
  convergenceEffect: {
    trigger: 'all 9 lanterns within 10 points',
    duration: '2 weeks (Convergence Celebration)',
    visual: 'All lanterns pulse in perfect unison with rainbow harmonics',
    harmonyIndexBoost: { all: 3, harmony: 5 }
  }
};
```

---

## Qualitative Feedback System (No Numbers to Player)

### Archive Description Generator
```javascript
function getArchiveDescription(harmonyIndex) {
  const overall = harmonyIndex.overall;
  
  if (overall >= 90) return {
    text: "First Harmony peak — the civilization thrives in perfect alignment.",
    tone: "vibrant"
  };
  if (overall >= 75) return {
    text: "Restoration advancing — the drift is being pushed back across all Realms.",
    tone: "hopeful"
  };
  if (overall >= 60) return {
    text: "Drift noticed, work underway — some Realms thrive while others struggle.",
    tone: "mixed"
  };
  if (overall >= 40) return {
    text: "Threshold approached — the Lanterns flicker. The work is urgent.",
    tone: "quiet"
  };
  if (overall >= 20) return {
    text: "Deep drift — memories fade, routes close, communities isolate.",
    tone: "fragile"
  };
  return {
    text: "Shattering imminent — the civilization's systems have nearly failed.",
    tone: "dark"
  };
}
```

### Realm Feel Generator
```javascript
function getRealmFeel(realmId, worldState) {
  const pillars = ['knowledge', 'discovery', 'growth', 'memory', 'resilience', 'harmony', 'belonging'];
  let avgScore = 0;
  let count = 0;
  
  pillars.forEach(p => {
    const val = worldState.indicators[`${realmId}.${p}`];
    if (val !== undefined) {
      avgScore += val;
      count++;
    }
  });
  
  avgScore = count > 0 ? avgScore / count : 50;
  
  if (avgScore >= 90) return "Vibrant, connected, alive with purpose";
  if (avgScore >= 75) return "Hopeful, active, healing — restoration visible";
  if (avgScore >= 60) return "Mixed — some districts thriving, others quiet";
  if (avgScore >= 40) return "Quiet, isolated, fragile — Lanterns dim";
  if (avgScore >= 20) return "Cold, silent, memories fading into frost";
  return "Dark, disconnected, lost to the drift";
}
```

---

## MVP Scope (Arena Realm First Slice)

### Included in MVP
| Feature | Implementation |
|---------|----------------|
| Great Archive Display | ✅ 3 Pillars (Knowledge, Resilience, Belonging) |
| Lantern Pulse Visual | ✅ Arena Realm + 2 connected Realms |
| Realm Map Overlay | ❌ Post-launch |
| All 7 Pillars Tracked | ✅ (Arena + Crystal Forest + Sky Citadel) |
| Weekly Update Simulation | ✅ Offline calculation |
| Festival Integration | ✅ Threshold Renewal only |
| Citizen Path Impact | ❌ Post-launch |
| Companion Stabilization | ❌ Post-launch (Spark, Prism only visual) |

### MVP Harmony Index State
```javascript
const MVP_INITIAL_STATE = {
  cycle: 1,
  harmonyIndex: {
    overall: 58,
    pillars: {
      knowledge: 62,
      discovery: 45,
      growth: 38,
      memory: 41,
      resilience: 65,
      harmony: 52,
      belonging: 58
    }
  },
  indicators: {
    // Arena Realm (focus)
    'arena-realm.knowledge': 55,
    'arena-realm.discovery': 50,
    'arena-realm.growth': 40,
    'arena-realm.memory': 45,
    'arena-realm.resilience': 70,
    'arena-realm.harmony': 55,
    'arena-realm.belonging': 65,
    // Crystal Forest (connected)
    'crystal-forest.knowledge': 65,
    'crystal-forest.discovery': 40,
    'crystal-forest.growth': 45,
    // Sky Citadel (connected)
    'sky-citadel.discovery': 55,
    'sky-citadel.knowledge': 50,
    'sky-citadel.harmony': 45
  }
};
```

---

## Implementation Checklist

| Component | Status |
|-----------|--------|
| Pillar definitions & indicators | ☐ |
| Realm definitions | ☐ |
| Index calculation formula | ☐ |
| Drift factor (0.98/week) | ☐ |
| Restoration impact table | ☐ |
| Festival bonus system | ☐ |
| Companion stabilization | ☐ |
| Lantern sync calculation | ☐ |
| Pulse visualization specs | ☐ |
| Qualitative feedback (Archive/Realm) | ☐ |
| MVP initial state | ☐ |
| Weekly update function | ☐ |
| **No player-facing numbers** | ☐ HARD CONSTRAINT |
| **Index can decline** | ☐ HARD CONSTRAINT |
| **No "maxed out" state** | ☐ HARD CONSTRAINT |
| **Drift continues without restoration** | ☐ HARD CONSTRAINT |

---

## Conflict Log Entry

**Conflict 41: Harmony Index Mechanics Specification** — **RESOLVED**  
Full system specified with canon-aligned drift/restoration model, qualitative Guardian feedback, festival/citizen/companion integration, and MVP scope. No player-facing numbers, no power escalation, no "maxed out" state.