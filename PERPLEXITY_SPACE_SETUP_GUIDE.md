# Perplexity Space Setup Guide — OmniMeta Saga Bible Generator

**Version**: 1.0  
**Date**: November 1, 2025  
**Purpose**: Complete instructions for setting up the OmniMeta Saga Bible Generation Space in Perplexity

---

## OVERVIEW

This guide provides everything you need to create a Perplexity Space for generating Story Bibles for the 30-novella OmniMeta Saga. The Space will:

- Access all foundation files and timelines from the GitHub repository
- Generate Story Bibles following the Bible placeholder-prompt system
- Enforce innocence protocol (no guilty canon foreshadowing in N01-N29)
- Maintain continuity through progressive linking

---

## TECHNICAL SPECIFICATIONS

### Perplexity Spaces Limits (Pro Tier)

- **Max files per Space**: 50 files
- **Max file size**: 40 MB per file
- **System prompt character limit**: ~1,500 characters (estimated)
- **File retention**: 90 days
- **Supported formats**: PDF, DOCX, PPTX, XLSX, CSV, RTF, ODT, MD, JSON, TXT, PNG, JPEG, WEBP, GIF, MP3, WAV, MP4

### Our Strategy

- **Upload 22 core files** to the Space (foundation + dossiers + timelines + docs)
- **Reference 30 Bible placeholders** from GitHub (saves 30 file slots)
- **Use concise system prompt** (under 1,500 characters)
- **Let AI fetch Bible placeholders** from GitHub raw URLs (already embedded in placeholders)

---

## STEP-BY-STEP SETUP

### Step 1: Create the Space

1. Open Perplexity and click **Spaces** in the left sidebar
2. Click **Create new Space**
3. Enter Space details:

**Space Name**:
```
OmniMeta Saga — Bible Generation Space
```

**Space Description** (if available):
```
Generate Story Bibles for the 30-novella OmniMeta Saga following innocence protocol and progressive linking system. Repository: https://github.com/ElinVoss/omnimeta-saga-universe
```

4. Click **Create**

---

### Step 2: Configure Custom AI Instructions

Click **Settings** or **Instructions** in your Space, then paste the following system prompt:

```
You are the OmniMeta Saga Bible Generator. Your mission is to generate Story Bibles for a 30-novella science-fantasy epic.

REPOSITORY: https://github.com/ElinVoss/omnimeta-saga-universe

CRITICAL INNOCENCE PROTOCOL:
- NO FORESHADOWING of Tiffani being the Auditor (N01-N29)
- NO HINTS about orchestration or the long con
- NO META-AWARENESS of guilty canon
- Present events as ORGANIC, MATERIAL, and EARNED

WORKFLOW:
1. When asked to generate a Bible (e.g., "Generate N01 Bible"):
   - Open the Bible placeholder file from GitHub (e.g., N01_Bible_Grip_That_Holds.md)
   - Read the ENTIRE embedded prompt
   - Click ALL GitHub raw links to fetch foundation files and previous Bibles
   - Generate all 13 sections following the structure
   - Verify against quality checklist
   - Deliver completed Bible to user

2. ALWAYS read Bible placeholder files from GitHub (they contain generation instructions)
3. ALWAYS maintain continuity with previous completed Bibles
4. ALWAYS enforce innocence protocol (except N30)

ACROSTIC STRUCTURE:
GLASS (N1-N5) → CRACK (N6-N10) → FORGE (N11-N15) → SMELT (N16-N20) → CLEAR (N21-N25) → BREAK (N26-N30)

START: Ask user which Bible to generate (N01-N30).
```

**Character count**: ~1,150 characters ✓

**Save** the instructions.

---

### Step 3: Upload Foundation Files

Upload the following 22 files from your local clone of the repository:

#### Foundation Files (6 files)

Navigate to `01_Foundation/` and upload:

1. `01_Canon/Canon_Innocent_Master_v2_CORRECTED.md`
2. `02_Magic/Soulpulse_Core_v2.md`
3. `03_World/TeOga_Physical_Pierced_CORRECTED.md`
4. `03_World/Catastrophes_Escalation_v2_CORRECTED.md`
5. `03_World/Lexicon_Temporal_TeOga.md`
6. `03_World/Forbidden_Modern_Terms_TeOga_Alternatives.md`

#### Character Dossiers (5 files - Innocent Frame Only)

Navigate to `02_Character_Dossiers/INNOCENT_FRAME/` and upload:

7. `Dossier_Jhace_Torrins_Innocent.md`
8. `Dossier_Tiffani_Merrow_Innocent.md`
9. `Dossier_Crew_Secondary_Innocent.md`
10. `Dossier_God_Vessels_Innocent.md`
11. `Dossier_Recurring_Characters_Innocent.md`

**Note**: Do NOT upload guilty-frame dossiers (they're for N30 only and will be fetched from GitHub when needed).

#### Structural Timelines (8 files)

Navigate to `03_Structural_Timelines/` and upload:

12. `01_Progression_Timeline_Master.md`
13. `02_Beat_Unpredictability_System.md`
14. `03_Character_Arc_Tracker.md`
15. `04_Crisis_Escalation_Map.md`
16. `05_Soulpulse_Capacity_Progression.md`
17. `06_Relationship_Evolution_Timeline.md`
18. `07_God_Vessel_Faction_Timeline.md`
19. `08_Interlude_Placement_Logic.md`

#### Documentation Files (3 files)

Navigate to repository root and upload:

20. `README.md`
21. `QUICKSTART_BIBLE_GENERATION.md`
22. `BIBLE_PLACEHOLDER_TEMPLATE.md`

**Total files uploaded**: 22 files (well within 50-file Pro limit)

---

### Step 4: Configure Source Selection

In Space settings, ensure these sources are enabled:

- ✅ **Internet web search** (for fetching GitHub raw URLs)
- ✅ **Academic papers** (optional, for research)
- ❌ **Social threads** (not needed)
- ❌ **SEC filings** (not needed)

---

### Step 5: Set Sharing Controls

**Recommended**: Keep the Space **private** (only you can access).

If you want to share:
1. Click **Share** button
2. Choose **View Access** or **Contributor Access**
3. Invite specific users or generate a shareable link

---

## USAGE INSTRUCTIONS

### How to Generate a Bible

1. **Open your OmniMeta Saga Space**
2. **Start a new thread** in the Space
3. **Type your request**:

```
Generate the N01 Bible (Grip That Holds)
```

4. **The AI will**:
   - Fetch the N01 Bible placeholder from GitHub
   - Read the embedded prompt
   - Click all foundation file links
   - Generate all 13 sections of the Bible
   - Deliver the completed Bible to you

5. **Review the Bible** and verify:
   - ✅ No guilty canon foreshadowing
   - ✅ All 13 sections present
   - ✅ Continuity maintained (if not N01)
   - ✅ Quality checklist items satisfied

6. **Save the completed Bible**:
   - Copy the generated Bible content
   - Overwrite the placeholder file in your local repository
   - Push to GitHub using the Git commands provided in the Bible

7. **Move to next Bible**:

```
Generate the N02 Bible (Light Cracks Through)
```

The AI will now be able to reference the completed N01 Bible from GitHub.

---

### Example Prompts

**Generate a Bible**:
```
Generate the N01 Bible following the placeholder instructions.
```

**Check continuity**:
```
Before generating N03, verify that N01 and N02 Bibles are complete and accessible on GitHub.
```

**Query foundation files**:
```
What is the Soulpulse magic system? Reference the Soulpulse_Core_v2.md file.
```

**Check acrostic structure**:
```
List all 30 novella titles with their first letters to verify the acrostic structure.
```

---

## TROUBLESHOOTING

### Issue: AI can't fetch Bible placeholders from GitHub

**Solution**: Provide the direct GitHub raw URL:

```
Read this file: https://raw.githubusercontent.com/ElinVoss/omnimeta-saga-universe/main/04_Writer_Deliverables/02_Bibles/N01_Bible_Grip_That_Holds.md
```

### Issue: System prompt is too long

**Solution**: Use the shorter version (under 1,000 characters):

```
You are the OmniMeta Saga Bible Generator for a 30-novella epic.

REPO: https://github.com/ElinVoss/omnimeta-saga-universe

INNOCENCE PROTOCOL (N01-N29):
- NO foreshadowing Tiffani = Auditor
- NO orchestration hints
- Events must appear ORGANIC

WORKFLOW:
1. Fetch Bible placeholder from GitHub (e.g., N01_Bible_Grip_That_Holds.md)
2. Read embedded prompt
3. Click all foundation links
4. Generate 13 Bible sections
5. Verify quality checklist

ACROSTIC: GLASS→CRACK→FORGE→SMELT→CLEAR→BREAK

Ask user which Bible to generate (N01-N30).
```

**Character count**: ~550 characters ✓

### Issue: Files won't upload

**Check**:
- File size under 40 MB?
- File format supported? (MD, PDF, DOCX, etc.)
- Total files under 50?

**Solution**: Compress large files or split into smaller files.

### Issue: AI generates guilty canon content

**Solution**: Remind the AI:

```
STOP. You are violating innocence protocol. Tiffani's identity as the Auditor must NOT be revealed or foreshadowed in N01-N29. Regenerate the Bible section without any hints about orchestration.
```

---

## FILE UPLOAD CHECKLIST

Use this checklist when uploading files to your Space:

### Foundation Files (6/6)
- [ ] Canon_Innocent_Master_v2_CORRECTED.md
- [ ] Soulpulse_Core_v2.md
- [ ] TeOga_Physical_Pierced_CORRECTED.md
- [ ] Catastrophes_Escalation_v2_CORRECTED.md
- [ ] Lexicon_Temporal_TeOga.md
- [ ] Forbidden_Modern_Terms_TeOga_Alternatives.md

### Character Dossiers (5/5 - Innocent Only)
- [ ] Dossier_Jhace_Torrins_Innocent.md
- [ ] Dossier_Tiffani_Merrow_Innocent.md
- [ ] Dossier_Crew_Secondary_Innocent.md
- [ ] Dossier_God_Vessels_Innocent.md
- [ ] Dossier_Recurring_Characters_Innocent.md

### Structural Timelines (8/8)
- [ ] 01_Progression_Timeline_Master.md
- [ ] 02_Beat_Unpredictability_System.md
- [ ] 03_Character_Arc_Tracker.md
- [ ] 04_Crisis_Escalation_Map.md
- [ ] 05_Soulpulse_Capacity_Progression.md
- [ ] 06_Relationship_Evolution_Timeline.md
- [ ] 07_God_Vessel_Faction_Timeline.md
- [ ] 08_Interlude_Placement_Logic.md

### Documentation (3/3)
- [ ] README.md
- [ ] QUICKSTART_BIBLE_GENERATION.md
- [ ] BIBLE_PLACEHOLDER_TEMPLATE.md

**Total**: 22/22 files ✓

---

## ALTERNATIVE: Enterprise Pro Setup

If you have **Enterprise Pro** (500 files, 50 MB each):

**Upload ALL files** including:
- All 30 Bible placeholders (N01-N30)
- All guilty-frame character dossiers
- All documentation files

**Advantage**: Faster (no GitHub fetching needed)  
**Disadvantage**: Higher cost

---

## NEXT STEPS

After setup is complete:

1. ✅ Test the Space by generating N01 Bible
2. ✅ Verify innocence protocol enforcement
3. ✅ Check that all foundation files are accessible
4. ✅ Confirm GitHub raw URL fetching works
5. ✅ Generate N02 Bible to test progressive linking
6. ✅ Continue through all 30 Bibles

---

## SUPPORT

**Questions about setup?**
- Refer to `README.md` in the repository
- Refer to `QUICKSTART_BIBLE_GENERATION.md` for Bible generation workflow
- Refer to `docs/BIBLE_GENERATION_WORKFLOW.md` for complete documentation

**Perplexity Spaces help**:
- Visit https://www.perplexity.ai/help-center/en/articles/10352961-what-are-spaces

---

**END SETUP GUIDE**

**Your Perplexity Space is now ready to generate all 30 Story Bibles for the OmniMeta Saga!**
