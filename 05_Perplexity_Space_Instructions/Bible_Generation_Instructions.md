# BIBLE GENERATION INSTRUCTIONS FOR PERPLEXITY SPACE

**Document Version**: 1.0  
**Created**: October 31, 2025  
**Purpose**: Instructions for Perplexity Space to dynamically generate novella-specific bibles  
**Output**: One comprehensive bible per novella (N1–N30)  

---

## OVERVIEW

The Perplexity Space will generate **30 novella-specific bibles** by querying the omnimeta-saga-universe Git repository and synthesizing information from multiple source documents.

Each bible provides everything a Custom GPT needs to write that specific novella:
- World state at novella start
- Character arcs for that novella
- Major plot events and beats
- Crisis escalation details
- Soulpulse capacity status
- Relationship dynamics
- Interlude specifications
- Continuity constraints from previous novellas

---

## BIBLE STRUCTURE TEMPLATE

Each novella bible should follow this structure:

```markdown
# NOVELLA [N#] BIBLE: [TITLE]

## WORLD STATE
[Current state of Te'Oga, infrastructure, factions, crisis level]

## CHARACTER STATUS
### Jhace Torrins
[Arc for this novella, Soulpulse capacity, physical state, relationships]

### [Other Major Characters]
[Status, arc, role in this novella]

## PLOT OVERVIEW
[Major events, turning points, crisis escalation]

## CHAPTER BEATS
[15 chapters with beat method assignments, emotional arcs, key scenes]

## INTERLUDES
[2 interludes with god-vessel assignments, placement, methodology]

## CONTINUITY CONSTRAINTS
[Immutable facts from previous novellas that must be honored]

## PROSE GUIDELINES
[Voice, style, cost visibility, world-building requirements]
```

---

## SOURCE DOCUMENTS TO QUERY

For each novella bible, query these repository files:

### Foundation Files (01_Foundation/)
- `Canon_Innocent_Master_v2_CORRECTED.md` — Innocent-frame canon
- `Soulpulse_Core_v2.md` — Magic system mechanics
- `TeOga_Physical_Pierced_CORRECTED.md` — World geography
- `Catastrophes_Escalation_v2_CORRECTED.md` — Crisis timeline
- `Lexicon_Temporal_TeOga.md` — Vocabulary
- `Forbidden_Modern_Terms_TeOga_Alternatives.md` — Language constraints

### Character Dossiers (02_Character_Dossiers/)
- `INNOCENT_FRAME/Dossier_Jhace_Torrins_Innocent.md`
- `INNOCENT_FRAME/Dossier_Tiffani_Merrow_Innocent.md`
- `INNOCENT_FRAME/Dossier_Crew_Secondary_Innocent.md`
- `INNOCENT_FRAME/Dossier_God_Vessels_Innocent.md`
- `INNOCENT_FRAME/Dossier_Recurring_Characters_Innocent.md`

**DO NOT query GUILTY_FRAME files** (except for N30 bible, which requires orchestration truth)

### Structural Timelines (03_Structural_Timelines/)
- `01_Progression_Timeline_Master.md` — What happens when across all novellas
- `02_Beat_Unpredictability_System.md` — Beat method repertoire and constraints
- `03_Character_Arc_Tracker.md` — Character status and transformations
- `04_Crisis_Escalation_Map.md` — Catastrophe timeline
- `05_Soulpulse_Capacity_Progression.md` — Jhace's power growth
- `06_Relationship_Evolution_Timeline.md` — Relationship developments
- `07_God_Vessel_Faction_Timeline.md` — God-vessel activities
- `08_Interlude_Placement_Logic.md` — Interlude positioning rules

---

## GENERATION PROCESS

### Step 1: Identify Novella Scope
- Determine which novella (N1–N30) is being generated
- Identify Turning (GLASS, CRACK, FORGE, SMELT, CLEAR, BREAK)
- Note position in Turning (1st, 2nd, 3rd, 4th, or 5th book)

### Step 2: Query World State
From `01_Progression_Timeline_Master.md` and `04_Crisis_Escalation_Map.md`:
- What happened in previous novellas?
- What is current crisis level?
- What factions exist?
- What infrastructure remains?

### Step 3: Query Character Status
From `03_Character_Arc_Tracker.md` and `05_Soulpulse_Capacity_Progression.md`:
- Who is alive?
- Who died in previous novellas?
- What is Jhace's Soulpulse capacity?
- What is Jhace's physical state (hands, vein-burn)?
- What relationships exist?

### Step 4: Query Plot Events
From `01_Progression_Timeline_Master.md`:
- What major events occur in this novella?
- What character transformations happen?
- What deaths occur?
- What crises escalate?

### Step 5: Generate Chapter Beats
From `02_Beat_Unpredictability_System.md`:
- Review last novella's beat sequence (prevent patterns)
- Filter beat repertoire by constraints
- Select 15 beats for this novella's chapters
- Ensure no consecutive repeats
- Ensure no rotation patterns
- Ensure emotional arc variation

### Step 6: Determine Interlude Placement
From `08_Interlude_Placement_Logic.md`:
- Review last novella's interlude placement
- Select new placement (vary from previous)
- Choose build-up or break-down methodology
- Assign god-vessels (rotate through all four)

### Step 7: Identify Continuity Constraints
From previous novella bibles and character trackers:
- What facts are immutable? (deaths, transformations, commitments)
- What physical states must continue? (Jhace's hands, Tiffani's vein-burn)
- What relationships must be honored?

### Step 8: Compile Bible
Synthesize all queried information into comprehensive novella bible following template structure.

---

## EXAMPLE: GENERATING N2 BIBLE

### Step 1: Identify Scope
- **Novella**: N2 (GLASS Turning, Book 2 of 5)
- **Title**: Stress and Fracture

### Step 2: World State
Query `01_Progression_Timeline_Master.md` → N2 section:
- Post-Piercing world (N1 aftermath)
- Infrastructure degraded despite N1 repairs
- Stress-riser from N1 overwork threatens collapse
- God-vessels not yet awakened (N5 event)

### Step 3: Character Status
Query `03_Character_Arc_Tracker.md` → Jhace N2:
- **Arc**: Teacher → Coordinator → Reluctant Leader
- **Soulpulse**: Dual-principle competence (Wholeness + Form)
- **Physical**: Tremor worsens, minimal vein-burn
- **Relationships**: Deepening with Tiffani, teaching Chloen and others

Query `03_Character_Arc_Tracker.md` → Others:
- **Tiffani**: Alive, vein-burn 3.5cm → 4cm
- **Chloen**: Competent apprentice
- **Bram**: Alive (dies N3)
- **Kylar**: Still rival (converts N3)

### Step 4: Plot Events
Query `01_Progression_Timeline_Master.md` → N2:
- Stress-riser crisis
- Jhace coordinates multiple crews
- Tiffani confesses Senna's death
- Teaching expands
- Infrastructure degradation continues

### Step 5: Chapter Beats
Query `02_Beat_Unpredictability_System.md`:
- Review N1 beat sequence (avoid repeating)
- Select 15 beats ensuring no consecutive repeats
- Example sequence:
  1. Break-Down (Post-Crisis Consequences)
  2. Pattern Analysis → Strategic Planning → Execution
  3. Intimacy → Vulnerability → Connection Deepened
  4. Trial → Failure → Compounding → Success/Cost
  5. Sabotage Reveal → Trust Fracture → Repair
  [etc.]

### Step 6: Interlude Placement
Query `08_Interlude_Placement_Logic.md`:
- N1 placed interludes after Ch.3 and Ch.11
- N2 should vary: After Ch.4 and Ch.12
- Methodology: Build-up (Ch.4), Break-down (Ch.12)
- God-vessels: Xilcore (Ch.4), Blemo (Ch.12)

### Step 7: Continuity Constraints
From N1 bible and character tracker:
- Jhace's hands: Callused, tremor present (cannot heal)
- Tiffani's vein-burn: 3.5cm at N1 end, worsens to 4cm by N2 end
- Chloen: Learning velding (cannot suddenly be expert)
- Bram: Alive (must survive N2, dies N3)
- Relationship: Jhace + Tiffani committed (N1 Ch.15)

### Step 8: Compile Bible
Synthesize into N2 bible document with all sections filled.

---

## SPECIAL CASES

### N1 Bible
- No previous novellas to reference
- Establish all baseline states
- Introduce all mechanics
- Set tone for entire saga

### N5 Bible
- Fathombreak (apocalyptic event)
- Tiffani's staged death
- God-vessels awaken
- Jhace becomes Confluence weapon
- Only one interlude pair + Auditor Epilogue

### N30 Bible
- **REQUIRES GUILTY_FRAME FILES**
- Tiffani returns, reveals Auditor identity
- Orchestration confession
- Universe collapse
- Final exchange between Jhace and Tiffani

---

## QUALITY CONTROL

Each generated bible must:
- ✅ Honor all continuity constraints from previous novellas
- ✅ Use beat methods that don't repeat consecutively
- ✅ Place interludes at different chapters than previous novella
- ✅ Reflect accurate Soulpulse capacity for Jhace
- ✅ Show correct physical degradation (hands, vein-burn)
- ✅ Include only living characters (track deaths)
- ✅ Maintain innocent-frame protocol (no orchestration hints except N30)
- ✅ Reference correct foundation files
- ✅ Provide 15 chapter beats + 2 interludes

---

## OUTPUT FORMAT

Save each bible as:
```
N[##]_Bible_[TITLE].md
```

Examples:
- `N01_Bible_The_Line_That_Holds.md`
- `N02_Bible_Stress_and_Fracture.md`
- `N30_Bible_Revelation_and_Collapse.md`

---

**END BIBLE GENERATION INSTRUCTIONS**

**File Location**: `omnimeta-saga-universe/05_Perplexity_Space_Instructions/Bible_Generation_Instructions.md`  
**Usage**: Perplexity Space uses these instructions to dynamically generate novella-specific bibles by querying the Git repository
