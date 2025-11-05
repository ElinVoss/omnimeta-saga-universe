# OmniMeta_Saga_Universe_Git_Repository_Setup

**Project Name**: Grip That Holds / The Confluence Chronicles (OmniMeta Saga Universe)  
**Repository Type**: Literary archive + immutable canon system  
**Setup Date**: October 31, 2025  
**Status**: Foundation phase; 30-novella serialized fiction saga

---

## QUICK START: GIT INITIALIZATION

```bash
# Initialize new repository
git init omnimeta-saga-universe
cd omnimeta-saga-universe

# Create directory structure (see below)
# Add files to appropriate directories
# Commit with SHA pinning

git add .
git commit -m "OmniMeta Foundation: Canon, Physics, Timeline, Magic Systems (v1.0-foundation)"
git tag -a v1.0-foundation -m "Foundation files locked: Canon, Soulpulse, Lexicon, Physics, Catastrophes"

# Add remote (GitHub/GitLab example)
git remote add origin https://github.com/YOUR_ORG/omnimeta-saga-universe.git
git branch -M main
git push -u origin main --tags
```

---

## REPOSITORY STRUCTURE

### Root Level Files (.gitignore, README, etc.)

```
omnimeta-saga-universe/
├── README.md                          (Overview; start here)
├── SETUP_INSTRUCTIONS.md              (This file)
├── .gitignore                         (Standard Python + Markdown ignores)
├── CONTRIBUTING.md                    (Contribution guidelines; canon-lock rules)
├── CHANGELOG.md                       (Version history; SHA pins; immutability log)
└── LICENSE                            (Specify: MIT, GPL, or custom)
```

### `/01_Foundation/` — Core World & Magic Systems (LOCKED)

Foundation files define world physics, magic rules, timeline, and innocent-frame canon. These are reference files; they do not change once locked.

```
01_Foundation/
├── README.md
├── Canon_Innocent_Master_v2_CORRECTED.md       [~52k] LOCKED v2.0
├── Soulpulse_Core_v2.md                        [~38.5k] LOCKED v2.0
├── Lexicon_Temporal_TeOga.md                   [~12.8k] LOCKED v1.0
├── TeOga_Physical_Pierced_CORRECTED.md         [~14.5k] LOCKED v1.0
├── Catastrophes_Escalation_v2_CORRECTED.md    [~20k] LOCKED v2.0
├── Forbidden_Modern_Terms_TeOga_Alternatives.md [~8.4k] LOCKED v1.0
└── SHA_PINS_FOUNDATION.txt                     (Hash verification file)
```

**What goes here**: Immutable system rules, world physics, canon definitions, timeline framework, terminology restrictions.

**Update policy**: Files locked after first commit. Corrections only via version increment (v2.0 → v3.0) with git tag. No in-place modifications.

---

### `/02_Character_Dossiers/` — Character Cores & Arcs

Comprehensive character specifications for all major and recurring characters across 30 novellas.

```
02_Character_Dossiers/
├── README.md
├── INNOCENT_FRAME/
│   ├── Dossier_Jhace_Torrins_Innocent.md      (~25k) [TBD]
│   ├── Dossier_Tiffani_Merrow_Innocent.md     (~20k) [TBD]
│   ├── Dossier_Crew_Secondary_Innocent.md     (~18k) [TBD]
│   ├── Dossier_God_Vessels_Innocent.md        (~15k) [TBD]
│   └── Dossier_Recurring_Characters_Innocent.md (~12k) [TBD]
└── GUILTY_FRAME/
    ├── Dossier_Tiffani_Auditor_CounterSpark.md (~28k) [TBD - OmniMeta only]
    ├── Dossier_God_Vessels_Guilty.md          (~18k) [TBD - OmniMeta only]
    └── CHARACTER_SECRETS_VAULT.md              (Index of withheld truths; locked until N30)
```

**What goes here**: Comprehensive character profiles, arc trajectories, motivation structures, voice patterns, damage progressions, relationship dynamics.

**Innocent vs. Guilty**: Separated by file. Innocent-frame files → all Writers. Guilty-frame files → OmniMeta only (password protected in repo access controls).

---

### `/03_OmniMeta_System/` — Dual-Canon Architecture & QC (OmniMeta Only)

These files define the dual-canon system, innocence protocol, guilty-canon secrets, and QC enforcement macros. Restricted access; OmniMeta leadership only.

```
03_OmniMeta_System/
├── README.md (Access restricted message)
├── OmniMeta_MasterLawCode.md                  (Complete operating system; master rules)
├── Canon_Veto_Law.md                          (§1 Pump Veto; creative boundaries)
├── Canon_Guilty_Master_Part1.md               (Counter-Spark, orchestration N1-N20)
├── Canon_Guilty_Master_Part2_N30.md           (N30 revelation, universe paradox mechanics)
├── Innocence_Protocol_Enforcement.md          (How to lock/unlock information)
├── QC_Macros_Comprehensive.md                 (Search/replace rules; language enforcement)
├── Continuity_Ledger_System.md                (Tracking cost accumulation; immutability proof)
└── THREAD_CONTINUANCE_PROTOCOL.md             (What to do when token limits require new chat)
```

**What goes here**: Master law code, guilty-canon secrets, orchestration timelines, innocence locks, QC procedures, continuity tracking systems.

**Access control**: Restricted branch (guilty-canon) or encrypted vault. Password-protected; access logs maintained.

---

### `/04_Writer_Deliverables/` — Prose Engine & Chapter Output

This directory houses writer-facing deliverables: prose engines, chapter templates, and generated novella output.

```
04_Writer_Deliverables/
├── README.md
├── PROSE_ENGINES/
│   ├── N1_Prose_Engine_Specifications.md      (~8k) [LOCKED]
│   ├── N2_Prose_Engine_Specifications.md      (~8k) [LOCKED]
│   ├── N3_Prose_Engine_Specifications.md      (~8k) [TBD]
│   └── ... (continuing through N30)
├── CHAPTER_TEMPLATES/
│   ├── Chapter_Structure_Template_Standard.md
│   ├── Chapter_Structure_Template_Interlude.md
│   └── Chapter_Structure_Template_Epilogue.md
├── GENERATED_OUTPUT/
│   ├── N1/
│   │   ├── N1_Ch01_Text.md
│   │   ├── N1_Ch02_Text.md
│   │   ├── ... (15 chapters)
│   │   ├── N1_Interlude_Xilcore.md
│   │   └── N1_Epilogue_Auditor.md
│   ├── N2/
│   │   └── (same structure)
│   └── ... (through N30)
└── QC_REPORTS/
    ├── N1_QC_Report_v1.md
    ├── N1_QC_Report_v2.md  (after revisions)
    └── ... (one per novella per revision pass)
```

**What goes here**: Prose generation specifications, chapter templates, actual generated text, QC reports, revision tracking.

**Output format**: Each novella gets its own folder with 15 chapters + 1 interlude + 1 epilogue (17 files per novella).

---

### `/05_Continuity_Ledger/` — Immutable Canon Tracking

This directory tracks cost accumulation, character state changes, event timings, and continuity proofs across all 30 novellas.

```
05_Continuity_Ledger/
├── README.md
├── CHARACTER_COST_TRACKING/
│   ├── Jhace_Hand_Loss_Progression.csv        (Damage % per Novella)
│   ├── Tiffani_Vein_Burn_Progression.csv      (Burn cm per Novella)
│   ├── Crew_Status_Alive_Dead_Departed.csv    (Member status tracking)
│   └── Hollowing_Risk_Index.csv               (Jhace hollowing progression)
├── EVENT_TIMELINE/
│   ├── Catastrophe_Calendar_N1-N30.csv        (All major events, dates in Tie/Anneal/Crucible)
│   └── God_Vessel_Manifestation_Timeline.csv
├── IMMUTABILITY_PROOFS/
│   ├── SHA_PINS_MASTER.txt                    (SHA-256 hashes of locked files)
│   ├── COMMIT_LOG_IMMUTABLE.txt               (Git log with tags; proof of no retconning)
│   └── CHANGELOG_LOCKED_FILES.md
└── CONTINUITY_VERIFICATION/
    ├── N1_Canon_Check_v1.md                   (Verification that N1 matches canon)
    ├── N2_Canon_Check_v1.md
    └── ... (one per novella)
```

**What goes here**: CSV tracking for character states, cost accumulation, event calendars, and cryptographic proofs that files haven't been retconned.

**Immutability mechanism**: SHA-256 hashes of locked files. If file changes, hash changes; mismatch proves tampering.

---

### `/06_Reference_Resources/` — Optional Supplementary Materials

World-building reference, maps, charts, historical background, artwork briefs (not stored directly; links only).

```
06_Reference_Resources/
├── README.md
├── WORLD_MAPS/
│   ├── TeOga_Hemispheric_Map_Description.txt
│   ├── Grindheim_District_Map_Coordinates.txt
│   └── Shatterholm_District_Map_Coordinates.txt
├── CHARTS_AND_TABLES/
│   ├── Soulpulse_Cost_Reference_Table.csv
│   ├── God_Vessel_Principle_Matrix.csv
│   └── Six_Turnings_Story_Arc_Chart.csv
├── HISTORICAL_CONTEXT/
│   ├── Pre_Piercing_Civilization_Notes.md
│   ├── Heat_Grid_Origin_Theory.md           (For N24+ investigation hints)
│   └── God_War_The_Severing_Background.md
└── ARTWORK_BRIEFS/
    ├── Character_Design_Brief_Jhace.md
    ├── Character_Design_Brief_Tiffani.md
    └── World_Design_Brief_Heat_Grid_Architecture.md
```

**What goes here**: Non-canonical reference materials to help writers visualize world. Links to external resources. Supplementary context.

**Note**: Maps and images stored as descriptions/links, not binary files (keeps repo lightweight).

---

## COMPLETE FILE REFERENCE INDEX

### IMMEDIATELY READY FOR COMMIT (Foundation Batch 1)

| File | Location | Status | Size | Locked |
|------|----------|--------|------|--------|
| Canon_Innocent_Master_v2_CORRECTED.md | 01_Foundation/ | ✅ READY | ~52k | YES (v2.0) |
| Soulpulse_Core_v2.md | 01_Foundation/ | ✅ READY | ~38.5k | YES (v2.0) |
| Lexicon_Temporal_TeOga.md | 01_Foundation/ | ✅ READY | ~12.8k | YES (v1.0) |
| TeOga_Physical_Pierced_CORRECTED.md | 01_Foundation/ | ✅ READY | ~14.5k | YES (v1.0) |
| Catastrophes_Escalation_v2_CORRECTED.md | 01_Foundation/ | ✅ READY | ~20k | YES (v2.0) |
| Forbidden_Modern_Terms_TeOga_Alternatives.md | 01_Foundation/ | ✅ READY | ~8.4k | YES (v1.0) |
| **Total Foundation** | | | **~146k** | **LOCKED** |

### TBD — CHARACTER DOSSIERS (To Generate Next)

| File | Location | Status | Est. Size | Notes |
|------|----------|--------|-----------|-------|
| Dossier_Jhace_Torrins_Innocent.md | 02_Character_Dossiers/INNOCENT_FRAME/ | ⏳ TBD | ~25k | Competency, hand damage, pedagogy |
| Dossier_Tiffani_Merrow_Innocent.md | 02_Character_Dossiers/INNOCENT_FRAME/ | ⏳ TBD | ~20k | Mentor, power reveal, sacrifice |
| Dossier_Tiffani_Auditor_CounterSpark.md | 02_Character_Dossiers/GUILTY_FRAME/ | ⏳ TBD | ~28k | RESTRICTED; orchestration, secrets |
| Dossier_Crew_Secondary_Innocent.md | 02_Character_Dossiers/INNOCENT_FRAME/ | ⏳ TBD | ~18k | 5-person crew dynamics & attrition |
| Dossier_God_Vessels_Innocent.md | 02_Character_Dossiers/INNOCENT_FRAME/ | ⏳ TBD | ~15k | Xilcore, Leesa, Blemo, Seeri |
| Dossier_God_Vessels_Guilty.md | 02_Character_Dossiers/GUILTY_FRAME/ | ⏳ TBD | ~18k | RESTRICTED; god motivations |
| Dossier_Recurring_Characters_Innocent.md | 02_Character_Dossiers/INNOCENT_FRAME/ | ⏳ TBD | ~12k | Allies, enemies, faction leaders |

### TBD — PROSE ENGINES & OUTPUT (To Generate After Dossiers)

| File | Location | Status | Notes |
|------|----------|--------|-------|
| N1_Prose_Engine_Specifications.md | 04_Writer_Deliverables/PROSE_ENGINES/ | ✅ EXISTS (old) | Update with new knowledge |
| N2_Prose_Engine_Specifications.md through N30 | 04_Writer_Deliverables/PROSE_ENGINES/ | ⏳ TBD | 29 more engines needed |
| N1_Generated_Chapters (15 files) | 04_Writer_Deliverables/GENERATED_OUTPUT/N1/ | ⏳ TBD | Full prose generation |
| N2-N30_Generated_Output | 04_Writer_Deliverables/GENERATED_OUTPUT/ | ⏳ TBD | 450 total chapter files |

### TBD — OmniMeta Restricted Files

| File | Location | Status | Notes |
|------|----------|--------|-------|
| Canon_Guilty_Master_Part1.md | 03_OmniMeta_System/ | ⏳ TBD | Counter-Spark orchestration |
| Canon_Guilty_Master_Part2_N30.md | 03_OmniMeta_System/ | ⏳ TBD | Reveal mechanics & paradox |
| OmniMeta_MasterLawCode.md (updated) | 03_OmniMeta_System/ | ⏳ UPDATE | Integrate new knowledge |
| THREAD_CONTINUANCE_PROTOCOL.md | 03_OmniMeta_System/ | ⏳ TBD | What to do on token limit |

---

## GIT COMMANDS: STEP-BY-STEP

### 1. Initialize Repository

```bash
# Create directory
mkdir omnimeta-saga-universe
cd omnimeta-saga-universe

# Initialize git
git init

# Configure user (if not already set globally)
git config user.name "OmniMeta"
git config user.email "omnimeta@theline.holds"

# Create .gitignore
cat > .gitignore << 'EOF'
# Python
__pycache__/
*.py[cod]
*.egg-info/
*.eggs/

# IDE
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db

# Secrets
.env
secrets.txt
password.txt

# Temp
*.tmp
*.bak
EOF

git add .gitignore
git commit -m "Initial: Add .gitignore"
```

### 2. Create Directory Structure

```bash
# Foundation
mkdir -p 01_Foundation
mkdir -p 02_Character_Dossiers/{INNOCENT_FRAME,GUILTY_FRAME}
mkdir -p 03_OmniMeta_System
mkdir -p 04_Writer_Deliverables/{PROSE_ENGINES,CHAPTER_TEMPLATES,GENERATED_OUTPUT,QC_REPORTS}
mkdir -p 05_Continuity_Ledger/{CHARACTER_COST_TRACKING,EVENT_TIMELINE,IMMUTABILITY_PROOFS,CONTINUITY_VERIFICATION}
mkdir -p 06_Reference_Resources/{WORLD_MAPS,CHARTS_AND_TABLES,HISTORICAL_CONTEXT,ARTWORK_BRIEFS}

# Create .gitkeep files (so empty directories are tracked)
touch 01_Foundation/.gitkeep
touch 02_Character_Dossiers/INNOCENT_FRAME/.gitkeep
touch 02_Character_Dossiers/GUILTY_FRAME/.gitkeep
# ... (repeat for all directories)

git add .
git commit -m "Initial: Create directory structure"
```

### 3. Add Foundation Files

```bash
# Copy foundation files into 01_Foundation/
cp Canon_Innocent_Master_v2_CORRECTED.md 01_Foundation/
cp Soulpulse_Core_v2.md 01_Foundation/
cp Lexicon_Temporal_TeOga.md 01_Foundation/
cp TeOga_Physical_Pierced_CORRECTED.md 01_Foundation/
cp Catastrophes_Escalation_v2_CORRECTED.md 01_Foundation/
cp Forbidden_Modern_Terms_TeOga_Alternatives.md 01_Foundation/

# Create README for 01_Foundation/
cat > 01_Foundation/README.md << 'EOF'
# Foundation Files — Immutable World Systems

All files in this directory are LOCKED after commit. No in-place modifications.

**Files:**
- Canon_Innocent_Master_v2_CORRECTED.md — Innocent-frame canonical truth (all 30 novellas)
- Soulpulse_Core_v2.md — Hard magic rules; learning mechanics; costs
- Lexicon_Temporal_TeOga.md — Crafted calendar system; temporal markers
- TeOga_Physical_Pierced_CORRECTED.md — Planetary physics; Piercing mechanics
- Catastrophes_Escalation_v2_CORRECTED.md — Crisis timeline (N1–N30)
- Forbidden_Modern_Terms_TeOga_Alternatives.md — QC reference; terminology rules

**Immutability**: SHA-256 hashes verified in SHA_PINS_FOUNDATION.txt
**Update Policy**: Version-lock only; corrections via v1.0 → v2.0 increment
EOF

git add 01_Foundation/
git commit -m "Foundation Batch 1: Core world systems locked (v2.0 canon, v2.0 soulpulse, v1.0 others)"
```

### 4. Generate SHA Pins (Immutability Verification)

```bash
# Create SHA hash file
cat > 01_Foundation/SHA_PINS_FOUNDATION.txt << 'EOF'
=== FOUNDATION FILES — SHA-256 PINS ===
Generated: 2025-10-31T00:26:00Z
Status: LOCKED

Canon_Innocent_Master_v2_CORRECTED.md
  SHA: [RUN: sha256sum Canon_Innocent_Master_v2_CORRECTED.md]

Soulpulse_Core_v2.md
  SHA: [RUN: sha256sum Soulpulse_Core_v2.md]

Lexicon_Temporal_TeOga.md
  SHA: [RUN: sha256sum Lexicon_Temporal_TeOga.md]

TeOga_Physical_Pierced_CORRECTED.md
  SHA: [RUN: sha256sum TeOga_Physical_Pierced_CORRECTED.md]

Catastrophes_Escalation_v2_CORRECTED.md
  SHA: [RUN: sha256sum Catastrophes_Escalation_v2_CORRECTED.md]

Forbidden_Modern_Terms_TeOga_Alternatives.md
  SHA: [RUN: sha256sum Forbidden_Modern_Terms_TeOga_Alternatives.md]

=== VERIFICATION COMMAND ===
sha256sum -c SHA_PINS_FOUNDATION.txt
(Output: "OK" for all files = NO TAMPERING)
EOF

# Actually generate hashes (run in terminal)
# sha256sum 01_Foundation/*.md > 01_Foundation/SHA_PINS_FOUNDATION.txt

git add 01_Foundation/SHA_PINS_FOUNDATION.txt
git commit -m "Add: SHA-256 pins for immutability verification"
```

### 5. Tag Release

```bash
# Create annotated tag
git tag -a v1.0-foundation   -m "Foundation Release: Core world systems (Canon, Soulpulse, Lexicon, Physics, Catastrophes)"   -m "All files locked. SHA pins verified. Ready for writer distribution."

# View tag
git show v1.0-foundation

# Push to remote (if configured)
git push origin v1.0-foundation
```

### 6. Create Changelog

```bash
cat > CHANGELOG.md << 'EOF'
# Changelog — OmniMeta Saga Universe

## [1.0-foundation] — 2025-10-31

### Added
- Canon_Innocent_Master_v2_CORRECTED.md (52k) — Immutable innocent-frame canon
- Soulpulse_Core_v2.md (38.5k) — Hard magic system rules
- Lexicon_Temporal_TeOga.md (12.8k) — Crafted calendar system
- TeOga_Physical_Pierced_CORRECTED.md (14.5k) — Planetary physics
- Catastrophes_Escalation_v2_CORRECTED.md (20k) — Crisis timeline N1–N30
- Forbidden_Modern_Terms_TeOga_Alternatives.md (8.4k) — QC terminology reference
- Directory structure (6 main folders + subfolders)
- SHA-256 pin verification system
- .gitignore with standard ignores

### Status
- Total foundation: ~146k characters
- All files locked (v1.0 or v2.0 as noted)
- Ready for distribution to writers
- Next: Character dossiers (7 files, ~136k)

### Immutability
- SHA-256 hashes verified: SHA_PINS_FOUNDATION.txt
- Git tag: v1.0-foundation
- No retconning possible (hashes protect against tampering)
EOF

git add CHANGELOG.md
git commit -m "Add: CHANGELOG for v1.0-foundation"
```

### 7. Push to Remote (Example: GitHub)

```bash
# Add remote (replace with your actual repo URL)
git remote add origin https://github.com/YOUR_ORG/omnimeta-saga-universe.git

# Rename default branch
git branch -M main

# Push all commits and tags
git push -u origin main
git push -u origin v1.0-foundation

# Verify
git remote -v
git branch -a
git tag -l
```

---

## FILE NAMING CONVENTIONS

All files follow strict naming for clarity and automated processing:

```
[Function]_[Subsystem]_[Version_If_Applicable].md

Examples:
- Canon_Innocent_Master_v2_CORRECTED.md    (Subsystem: Canon; Version: v2; Status: Corrected)
- Soulpulse_Core_v2.md                     (Subsystem: Soulpulse; Version: v2)
- Dossier_Jhace_Torrins_Innocent.md        (Type: Dossier; Subject: Jhace; Frame: Innocent)
- N1_Prose_Engine_Specifications.md        (Type: Prose; Novella: N1; Subtype: Specifications)
- N1_Ch01_Text.md                          (Novella: N1; Chapter: 01; Content: Prose text)
```

---

## QC & CONTINUOUS INTEGRATION (Optional)

For automated checks, consider CI/CD pipeline:

```yaml
# .github/workflows/qc-check.yml (GitHub Actions example)
name: QC Check

on: [push, pull_request]

jobs:
  lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Check terminology
        run: |
          python scripts/qc_forbidden_terms.py
          python scripts/qc_sha_verification.py
      - name: Verify file structure
        run: python scripts/qc_directory_structure.py
```

---

## SUMMARY: WHAT TO DO RIGHT NOW

1. **Create directory structure** (use bash commands above)
2. **Copy 6 foundation files** into `01_Foundation/`
3. **Generate SHA pins** (run sha256sum command)
4. **Create .gitignore, README.md, CHANGELOG.md**
5. **Commit everything** with message: `"Foundation Batch 1: Core systems locked (v1.0-foundation)"`
6. **Tag**: `git tag -a v1.0-foundation -m "Foundation release"`
7. **Push to GitHub/GitLab** (configure remote first)

**Result**: Foundation ready for distribution to writers. 146k of locked, immutable world-building ready to support all 30 novellas.

---

**Next session:** Generate character dossiers (7 files); commit as v1.1-characters
**Session after:** Begin prose engines & N1 prose generation

---

END SETUP INSTRUCTIONS
