# OmniMeta Saga Universe — Perplexity Space Knowledge Base

**Document Version**: 4.0 (Post-Acrostic Audit)
**Created**: November 4, 2025
**Author**: Manus AI
**Purpose**: Complete, audited, and optimized knowledge base for the 30-novella OmniMeta Saga. This document serves as the primary ingestion source for the Perplexity Space to ensure continuity and accurate generation of Story Bibles and prose.
**Protocol**: All content is structured for maximum machine readability and minimal ambiguity.

---

## 1. OVERVIEW AND ACROSTIC STRUCTURE (IMMUTABLE CANON)

This repository contains the complete foundational knowledge, character documentation, and structural timelines for the **OmniMeta Saga** — a 30-novella science-fantasy epic spanning six Turnings. The entire narrative is built upon a **hidden acrostic structure** that dictates the title of each novella and represents the central metalworking metaphor.

### The Six Turnings (Metalworking Metaphor)

The first letter of each novella title in a turning spells a word representing the metalworking process applied to the protagonist, Jhace Torrins, who is being forged as a weapon through orchestrated catastrophe.

| Turning | Novellas | Acrostic | Metaphor |
| :--- | :--- | :--- | :--- |
| **1. GLASS** | N01–N05 | G-L-A-S-S | Fragile, transparent, newly formed (Soulpulse awakens, world is brittle) |
| **2. CRACK** | N06–N10 | C-R-A-C-K | Fractures spread, stress accumulates (factions form, world splinters) |
| **3. FORGE** | N11–N15 | F-O-R-G-E | Heat and hammering, shaping through violence (god wars, Jhace forged as weapon) |
| **4. SMELT** | N16–N20 | S-M-E-L-T | Melting down, refining through extreme heat (attrition, casualties mount) |
| **5. CLEAR** | N21–N25 | C-L-E-A-R | Purified, transparent, ready for final use (final preparation, convergence) |
| **6. BREAK** | N26–N30 | B-R-E-A-K | Shattering, collapse, revelation (battle royale, universe breaks, truth revealed) |

### Audited Novella Titles (N01–N30)

The following list contains the **audited and corrected** novella titles. All Perplexity Space operations must use these titles for file naming, internal references, and prose generation.

| Novella | Acrostic | Title |
| :--- | :--- | :--- |
| N01 | G | Grip That Holds |
| N02 | L | Light Cracks Through |
| N03 | A | Alloy Folded Wrong |
| N04 | S | Shatter From Heat |
| N05 | S | Steal Breaks Open |
| N06 | C | Called From Refuge |
| N07 | R | Resonance Awakens |
| N08 | A | Adaptation's Cost |
| N09 | C | Creation's Test |
| N10 | K | Knowledge Demanded |
| N11 | F | Forging the Sacred |
| N12 | O | Order Sought |
| N13 | R | Resistance Grows |
| N14 | G | Gods Entrench |
| N15 | E | Escalation Burns |
| N16 | S | Separation Deepens |
| N17 | M | Material Degradation |
| N18 | E | Erosion's Edge |
| N19 | L | Losses Mount |
| N20 | T | Threshold Approached |
| N21 | C | Convergence Rising |
| N22 | L | Loyalty Tested |
| N23 | E | Each Faction Stands |
| N24 | A | Armistice Failing |
| N25 | R | Reckoning Ready |
| N26 | B | Breaking Point Reached |
| N27 | R | Revelation Unfolds |
| N28 | E | Echoes End |
| N29 | A | Apex of Stasis |
| N30 | K | Knowing Everything |

---

## 2. REPOSITORY STRUCTURE (PERPLEXITY SPACE MAPPING)

The repository is organized into five primary directories, each serving a specific function in the Perplexity Space's generation workflow.

| Path | Purpose | Content Protocol |
| :--- | :--- | :--- |
| `01_Foundation/` | **Immutable World Canon**: Core, unchangeable rules for the saga. | **MUST** be ingested by all GPTs. Provides the absolute truth of the world. |
| `02_Character_Dossiers/` | **Character Bibles**: Detailed psychological and physical profiles. | **MUST** be filtered by `INNOCENT_FRAME/` for N01-N29. `GUILTY_FRAME/` is reserved for N30 only. |
| `03_Structural_Timelines/` | **Continuity Ledger**: Tracks all major plot beats, character states, and crisis escalation across all 30 novellas. | **MUST** be queried before generating any Bible or prose to ensure continuity. |
| `04_Writer_Deliverables/` | **Generation Assets**: Contains the Bible files and Prose Engine prompts. | **Primary Target** for Bible generation. Placeholder files are the **prompts** themselves. |
| `05_Perplexity_Space_Instructions/` | **Workflow Documentation**: Guides for the Perplexity Space's operational procedures. | **Reference Only**. Contains meta-instructions for the generation process. |

### Detailed Directory Mapping

#### `01_Foundation/` (Immutable Canon)

| File/Directory | Description for Perplexity Space | Usage Protocol |
| :--- | :--- | :--- |
| `01_Canon/` | Contains the single source of truth for the saga's lore. | **HIGH PRIORITY INGESTION**. |
| `Canon_Innocent_Master_v2_CORRECTED.md` | The complete, innocent-frame narrative canon. | **MANDATORY** for all generation tasks (N01-N30). |
| `02_Magic/` | Defines the Soulpulse magic system. | **HIGH PRIORITY INGESTION**. |
| `Soulpulse_Core_v2.md` | Detailed mechanics, principles (Wholeness, Form, Purity, Entropy), and cost (Vein-burn, Hollowing). | **MANDATORY** for all generation tasks. |
| `03_World/` | Defines the physical world of Te'Oga and its history. | **HIGH PRIORITY INGESTION**. |
| `TeOga_Physical_Pierced_CORRECTED.md` | Physical description of the world, including the wound from The Piercing. | **MANDATORY** for all world-building and setting descriptions. |
| `Catastrophes_Escalation_v2_CORRECTED.md` | Timeline of major world-level crises. | **MANDATORY** for tracking crisis escalation. |
| `Lexicon_Temporal_TeOga.md` | Approved vocabulary and terminology for the world. | **MANDATORY** for prose generation to maintain voice. |
| `Forbidden_Modern_Terms_TeOga_Alternatives.md` | List of anachronistic terms and their approved in-world alternatives. | **MANDATORY** for prose generation to enforce language constraints. |

#### `02_Character_Dossiers/` (Character Bibles)

| File/Directory | Description for Perplexity Space | Usage Protocol |
| :--- | :--- | :--- |
| `INNOCENT_FRAME/` | Character profiles consistent with the innocent-frame narrative. | **MANDATORY** for all generation tasks (N01-N29). |
| `Dossier_Jhace_Torrins_Innocent.md` | Protagonist's profile (competent survivor, reluctant leader). | **MANDATORY** for all generation tasks. |
| `Dossier_Tiffani_Merrow_Innocent.md` | Tiffani's profile (mysterious partner, tragic loss). | **MANDATORY** for all generation tasks. |
| `GUILTY_FRAME/` | Character profiles containing the orchestrated truth. | **FORBIDDEN** for N01-N29. **MANDATORY** for N30 generation only. |
| `Dossier_Tiffani_Merrow_Guilty.md` | Tiffani's profile as the Auditor. | **N30 ONLY**. |

#### `03_Structural_Timelines/` (Continuity Ledger)

| File/Directory | Description for Perplexity Space | Usage Protocol |
| :--- | :--- | :--- |
| `01_Progression_Timeline_Master.md` | **Master Ledger**: Tracks all major plot events, character arcs, and crisis escalation across all 30 novellas. **UPDATED with corrected titles.** | **MANDATORY QUERY** before generating any Bible to ensure beat-by-beat continuity. |
| `09_Story_Spine_Mapping_Innocent.md` | **Civic-Ledger Spine**: Tracks the immutable core events (deaths, capacity changes, world state) that cannot be retconned. **UPDATED with corrected titles.** | **MANDATORY QUERY** for all continuity checks. |
| `02_Beat_Unpredictability_System.md` | Defines the narrative structure variation for each novella. | **MANDATORY** for prose generation to select the correct beat method. |
| `03_Character_Arc_Tracker.md` | Detailed tracking of psychological and emotional state changes for key characters. | **MANDATORY QUERY** for character consistency. |
| `04_Crisis_Escalation_Map.md` | Tracks the rising severity of world-level crises. | **MANDATORY QUERY** for setting the correct narrative tension. |

#### `04_Writer_Deliverables/` (Generation Assets)

| File/Directory | Description for Perplexity Space | Usage Protocol |
| :--- | :--- | :--- |
| `02_Bibles/` | Contains the 30 Story Bible files. **All files are now corrected and up-to-date.** | **PRIMARY TARGET**. Each file is a **placeholder-prompt** that must be overwritten with the completed 13-section Story Bible upon generation. |
| `N##_Bible_TITLE.md` | The placeholder file for a specific novella. Contains the prompt, innocence protocol, and links to all previous completed Bibles. | **MANDATORY INGESTION** for the prompt. **MANDATORY OVERWRITE** upon completion. |
| `PROSE_ENGINES/` | Contains the system prompts for the prose-writing GPTs. | **SECONDARY TARGET**. Ingested by the prose-writing GPT after the Bible is generated. |
| `N1_Prose_Engine_Prompt.md` | The detailed system prompt for generating the N1 novella prose. **UPDATED with corrected title.** | **MANDATORY INGESTION** for N1 prose generation. |

---

## 3. BIBLE GENERATION PROTOCOL (WORKFLOW)

The Perplexity Space must adhere to the following workflow to maintain continuity and the integrity of the saga.

### A. Progressive Linking System (Continuity Chain)

Each Bible placeholder links to **ALL** previous completed Bibles. This creates a continuity chain that ensures every new Bible is generated with full context of the entire saga up to that point.

- **N01**: 0 previous links (establishes baselines)
- **N02**: 1 previous link (N01)
- **N15**: 14 previous links (N01-N14)
- **N30**: 29 previous links (N01-N29)

### B. Innocence Protocol Enforcement

The Perplexity Space **MUST** enforce the Dual-Canon Architecture:

1.  **N01–N29 Generation**: **STRICTLY** use files from `INNOCENT_FRAME/` and the innocent-frame sections of the structural timelines. The Writer GPT must operate with **ZERO** knowledge of the orchestration, Tiffani's Auditor identity, or the guilty canon.
2.  **N30 Generation**: **ONLY** for N30, the Writer GPT must access the `GUILTY_FRAME/` dossiers and the full, guilty-frame truth from the structural timelines to execute the final **Revelation and Collapse** beat.

### C. Generation Steps

1.  **Select Target**: Choose the next sequential novella (e.g., N01, N02, etc.).
2.  **Ingest Prompt**: Read the corresponding `N##_Bible_TITLE.md` placeholder file from `04_Writer_Deliverables/02_Bibles/`.
3.  **Gather Context**: Ingest all linked previous Bibles and the mandatory files from `01_Foundation/`, `02_Character_Dossiers/INNOCENT_FRAME/`, and `03_Structural_Timelines/`.
4.  **Generate Bible**: Produce the 13-section Story Bible based on the prompt and ingested context.
5.  **Overwrite File**: Replace the placeholder file with the completed Story Bible.
6.  **Commit and Push**: Commit the change with a clear message (e.g., "FEAT: Completed N01 Bible: Grip That Holds") and push to the repository.
7.  **Prose Generation**: Use the corresponding `N##_Prose_Engine_Prompt.md` file and the newly generated Bible to configure the prose-writing GPT.

---

## 4. KEY CONCEPTS (TECHNICAL DEFINITIONS)

| Concept | Technical Definition | Continuity Constraint |
| :--- | :--- | :--- |
| **Soulpulse** | The latent vein-system activated by The Piercing, enabling the four principles of magic. | **Cost is Cumulative**: Vein-burn and Hollowing must accumulate as tracked in `03_Structural_Timelines/09_Story_Spine_Mapping_Innocent.md`. |
| **Confluence** | Jhace's unique ability to wield all four Soulpulse principles simultaneously (Wholeness, Form, Purity, Entropy). | **Progression is Linear**: Must follow the capacity progression defined in `03_Structural_Timelines/01_Progression_Timeline_Master.md`. |
| **Fathombreak (N05)** | The apocalyptic event where Jhace unlocks Confluence and the four God-Vessels awaken. | **Immutable Event**: Marks the transition from the GLASS turning to the CRACK turning. |
| **God-Vessels** | Four mortals (Xilcore, Leesa, Blemo, Seeri) transformed into divine embodiments of the four Soulpulse principles. | **Faction Doctrine is Fixed**: Their motivations and actions must align with their respective principles (Form, Wholeness, Purity, Entropy). |
| **Civic-Ledger Spine** | The core, non-negotiable facts of the narrative (deaths, major events) tracked in `09_Story_Spine_Mapping_Innocent.md`. | **NO RETCONS**: Any event marked in the spine is an absolute truth within the innocent frame. |

---

**END PERPLEXITY SPACE KNOWLEDGE BASE**
