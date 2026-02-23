# Testing Plan

## Unit tests
- Fuzzy match scoring for OCR output → oracle match
- Grouping logic (merge/split rules)
- Export formatting
  - PDF snapshot tests (golden files)
  - CSV header/row correctness

## Integration tests
- Upload → process → results → corrections → export PDF/CSV
- Failure cases:
  - No cards detected
  - OCR empty
  - Low confidence across many cards
  - Export strict mode blocks as expected

## Manual QA checklist
- Various lighting conditions
- Old-border cards (low printing confidence expected)
- Slight overlaps and partial occlusions
- Mobile capture on iOS/Android browsers
