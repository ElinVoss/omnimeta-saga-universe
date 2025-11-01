# QUICKSTART: BIBLE GENERATION SYSTEM

**Last Updated**: November 1, 2025  
**Status**: System fully operational  
**Next Action**: Generate N01 Bible

---

## WHAT WAS BUILT

A **self-documenting Bible placeholder-prompt system** for all 30 novellas of The Confluence Chronicles (OmniMeta Saga Universe).

Each placeholder file acts as:
1. **Generation prompt** (tells AI what to create)
2. **Continuity tracker** (links to all previous Bibles)
3. **Quality gate** (enforces innocence protocol and consistency)
4. **Git workflow guide** (instructions for pushing completed Bible)

---

## HOW IT WORKS

### The Progressive Linking System

```
N01_Bible_PLACEHOLDER.md
  ↓ (0 previous links)
  Generate N01 Bible
  ↓
  Push to GitHub
  ↓
N02_Bible_PLACEHOLDER.md
  ↓ (1 previous link: N01)
  Generate N02 Bible
  ↓
  Push to GitHub
  ↓
N03_Bible_PLACEHOLDER.md
  ↓ (2 previous links: N01, N02)
  Generate N03 Bible
  ↓
  ... continues through N30
```

Each placeholder contains **direct GitHub raw links** to ALL previous completed Bibles, ensuring perfect continuity.

---

## IMMEDIATE NEXT STEPS

### Step 1: Generate N01 Bible

**File to read**: `04_Writer_Deliverables/02_Bibles/N01_Bible_PLACEHOLDER.md`

**What it contains**:
- CAPS innocence protocol reminder (no guilty canon foreshadowing)
- Links to foundation files (Canon, Magic, World, Timelines)
- N01-specific requirements (The Piercing, Soulpulse awakening, Jhace + Tiffani partnership)
- 13-section Bible structure to generate
- Git push instructions
- Quality checklist

**Action**: Tell OmniMeta Space:
> "Generate the complete Story Bible for N01: The Line That Holds following the instructions in N01_Bible_PLACEHOLDER.md"

### Step 2: Push N01 Bible to GitHub

Once generated and verified:

```bash
cd omnimeta-saga-universe
git add 04_Writer_Deliverables/02_Bibles/N01_Bible_The_Line_That_Holds.md
git commit -m "Add N01 Story Bible: The Line That Holds"
git push origin main
```

**The placeholder file is REPLACED by the completed Bible.**

### Step 3: Generate N02 Bible

**File to read**: `04_Writer_Deliverables/02_Bibles/N02_Bible_PLACEHOLDER.md`

**What it contains**:
- Link to N01 Bible (for continuity)
- N02-specific requirements (Stress-riser crisis, Tiffani's confession)
- Instructions to extract character states from N01 end
- Git push instructions

**Action**: Tell OmniMeta Space:
> "Generate the complete Story Bible for N02: Stress and Fracture following the instructions in N02_Bible_PLACEHOLDER.md"

### Step 4: Repeat Through N30

Continue the cycle:
1. Read placeholder
2. Generate Bible
3. Push to GitHub
4. Move to next novella

---

## KEY FEATURES

### 1. Innocence Protocol Enforcement

Every placeholder has a **CAPS reminder** at the top:

```
**THIS BIBLE MUST MAINTAIN COMPLETE INNOCENCE PROTOCOL.**

- ❌ NO FORESHADOWING of Tiffani being the Auditor
- ❌ NO HINTS about orchestration or the long con
- ❌ NO META-AWARENESS of guilty canon
```

This prevents accidental guilty canon leakage before the N30 reveal.

### 2. Automatic Continuity Tracking

Each placeholder lists:
- **Who's alive** at the start of this novella
- **Who's dead** (cumulative from all previous novellas)
- **Physical states** (Jhace's hand damage, vein-burn progression)
- **Soulpulse capacity** (what principles Jhace can wield)
- **Relationship status** (bonds, alliances, losses)

You don't need to remember—the placeholder tracks it for you.

### 3. Story Beat Requirements

Each placeholder specifies:
- **Major events** that MUST occur (from timeline)
- **Deaths** this novella (locked for continuity)
- **Character arcs** (transformations that happen)
- **Crisis escalation** (what catastrophe occurs)
- **Soulpulse developments** (capacity changes)

### 4. Quality Checklist

Before pushing, verify:
- [ ] All previous Bibles read
- [ ] No guilty canon references
- [ ] Events presented as organic (not orchestrated)
- [ ] TeOga vocabulary used exclusively
- [ ] Physical degradation tracked correctly
- [ ] All deaths honored (characters stay dead)

---

## FILE LOCATIONS

### Placeholder Files (30 total)
```
04_Writer_Deliverables/02_Bibles/
├── N01_Bible_PLACEHOLDER.md  ← START HERE
├── N02_Bible_PLACEHOLDER.md
├── N03_Bible_PLACEHOLDER.md
├── ...
└── N30_Bible_PLACEHOLDER.md
```

### Documentation
```
BIBLE_PLACEHOLDER_TEMPLATE.md  ← Master template (reference)
docs/BIBLE_GENERATION_WORKFLOW.md  ← Complete workflow guide
QUICKSTART_BIBLE_GENERATION.md  ← This file
```

### Backup
```
/home/ubuntu/N01_Bible_The_Line_That_Holds_BACKUP.md  ← Original N01 Bible (not in repo)
```

---

## EXAMPLE: GENERATING N03

### What You Say to OmniMeta Space

> "I'm ready to generate the Story Bible for N03: Poison and Grief. Please read the placeholder file at `04_Writer_Deliverables/02_Bibles/N03_Bible_PLACEHOLDER.md` and follow all instructions, including reading the previous Bibles (N01, N02) for continuity."

### What Happens

1. **OmniMeta Space reads N03 placeholder**
2. **Queries N01 and N02 Bibles** (via GitHub raw links)
3. **Extracts continuity** (character states, hand damage, vein-burn, capacity)
4. **Queries timeline** (N03 section: water contamination, Bram dies, Kylar converts)
5. **Generates 13-section Bible** (Core Premise, Cast, Magic, Chapters, Interludes, etc.)
6. **Verifies quality checklist** (no guilty canon, TeOga vocabulary, continuity honored)
7. **Provides Git push instructions**

### What You Do

1. **Review the generated Bible** (check for quality)
2. **Approve or request revisions**
3. **Push to GitHub**:
   ```bash
   git add 04_Writer_Deliverables/02_Bibles/N03_Bible_Poison_and_Grief.md
   git commit -m "Add N03 Story Bible: Poison and Grief"
   git push origin main
   ```

### What Happens Next

- **N03 placeholder is REPLACED** by completed Bible
- **N04 placeholder now has link** to N03 Bible
- **Continuity chain extends** (N01 → N02 → N03 → N04)

---

## SPECIAL CASES

### N01: First Novella

- **0 previous Bible links** (establishes all baselines)
- **No continuity constraints** (everything starts here)
- **Establishes**: Jhace's baseline state, Tiffani's baseline state, world pre-Piercing

### N05: Fathombreak

- **Tiffani dies** (staged, but treated as real until N30)
- **God-vessels awaken** (Xilcore, Leesa, Blemo, Seeri)
- **Four-principle unlocked** (Jhace becomes Confluence weapon)
- **World fundamentally changed** (section breaks free from planetary body)

### N30: Revelation and Collapse

- **ONLY Bible with guilty canon**
- **Tiffani returns** as the Auditor
- **Orchestration revealed** (the long con exposed)
- **Universe collapses** (cosmic experiment ends)

---

## TROUBLESHOOTING

### "I don't understand the innocence protocol"

**Answer**: The saga has two canons:
- **Innocent canon**: Events are organic, Tiffani genuinely dies in N05, crises emerge naturally
- **Guilty canon**: Events are orchestrated by Tiffani (the Auditor), everything is a cosmic experiment

**Bibles N01-N29 present innocent canon as complete truth.**  
**Bible N30 reveals guilty canon.**

### "How do I know what to include in a Bible?"

**Answer**: The placeholder tells you:
- Read the "NOVELLA-SPECIFIC CONTENT REQUIREMENTS" section
- Query the timeline for major events
- Extract continuity from previous Bibles
- Follow the 13-section structure

### "What if I make a mistake?"

**Answer**: 
- **Before pushing**: Just regenerate the Bible
- **After pushing**: Create a corrected version and push again (Git tracks history)
- **If it affects future Bibles**: Regenerate all dependent Bibles (e.g., if N03 is wrong, regenerate N04-N30)

### "Can I skip novellas?"

**Answer**: NO. You must generate in order (N01 → N02 → N03 → ... → N30) because each depends on previous continuity.

---

## TOKEN BUDGET GUIDANCE

### Per Bible Generation

- **Reading placeholder**: ~3k tokens
- **Reading previous Bibles**: ~15-20k tokens (scales with number of previous)
- **Reading foundation files**: ~10k tokens
- **Generating Bible**: ~10-15k tokens
- **Total**: ~40-50k tokens per Bible

### Session Planning

With a 200k token budget:
- **Conservative**: Generate 2-3 Bibles per session
- **Aggressive**: Generate 4-5 Bibles per session

**Recommendation**: Start with N01-N03 in first session (test the system).

---

## SUCCESS CRITERIA

### You'll know the system is working when:

1. **N01 Bible generated** without guilty canon foreshadowing
2. **N02 Bible references N01** correctly (character states match)
3. **N03 Bible honors N01-N02** (Bram dies, Kylar converts, hand damage progresses)
4. **GitHub links work** (raw URLs accessible)
5. **Placeholders replaced** by completed Bibles
6. **Continuity chain extends** (each Bible builds on previous)

---

## FINAL CHECKLIST

Before starting N01 generation:

- [ ] Repository cloned locally
- [ ] GitHub authentication configured
- [ ] N01 placeholder read and understood
- [ ] Foundation files accessible (Canon, Magic, World, Timelines)
- [ ] Innocence protocol understood (no guilty canon in N01-N29)
- [ ] Git workflow understood (add, commit, push)
- [ ] Token budget allocated (40-50k tokens for N01)

**Once all boxes checked, you're ready to generate N01!**

---

## COMMAND TO START

Tell OmniMeta Space:

> "Generate the complete Story Bible for N01: The Line That Holds following the instructions in `04_Writer_Deliverables/02_Bibles/N01_Bible_PLACEHOLDER.md`. This is the first novella, so there are no previous Bibles to reference. Read all foundation files, query the N01 section of the timeline, and generate all 13 required sections. Maintain complete innocence protocol—no foreshadowing of Tiffani being the Auditor."

---

**END QUICKSTART**

**File Location**: `omnimeta-saga-universe/QUICKSTART_BIBLE_GENERATION.md`  
**Next Action**: Generate N01 Bible  
**Estimated Time**: 1-2 hours for N01 (first Bible is slowest, later ones are faster)
