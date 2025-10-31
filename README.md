# OmniMeta Saga Universe — Git Repository

**Version**: 2.0  
**Created**: October 31, 2025  
**Purpose**: Complete knowledge base for the 30-novella OmniMeta Saga  
**Usage**: Foundation for Perplexity Space to generate novella-specific bibles and Custom GPT prompts  

---

## OVERVIEW

This repository contains all foundational knowledge, character documentation, and structural timelines for the **OmniMeta Saga** — a 30-novella science-fantasy epic spanning six Turnings (GLASS, CRACK, FORGE, SMELT, CLEAR, BREAK).

The repository is designed to support a **three-tier writing system**:

1. **Git Repository** (this) → Contains all canon, world-building, character dossiers, structural timelines
2. **Perplexity Space** → Queries this repo to dynamically generate novella-specific bibles and prompts
3. **30 Custom GPTs** → Each configured with its novella bible to write prose

---

## REPOSITORY STRUCTURE

```
omnimeta-saga-universe/
├── README.md                           # This file
├── SourceMap_Git.md                    # File manifest and descriptions
├── docs/
│   └── NEXT_CONVERSATION_INSTRUCTIONS.md
│
├── 01_Foundation/                      # Immutable canon and world-building
│   ├── 01_Canon/
│   │   └── Canon_Innocent_Master_v2_CORRECTED.md
│   ├── 02_Magic/
│   │   └── Soulpulse_Core_v2.md
│   └── 03_World/
│       ├── TeOga_Physical_Pierced_CORRECTED.md
│       ├── Catastrophes_Escalation_v2_CORRECTED.md
│       ├── Lexicon_Temporal_TeOga.md
│       └── Forbidden_Modern_Terms_TeOga_Alternatives.md
│
├── 02_Character_Dossiers/              # Character bibles (innocent + guilty frames)
│   ├── INNOCENT_FRAME/
│   │   ├── Dossier_Jhace_Torrins_Innocent.md
│   │   ├── Dossier_Tiffani_Merrow_Innocent.md
│   │   ├── Dossier_Crew_Secondary_Innocent.md
│   │   ├── Dossier_God_Vessels_Innocent.md
│   │   └── Dossier_Recurring_Characters_Innocent.md
│   └── GUILTY_FRAME/
│       ├── Dossier_Tiffani_Merrow_Guilty.md
│       ├── Dossier_Jhace_Torrins_Guilty.md
│       └── Dossier_God_Vessels_Guilty.md
│
├── 03_Structural_Timelines/            # Progression tracking across all 30 novellas
│   ├── 01_Progression_Timeline_Master.md
│   ├── 02_Beat_Unpredictability_System.md
│   ├── 03_Character_Arc_Tracker.md
│   ├── 04_Crisis_Escalation_Map.md
│   ├── 05_Soulpulse_Capacity_Progression.md
│   ├── 06_Relationship_Evolution_Timeline.md
│   ├── 07_God_Vessel_Faction_Timeline.md
│   └── 08_Interlude_Placement_Logic.md
│
├── 04_Writer_Deliverables/             # Prose engine prompts (N1 example included)
│   └── PROSE_ENGINES/
│       └── N1_Prose_Engine_Prompt.md
│
└── 05_Perplexity_Space_Instructions/   # Instructions for dynamic bible/prompt generation
    ├── Bible_Generation_Instructions.md
    └── Prompt_Generation_Instructions.md
```

---

## KEY CONCEPTS

### Dual-Canon Architecture

The saga operates on two narrative layers:

**INNOCENT FRAME** (N1–N29):
- What characters experience
- Crises appear organic
- Tiffani is genuine partner who dies in N5
- Jhace is survivor forced into mastery
- Gods awaken naturally during Fathombreak

**GUILTY FRAME** (N30 revelation):
- What the Auditor orchestrated
- Crises were engineered
- Tiffani is extradimensional observer who staged death
- Jhace was forged as weapon
- Gods were awakened deliberately

**Writer GPTs only access INNOCENT FRAME** (except N30 GPT, which requires guilty truth).

---

### Beat Unpredictability System

Narrative structure varies unpredictably across all novellas:
- 30+ beat methods in repertoire
- No consecutive repeats
- No rotation patterns
- No sequence repeats
- Readers cannot predict delivery method, only content escalation

---

### Soulpulse Magic System

**Principles**:
- Wholeness (integration, healing, organic connection)
- Form (geometry, structure, perfection)
- Purity (separation, cleansing, isolation)
- Entropy (dissolution, release, acceptance)

**Jhace's Progression**:
- N1: Wholeness (instinctive)
- N2: Dual-principle (Wholeness + Form)
- N5: Four-principle simultaneity (Confluence weapon)
- N29: Fivefold stasis (all four + Confluence)

**Cost**:
- Immediate: Tremor, exhaustion
- Cumulative: Vein-burn (visible scarring)
- Terminal: Hollowing (neurological collapse)

---

### God-Vessels

Four mortals transformed into divine embodiments during Fathombreak (N5):
- **Xilcore/Corlexi** (Form) — Perfection through geometric correction
- **Leesa/Salee** (Wholeness) — Compassion through forced integration
- **Blemo/Mobel** (Purity) — Cleansing through purge operations
- **Seeri/Eries** (Entropy) — Peace through acceptance of dissolution

Each builds faction, spreads doctrine, escalates toward Battle Royale (N26–N29).

---

## USAGE GUIDE

### For Perplexity Space

1. **Read** `05_Perplexity_Space_Instructions/Bible_Generation_Instructions.md`
2. **Query** repository files to generate novella-specific bible
3. **Read** `05_Perplexity_Space_Instructions/Prompt_Generation_Instructions.md`
4. **Generate** Custom GPT prose engine prompt
5. **Deliver** bible + prompt to user for Custom GPT configuration

### For Custom GPT Configuration

1. **Receive** novella bible + prose engine prompt from Perplexity Space
2. **Configure** Custom GPT with:
   - System prompt = Prose engine prompt
   - Knowledge files = Foundation files + character dossiers + novella bible
3. **Write** prose chapter-by-chapter
4. **Share** completed chapters back to Perplexity Space for consistency validation

### For Manual Reference

All files are human-readable Markdown. Query any file directly for:
- Canon questions → `01_Foundation/01_Canon/`
- Character status → `02_Character_Dossiers/` or `03_Structural_Timelines/03_Character_Arc_Tracker.md`
- Plot events → `03_Structural_Timelines/01_Progression_Timeline_Master.md`
- Crisis timeline → `03_Structural_Timelines/04_Crisis_Escalation_Map.md`

---

## INNOCENCE PROTOCOL

**Critical**: Writer GPTs must NOT access guilty-frame files (except N30).

**Innocent-frame files** (safe for all Writer GPTs):
- All `01_Foundation/` files
- All `02_Character_Dossiers/INNOCENT_FRAME/` files
- All `03_Structural_Timelines/` files (contain both frames but clearly labeled)

**Guilty-frame files** (N30 ONLY):
- `02_Character_Dossiers/GUILTY_FRAME/` files
- Orchestration truth in structural timelines (clearly marked)

**Enforcement**: Perplexity Space must filter file references when generating bibles/prompts for N1–N29.

---

## CONTINUITY CONSTRAINTS

All novellas must honor:
- **Deaths are permanent** (except Tiffani's staged death in N5)
- **Physical degradation accumulates** (Jhace's hands, Tiffani's vein-burn)
- **Soulpulse capacity only increases** (never decreases or resets)
- **Relationships evolve** (cannot regress without cause)
- **World-state changes persist** (infrastructure doesn't magically repair)

Track continuity via:
- `03_Structural_Timelines/03_Character_Arc_Tracker.md` (who's alive, who's dead)
- `03_Structural_Timelines/05_Soulpulse_Capacity_Progression.md` (Jhace's power level)
- Previous novella bibles (immutable facts from earlier books)

---

## TURNING STRUCTURE

**GLASS (N1–N5)**: Catastrophe → Chronic Crisis → Apocalypse  
- N1: The Piercing, Soulpulse awakens
- N5: Fathombreak, gods awaken, Tiffani dies

**CRACK (N6–N10)**: Rebuilding → Faction Emergence → Attrition  
- N6: Marisse appears, resistance forms
- N9: Chloen dies

**FORGE (N11–N15)**: Ideological Wars → Siege  
- N11: First god-vessel confrontations
- N15: Major siege, Kylar dies

**SMELT (N16–N20)**: Grinding Attrition → Stalemate  
- N17: Selwin defects
- N20: Jessa dies, breaking point

**CLEAR (N21–N25)**: Final Preparation → Convergence  
- N22: Rennik dies
- N25: All factions converge

**BREAK (N26–N30)**: Battle Royale → Universe Collapse  
- N29: Fivefold stasis achieved
- N30: Orchestration revealed, reality collapses

---

## FILE MANIFEST SUMMARY

**Total Files**: 30+  
**Foundation Files**: 6  
**Character Dossiers**: 8 (5 innocent, 3 guilty)  
**Structural Timelines**: 8  
**Prose Engine Prompts**: 1 (N1 example; Perplexity Space generates remaining 29)  
**Instructions**: 2 (Bible generation, Prompt generation)  

---

## VERSION HISTORY

**v1.0** (Initial): Foundation files only  
**v2.0** (Current): Complete repository with all structural timelines and Perplexity Space instructions  

---

## CONTACT & SUPPORT

For questions about this repository structure or usage:
- Refer to `SourceMap_Git.md` for detailed file descriptions
- Refer to `docs/NEXT_CONVERSATION_INSTRUCTIONS.md` for workflow guidance
- Refer to `05_Perplexity_Space_Instructions/` for generation procedures

---

**END README**

This repository is the complete knowledge base for the OmniMeta Saga. All 30 novellas can be generated from these files.
