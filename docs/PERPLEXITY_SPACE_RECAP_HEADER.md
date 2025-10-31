# PERPLEXITY SPACE RECAP HEADER TEMPLATE

**Purpose**: Standard header to paste at the start of every Perplexity Space session  
**Version**: 1.0  
**Usage**: Copy/paste this template, fill in task-specific details  

---

## TEMPLATE

```
[RECAP v1]
• SourceMap loaded @ 9b842199ca4b54cf7dd8184525ac7d388da403cf
• Foundation ledger @ 3475ee932d87535e7f3fb90166bfa4906b243c25 (immutable)
• Canon stance: INNOCENT ONLY; Forbidden Lexicon + LAW_TEST enforced
• Task: <one line describing what this session will accomplish>
• Outputs: <list of files or deliverables expected>
• Session-close: list files + new commit SHA + "CONTINUE FROM: <next task>"
```

---

## EXAMPLE USAGE

### Session 5: Generate Innocent-Frame Dossiers

```
[RECAP v1]
• SourceMap loaded @ 9b842199ca4b54cf7dd8184525ac7d388da403cf
• Foundation ledger @ 3475ee932d87535e7f3fb90166bfa4906b243c25 (immutable)
• Canon stance: INNOCENT ONLY; Forbidden Lexicon + LAW_TEST enforced
• Task: Generate five innocent-frame character dossiers (Jhace, Tiffani, Crew, God-Vessels, Recurring)
• Outputs: 5 .md files in 02_Character_Dossiers/INNOCENT_FRAME/
• Session-close: list files + new commit SHA + "CONTINUE FROM: Generate N01–N12 prose engine prompts"
```

### Session 6: Generate Prose Engine Prompts (N01–N12)

```
[RECAP v1]
• SourceMap loaded @ 9b842199ca4b54cf7dd8184525ac7d388da403cf
• Foundation ledger @ 3475ee932d87535e7f3fb90166bfa4906b243c25 (immutable)
• Canon stance: INNOCENT ONLY; Forbidden Lexicon + LAW_TEST enforced
• Task: Generate prose engine prompts for N01–N12 (GLASS + CRACK Turnings)
• Outputs: 12 .md files in 04_Writer_Deliverables/PROSE_ENGINES/
• Session-close: list files + new commit SHA + "CONTINUE FROM: Generate N13–N24 prose engine prompts"
```

---

## WHY THIS HEADER MATTERS

### Prevents Drift
Every session starts with the same immutable references:
- **SourceMap @ 9b84219** — Where to find all files
- **Foundation @ 3475ee9** — Immutable canon baseline
- **LAW_TEST enforced** — Quality control reminder

### Ensures Continuity
The "CONTINUE FROM" line at session close tells the next session exactly what to do next, preventing task fragmentation.

### Tracks Outputs
The "Outputs" line makes it clear what files should exist after the session, enabling verification.

---

## SESSION-CLOSE FORMAT

At the end of every Perplexity Space session, provide:

```
[SESSION COMPLETE]
Files created:
- 02_Character_Dossiers/INNOCENT_FRAME/Dossier_Jhace_Torrins_Innocent.md
- 02_Character_Dossiers/INNOCENT_FRAME/Dossier_Tiffani_Merrow_Innocent.md
- [etc.]

New commit SHA: <commit hash>
Tag: v2.1-dossiers

CONTINUE FROM: Generate N01–N12 prose engine prompts
```

---

## UPDATING THE TEMPLATE

If the SourceMap or Foundation ledger gets updated (new commit), update this template:

1. Get new SourceMap commit: `git log --oneline -1 SourceMap_Git.md`
2. Get new Foundation commit: `git log --oneline -1 05_Continuity_Ledger/hashes/v2.0-foundation.sha256.txt`
3. Update template with new SHAs
4. Commit: `git commit -m "Update recap header template with new SHAs"`

---

## CURRENT PINNED COMMITS

**SourceMap**: 9b842199ca4b54cf7dd8184525ac7d388da403cf  
**Foundation Ledger**: 3475ee932d87535e7f3fb90166bfa4906b243c25  

These are immutable unless foundation files change (which requires version bump and rehash).

---

**END RECAP HEADER TEMPLATE**

Use this at the start of every Perplexity Space session to maintain continuity and prevent canon drift.
