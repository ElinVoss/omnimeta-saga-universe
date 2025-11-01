# BIBLE GENERATION WORKFLOW

**Document Version**: 1.0  
**Created**: November 1, 2025  
**Purpose**: Complete instructions for generating Story Bibles using the placeholder-prompt system  
**Audience**: OmniMeta Space operators and future conversation continuations

---

## OVERVIEW

The OmniMeta Saga Universe uses a **self-documenting Bible placeholder-prompt system** where each of the 30 novellas has a placeholder file that serves as both a generation prompt and a continuity tracker. When you're ready to generate a Story Bible for a specific novella, you read its placeholder, which contains:

- **Direct GitHub links** to ALL previous completed Bibles (for continuity)
- **CAPS innocence protocol reminder** (no guilty canon foreshadowing)
- **Specific story beats** from the timeline (what MUST happen)
- **Character status tracking** (who's alive, who's dead, physical states)
- **Crisis escalation details** (what catastrophe occurs)
- **Continuity constraints** (immutable facts from previous novellas)
- **Git push instructions** (how to replace placeholder with completed Bible)

---

## SYSTEM ARCHITECTURE

### File Structure

```
omnimeta-saga-universe/
├── 04_Writer_Deliverables/
│   └── 02_Bibles/
│       ├── N01_Bible_PLACEHOLDER.md  ← Start here
│       ├── N02_Bible_PLACEHOLDER.md
│       ├── N03_Bible_PLACEHOLDER.md
│       ├── ...
│       └── N30_Bible_PLACEHOLDER.md
│
├── BIBLE_PLACEHOLDER_TEMPLATE.md  ← Master template (reference only)
└── docs/
    └── BIBLE_GENERATION_WORKFLOW.md  ← This file
```

### Progressive Linking System

Each placeholder contains direct GitHub raw links to ALL previous completed Bibles:

- **N01**: 0 previous links (first novella, establishes baselines)
- **N02**: 1 previous link (N01)
- **N03**: 2 previous links (N01, N02)
- **N15**: 14 previous links (N01-N14)
- **N25**: 24 previous links (N01-N24)
- **N30**: 29 previous links (N01-N29) + special guilty canon instructions

This ensures **perfect continuity** — you cannot generate N15 without having read N01-N14.

---

## GENERATION WORKFLOW

### Step 1: Select Novella to Generate

Decide which novella Bible you're ready to create. **You MUST generate Bibles in order** (N01 → N02 → N03 → ... → N30) because each depends on previous continuity.

**Example**: "I'm ready to generate N03: Poison and Grief"

### Step 2: Read the Placeholder File

Navigate to the placeholder:

```
04_Writer_Deliverables/02_Bibles/N03_Bible_PLACEHOLDER.md
```

The placeholder contains:

1. **Critical Protocol Reminder** (CAPS section about innocence)
2. **Previous Novella Bibles** (direct links to N01, N02)
3. **Foundation Files** (links to Canon, Magic, World, etc.)
4. **Character Dossiers** (links to innocent-frame character files)
5. **Structural Timelines** (links to timeline sections for N03)
6. **Novella-Specific Content Requirements** (what MUST happen in N03)
7. **Bible Structure to Generate** (13 required sections)
8. **Git Push Instructions** (how to commit completed Bible)
9. **Quality Checklist** (verification before pushing)

### Step 3: Query All Referenced Files

The placeholder tells you exactly which files to read:

**Previous Bibles (MUST READ):**
- N01_Bible_The_Line_That_Holds.md
- N02_Bible_Stress_and_Fracture.md

**Foundation Files (ALWAYS REFERENCE):**
- Canon_Innocent_Master_v2_CORRECTED.md
- Soulpulse_Core_v2.md
- TeOga_Physical_Pierced_CORRECTED.md
- Catastrophes_Escalation_v2_CORRECTED.md
- Lexicon_Temporal_TeOga.md
- Forbidden_Modern_Terms_TeOga_Alternatives.md

**Character Dossiers (INNOCENT FRAME ONLY):**
- Dossier_Jhace_Torrins_Innocent.md
- Dossier_Tiffani_Merrow_Innocent.md
- Dossier_Crew_Secondary_Innocent.md
- Dossier_God_Vessels_Innocent.md
- Dossier_Recurring_Characters_Innocent.md

**Structural Timelines (QUERY N03 SECTIONS):**
- 01_Progression_Timeline_Master.md (read N03 section)
- 02_Beat_Unpredictability_System.md
- 03_Character_Arc_Tracker.md (read Jhace N03 arc)
- 04_Crisis_Escalation_Map.md (read N03 crisis)
- 05_Soulpulse_Capacity_Progression.md (read N03 capacity)
- 06_Relationship_Evolution_Timeline.md (read N03 relationships)
- 07_God_Vessel_Faction_Timeline.md (read N03 god-vessel activities)
- 08_Interlude_Placement_Logic.md

### Step 4: Extract Continuity Constraints

From the previous Bibles (N01, N02), extract:

- **Character states at N02 end**: Who's alive? Who's dead? Physical damage levels?
- **Jhace's hand damage**: What percentage at N02 end?
- **Tiffani's vein-burn**: What measurement at N02 end?
- **Jhace's Soulpulse capacity**: What principles can he wield at N02 end?
- **Relationships**: What bonds exist at N02 end?
- **Infrastructure**: What damage persists from N01-N02?

**These are IMMUTABLE** — N03 Bible CANNOT contradict them.

### Step 5: Extract N03-Specific Requirements

From the timeline (01_Progression_Timeline_Master.md), extract:

- **Major events**: Water contamination, Bram dies, Kylar converts
- **Character arcs**: Jhace → Grief-Carrier, Kylar → Ally
- **Deaths**: Bram (Ch.12)
- **Soulpulse developments**: Wholeness limits discovered
- **Crisis escalation**: Civic corruption, mass poisoning
- **Relationship changes**: Jhace + Tiffani bonded through grief

### Step 6: Generate the Bible

Create a new file: `N03_Bible_Poison_and_Grief.md`

Include all 13 required sections:

1. **Core Premise** (2-3 paragraphs, innocent frame only)
2. **Tone & Style Constraints** (LAW_TEST compliance)
3. **Worldframe** (Te'Oga post-N02 state)
4. **Cast** (Character profiles with innocent motives only)
5. **Magic & Limits** (Soulpulse status at N03)
6. **Locations & Setpieces** (Where events occur)
7. **Objects & Motifs** (Recurring symbols, tools, physical markers)
8. **Chapter Cadence** (15 chapters with beat assignments)
9. **Interlude Specifications** (2 interludes with placement and focus)
10. **Beats ↔ Scenes Map** (How beat methods map to story moments)
11. **Forbidden Lexicon Gate** (TeOga vocabulary enforcement)
12. **LAW_TEST Checklist** (Compliance verification)
13. **Mission Statement** (What N03 accomplishes in the saga)

**Critical**: The Bible must read as if events are **organic, material, and earned** — no hints that they're orchestrated by the Auditor.

### Step 7: Verify Against Quality Checklist

Before pushing, verify:

- [ ] N01 and N02 Bibles read and continuity maintained
- [ ] No guilty canon references or foreshadowing
- [ ] No "innocent frame" or "guilty frame" terminology in Bible text
- [ ] Water contamination presented as civic corruption (not orchestrated)
- [ ] Bram's death presented as tragic failure (not planned)
- [ ] All foundation files referenced correctly
- [ ] 15 chapters + 2 interludes structure maintained
- [ ] Costs visible for all Soulpulse use
- [ ] TeOga vocabulary used exclusively (no modern terms)
- [ ] Beat methods don't repeat consecutively from N02
- [ ] Interlude placement varies from N01-N02
- [ ] Hand damage progression accurate
- [ ] Vein-burn progression accurate
- [ ] Bram DIES Ch.12 (locked for continuity)
- [ ] Kylar converts to ally (locked for continuity)

### Step 8: Push to Repository

Once verified, commit the completed Bible:

```bash
cd omnimeta-saga-universe
git add 04_Writer_Deliverables/02_Bibles/N03_Bible_Poison_and_Grief.md
git commit -m "Add N03 Story Bible: Poison and Grief"
git push origin main
```

**The placeholder file is REPLACED by the completed Bible.**

### Step 9: Verify GitHub Link

Confirm the raw GitHub link is accessible:

```
https://raw.githubusercontent.com/ElinVoss/omnimeta-saga-universe/main/04_Writer_Deliverables/02_Bibles/N03_Bible_Poison_and_Grief.md
```

This link will now be referenced by N04's placeholder.

### Step 10: Move to Next Novella

Repeat Steps 1-9 for N04, N05, N06, etc.

---

## INNOCENCE PROTOCOL

### What You MUST Understand (But NOT Reveal)

**Guilty Canon Truth:**
- Tiffani is the Auditor, an extradimensional observer
- All crises are orchestrated to shape Jhace into a weapon
- The Fathombreak (N05) is a planned detonation
- Tiffani's death (N05) is staged
- God-vessels are awakened deliberately
- The entire saga is a cosmic experiment
- The endpoint is universe collapse (N30)

**Innocent Canon Presentation:**
- The Piercing is a natural cosmic catastrophe
- Soulpulse awakens as unexpected consequence
- Tiffani is a genuine partner who dies in N05
- Jhace's growth is earned through trauma
- God-vessels awaken naturally during Fathombreak
- Crises emerge from infrastructure failure and corruption
- Relationships develop authentically

**The Bible you create MUST present the innocent canon as complete truth.**

### Forbidden Language in Bibles

**NEVER include these terms in Bible text:**
- "Innocent frame" or "guilty frame"
- "Orchestrated" (when describing crises)
- "Auditor" (when describing Tiffani)
- "Staged" (when describing Tiffani's death)
- "Engineered" or "calculated" (when describing events)
- "Foreshadowing" or "hints" about the long con

**Instead, use:**
- "Organic escalation" (for crises)
- "Tragic consequence" (for deaths)
- "Earned through struggle" (for growth)
- "Authentic partnership" (for relationships)
- "Material failure" (for infrastructure)

### Special Case: N30

**N30 is the ONLY Bible that includes guilty canon.**

N30's placeholder has special instructions:
- Read guilty-frame character dossiers
- Include Tiffani's return as the Auditor
- Reveal orchestration truth
- Present universe collapse
- Final exchange between Jhace and Tiffani

All other Bibles (N01-N29) maintain complete innocence.

---

## CONTINUITY TRACKING

### Character Deaths (Cumulative)

Track who dies in each novella:

- **N03**: Bram
- **N05**: Tiffani (staged, but treated as real until N30)
- **N08**: Marisse
- **N09**: Chloen
- **N10**: Dren (injured, not dead)
- **N11**: Inspector Harven
- **N12**: Mrs. Kettner
- **N15**: Kylar
- **N16**: Councilor Vren
- **N18**: Torim
- **N19**: Petran
- **N20**: Jessa
- **N22**: Rennik
- **N23**: Old Torven
- **N24**: Lysenne
- **N25**: Mourne
- **N26**: Orveth
- **N27**: Thessa
- **N28**: Daric

**Dead characters CANNOT reappear** (except Tiffani in N30).

### Physical Degradation Tracking

**Jhace's Hands:**
- N01: 0% → 60% right / 40% left
- N02: 60%/40% → 70%/50%
- N03: 70%/50% → 80%/60%
- N04: 80%/60% → 85%/65%
- N05: 85%/65% → 90%/75% (Fathombreak)
- N06-N14: Progressive worsening
- N15: 95%/85% → 98%/90%
- N16-N25: Near-total (99%/95%)

**Tiffani's Vein-Burn:**
- N01: 3cm → 3.5cm
- N02: 3.5cm → 4cm
- N03: 4cm → 4.2cm
- N04: 4.2cm → 4.4cm
- N05: 4.4cm → (dies)

**Jhace's Vein-Burn:**
- Begins appearing N03
- Progressive worsening N04-N30
- Critical by N25 (entire torso)

### Soulpulse Capacity Progression

**Jhace's Progression:**
- N01: Wholeness (primary), Form (learning), dual-principle emerging
- N02: Dual-principle competence (Wholeness + Form)
- N03: Wholeness limits discovered
- N04: Wholeness self-healing discovered
- N05: **Four-principle simultaneity unlocked** (Wholeness, Form, Purity, Entropy)
- N06-N28: Four-principle mastery improving
- N29: **Fivefold stasis achieved** (all four + Confluence)
- N30: Stasis collapses, universe ends

---

## BEAT UNPREDICTABILITY SYSTEM

### Constraint: No Consecutive Repeats

Each novella uses 15 beat methods for its 15 chapters. **The last beat of N02 CANNOT be the first beat of N03.**

**Example:**
- N02 Ch.15: "Closure with Threads"
- N03 Ch.1: CANNOT be "Closure with Threads" (must be different)

### Constraint: No Rotation Patterns

Beats cannot follow predictable rotation:
- ❌ N01 uses beats A, B, C → N02 uses beats D, E, F → N03 uses beats A, B, C (FORBIDDEN)
- ✅ N01 uses beats A, B, C → N02 uses beats D, A, F → N03 uses beats B, E, G (ALLOWED)

### Constraint: No Sequence Repeats

A sequence of 3+ beats cannot repeat across novellas:
- ❌ N01 Ch.5-7: "Trial → Failure → Success" AND N02 Ch.5-7: "Trial → Failure → Success" (FORBIDDEN)
- ✅ N01 Ch.5-7: "Trial → Failure → Success" AND N02 Ch.5-7: "Trial → Success → Failure" (ALLOWED)

### Available Beat Methods

Query `02_Beat_Unpredictability_System.md` for the complete repertoire (30+ methods).

---

## INTERLUDE PLACEMENT LOGIC

### Constraint: Vary Placement from Previous Novella

Interludes cannot be placed at the same chapters as the previous novella:

**Example:**
- N01: Interludes after Ch.8 and Ch.12
- N02: CANNOT place after Ch.8 and Ch.12 (must vary)
- N02: COULD place after Ch.4 and Ch.11 (different)

### Methodology: Build-Up vs. Break-Down

Interludes alternate between:
- **Build-Up**: God-vessel perspective during escalation
- **Break-Down**: God-vessel perspective during aftermath

### God-Vessel Rotation

Rotate through all four god-vessels across novellas:
- Xilcore/Corlexi (Form)
- Leesa/Salee (Wholeness)
- Blemo/Mobel (Purity)
- Seeri/Eries (Entropy)

---

## COMMON PITFALLS

### Pitfall 1: Forgetting Previous Continuity

**Problem**: Generating N10 without reading N01-N09.

**Solution**: The placeholder FORCES you to read previous Bibles by providing direct links. You cannot skip them.

### Pitfall 2: Accidentally Foreshadowing Guilty Canon

**Problem**: Writing "Tiffani's mysterious motives" or "the orchestrated crisis."

**Solution**: The CAPS reminder in every placeholder warns against this. Present events as organic.

### Pitfall 3: Resurrecting Dead Characters

**Problem**: Bram appears in N10 (but he died N03).

**Solution**: Track deaths cumulatively. The placeholder lists deaths for each novella.

### Pitfall 4: Contradicting Physical States

**Problem**: Jhace's hands are 70% damaged in N10 but 60% in N11.

**Solution**: Physical degradation ONLY worsens, never improves. Track progression.

### Pitfall 5: Using Modern Terms

**Problem**: Writing "technology" or "infrastructure" instead of "craft" or "cityworks."

**Solution**: Reference `Forbidden_Modern_Terms_TeOga_Alternatives.md` for replacements.

---

## WORKFLOW FOR MULTIPLE NOVELLAS

### Sequential Generation (Recommended)

Generate Bibles in strict order:

1. Generate N01 (0 previous dependencies)
2. Push N01 to GitHub
3. Generate N02 (reads N01)
4. Push N02 to GitHub
5. Generate N03 (reads N01, N02)
6. Push N03 to GitHub
7. Continue through N30

**Advantage**: Perfect continuity, no gaps.

### Batch Generation (Advanced)

Generate multiple Bibles in one session:

1. Generate N01
2. Generate N02 (reads N01 from local file, not GitHub)
3. Generate N03 (reads N01, N02 from local files)
4. Push N01, N02, N03 to GitHub simultaneously

**Advantage**: Faster for experienced operators.

**Risk**: If you make a mistake in N01, it propagates to N02 and N03.

---

## TOKEN BUDGET MANAGEMENT

### Typical Token Usage per Bible

- **Reading placeholder**: ~3k tokens
- **Reading previous Bibles (2-3)**: ~15-20k tokens
- **Reading foundation files**: ~10k tokens
- **Reading timeline sections**: ~5k tokens
- **Generating Bible**: ~10-15k tokens
- **Total per novella**: ~45-55k tokens

### Session Planning

With a 200k token budget:
- **Conservative**: Generate 2-3 Bibles per session
- **Aggressive**: Generate 4-5 Bibles per session

**Recommendation**: Generate 3 Bibles per session, leaving buffer for revisions.

---

## EXAMPLE: GENERATING N03

### Full Workflow Demonstration

**Step 1**: Read `N03_Bible_PLACEHOLDER.md`

**Step 2**: Query previous Bibles:
- Read N01_Bible_The_Line_That_Holds.md (extract character states at end)
- Read N02_Bible_Stress_and_Fracture.md (extract character states at end)

**Step 3**: Extract continuity:
- Jhace's hands: 70% right / 50% left (from N02 end)
- Tiffani's vein-burn: 4cm (from N02 end)
- Jhace's capacity: Dual-principle (Wholeness + Form)
- Relationships: Jhace + Tiffani committed, Kylar still rival

**Step 4**: Query timeline for N03:
- Water contamination crisis
- Bram dies Ch.12
- Kylar converts from rival to ally
- Wholeness limits discovered

**Step 5**: Generate Bible sections:
1. Core Premise: "N03 is the first major tragedy..."
2. Tone & Style: LAW_TEST compliance
3. Worldframe: Te'Oga post-N02, infrastructure strained
4. Cast: Jhace, Tiffani, Bram (dies), Kylar (converts), Chloen
5. Magic & Limits: Wholeness limits, Hollowing threat
6. Locations: Contaminated districts, water systems
7. Objects: Contaminated water, falsified records
8. Chapter Cadence: 15 chapters (beats assigned)
9. Interludes: Ch.5 (Entropy), Ch.11 (Purity)
10. Beats ↔ Scenes: Discovery → Crisis → Failure → Grief → Acceptance
11. Forbidden Lexicon: TeOga vocabulary enforced
12. LAW_TEST Checklist: All checks passed
13. Mission Statement: "N03 establishes limits, grief conditioning..."

**Step 6**: Verify quality checklist (all boxes checked)

**Step 7**: Push to GitHub:
```bash
git add 04_Writer_Deliverables/02_Bibles/N03_Bible_Poison_and_Grief.md
git commit -m "Add N03 Story Bible: Poison and Grief"
git push origin main
```

**Step 8**: Verify link accessible

**Step 9**: Move to N04

---

## TROUBLESHOOTING

### Issue: "I can't access previous Bible links"

**Solution**: Ensure previous Bibles are pushed to GitHub. If generating in batch, read from local files instead.

### Issue: "I'm not sure what 'innocent frame' means"

**Solution**: Read the CRITICAL PROTOCOL REMINDER section in any placeholder. It explains guilty vs. innocent canon.

### Issue: "The timeline doesn't specify enough detail"

**Solution**: The timeline provides major events. You fill in the narrative details based on character arcs and crisis escalation.

### Issue: "I accidentally included guilty canon"

**Solution**: Search the Bible for forbidden terms (orchestrated, Auditor, staged, engineered). Remove and rephrase as organic events.

### Issue: "I forgot to track a death"

**Solution**: Reference the "Character Deaths (Cumulative)" section in this document. Cross-check against previous Bibles.

---

## FINAL NOTES

### This System is Self-Documenting

Every placeholder contains everything you need to generate its Bible. You don't need to remember continuity—the placeholders track it for you.

### This System Enforces Innocence

The CAPS reminder in every placeholder prevents accidental guilty canon leakage. The system is designed to protect the N30 reveal.

### This System Scales Perfectly

N01 has 0 previous links. N30 has 29 previous links. The architecture handles both equally well.

### This System is Immutable

Once a Bible is pushed to GitHub, it becomes part of the continuity chain. Future Bibles MUST honor it.

---

**END BIBLE GENERATION WORKFLOW**

**File Location**: `omnimeta-saga-universe/docs/BIBLE_GENERATION_WORKFLOW.md`  
**Usage**: Reference this document whenever generating a Story Bible  
**Maintenance**: Update if placeholder structure changes
