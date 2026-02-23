# UX Flows (MVP)

## 1. Upload/Capture
- Landing shows:
  - “Use Camera” (mobile)
  - “Upload Image” (desktop/mobile)
- After selection, show preview and “Start Scan”

## 2. Processing
- Progress steps:
  1) Detecting cards
  2) Reading names
  3) Guessing printings
  4) Grouping duplicates

## 3. Review Screen (primary)
Layout:
- Top summary: counts (total cards detected, groups, needs review)
- Tabs or sections based on selected format:
  - Mainboard
  - Sideboard (if applicable)
  - None/Unassigned (for no-sideboard formats, or unknown)

Each group tile shows:
- Qty (big)
- Card name
- Printing indicator (set code / symbol if known) + confidence badge
- “Needs review” indicator if below thresholds

Actions:
- Select mode (checkbox on each tile)
- Buttons:
  - Move to Mainboard
  - Move to Sideboard
  - Move to None
- Per-tile actions:
  - Edit card (search oracle name)
  - Edit printing (picker)
  - Remove (if false positive)

## 4. Printing Picker
- Shows top candidate printings
- Filters: set, year, collector number
- Option: “Use name only”

## 5. Export
Export modal:
- Choose format/template: (60+15, no-sideboard, etc.)
- Set `confidence_threshold` slider (0–100)
- Strict printing checkbox (for CSV export only)
- PDF fields (player name, event, etc.)
- Buttons:
  - Generate PDF
  - Generate CSV

## 6. Edge Cases UI
- If detection finds too few cards: show guidance (lighting, distance, avoid glare)
- If many low-confidence: recommend retake photo
