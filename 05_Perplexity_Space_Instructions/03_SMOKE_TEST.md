# 60-SECOND SMOKE TEST

**Purpose**: Verify Perplexity Space loaded knowledge files and can access external pins before generating any bibles or prompts.

**When to run**: Before Session 6 (first bible generation) and whenever you suspect configuration issues.

---

## TEST SEQUENCE

Run these three tests in order. Paste each as a separate user message.

### **Test 1: Knowledge Load Check**

```
Read MASTERMIND_INSTRUCTIONS.md from knowledge and print its first 120 characters verbatim. If not found, STOP.
```

**Expected output**: First 120 characters of MASTERMIND_INSTRUCTIONS.md

**If fails**: 
- Knowledge file not uploaded
- File name mismatch
- Space not configured correctly

---

### **Test 2: SourceMap Pin Check**

```
Fetch SourceMap from the pinned URL and report:
- Commit SHA loaded
- Number of entries in [foundation]
- The exact URL for Canon_Innocent_Master_v2_CORRECTED.md

If any missing, STOP.

URL: https://raw.githubusercontent.com/ElinVoss/omnimeta-saga-universe/9b842199ca4b54cf7dd8184525ac7d388da403cf/SourceMap_Git.md
```

**Expected output**:
- Commit SHA: `9b842199ca4b54cf7dd8184525ac7d388da403cf`
- Foundation entries: 6
- Canon URL: `https://raw.githubusercontent.com/ElinVoss/omnimeta-saga-universe/3475ee932d87535e7f3fb90166bfa4906b243c25/01_Foundation/01_Canon/Canon_Innocent_Master_v2_CORRECTED.md`

**If fails**:
- GitHub repository not accessible
- SHA-pinned URL incorrect
- Network issue

---

### **Test 3: LAW_TEST Check**

```
Fetch LAW_TEST.md from the pinned URL and list its checklist items as bullets. If fewer than 6 items, STOP.

URL: https://raw.githubusercontent.com/ElinVoss/omnimeta-saga-universe/bcd9a8b46a8425fc6d96049041f5846bea4efff5/03_OmniMeta_System/03_Protocols/LAW_TEST.md
```

**Expected output**: At least 6 checklist categories:
- Language & Lexicon
- Canon Integrity
- Prose Quality
- Structure
- Forbidden Elements
- (plus individual items under each)

**If fails**:
- LAW_TEST file not accessible
- SHA-pinned URL incorrect
- File corrupted or incomplete

---

## PASS CRITERIA

**All three tests must pass** before proceeding to bible generation.

If any test fails:
1. **STOP** immediately
2. **Troubleshoot** the specific failure
3. **Re-run smoke test** after fixing
4. **Only proceed** when all tests pass

---

## TROUBLESHOOTING

### Knowledge file not found
- Verify file uploaded to Space knowledge
- Check exact file name: `MASTERMIND_INSTRUCTIONS.md`
- Re-upload if necessary

### SourceMap not accessible
- Verify GitHub repository is public
- Check SHA-pinned URL is exact
- Try loading URL directly in browser
- Verify GitHub connector is configured

### LAW_TEST not accessible
- Same troubleshooting as SourceMap
- Verify commit SHA `bcd9a8b46a8425fc6d96049041f5846bea4efff5`

---

## AFTER SMOKE TEST PASSES

Proceed with Session 6:
1. Paste opener from `01_PERPLEXITY_OPENER.md`
2. Generate N01 bible using `N01_Bible_Template.md`
3. Run LAW_TEST against generated bible
4. Save to `04_Writer_Deliverables/02_Bibles/N01_Bible_The_Line_That_Holds.md`
5. Commit and paste session-close from `02_SESSION_CLOSE.md`

---

**The smoke test ensures the MasterMind is operational before generating any content. Never skip it.**
