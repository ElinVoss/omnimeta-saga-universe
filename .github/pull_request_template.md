---
name: OmniMeta Saga Consistency Checklist
about: Checklist for ensuring continuity and consistency before merging changes.
title: "[FEAT/CHORE/DOCS]: Concise description of changes"
labels: consistency
assignees: ''

---

## OmniMeta Saga Consistency Guardrail Checklist

Please ensure all checks pass before requesting a review. This checklist is enforced by the `omnimeta-consistency` CI workflow.

- [ ] **File Count**: Exactly one Bible file exists for each N01–N30 (30 files total).
- [ ] **File Naming**:
    - [ ] N28 filename matches the corrected title: `N28_Bible_ECHOES_END.md`
    - [ ] N29 filename matches the corrected title: `N29_Bible_APEX_OF_STASIS.md`
- [ ] **Title Consistency**:
    - [ ] No instance of the old title “All Constructs Fall” exists anywhere in the repository.
    - [ ] No instance of the old title “Knotted Resolution” exists anywhere in the repository.
- [ ] **Structural References**:
    - [ ] The `03_Structural_Timelines/01_Progression_Timeline_Master.md` file references the corrected titles.
    - [ ] The `03_Structural_Timelines/09_Story_Spine_Mapping_Innocent.md` file references the corrected titles.

---

## Description of Changes

[Please provide a detailed description of the changes made in this Pull Request.]
