# Recognition Pipeline (MVP + growth path)

## 0. Inputs & constraints
- One image (often phone camera)
- Cards may be skewed, overlapping slightly, glare present
- English-only for MVP

## 1. Stage A: Card Detection (object detection)
Goal: find card bounding boxes.
Output:
- bounding boxes + corner points (preferred) for perspective correction

Implementation options:
- YOLO-family detector fine-tuned on MTG card layouts
- Fallback: contour detection + aspect ratio heuristics (less reliable)

## 2. Stage B: Crop + Normalize
For each detected card:
- Perspective transform to standard card rectangle
- Normalize brightness/contrast
- Optional glare mitigation

## 3. Stage C: Name OCR + Oracle match
- Crop nameplate region
- OCR text
- Fuzzy match against oracle name index (Scryfall oracle names)
- Return top candidates with confidence scores

## 4. Stage D: Printing guess (best effort)
Attempt in descending reliability:
1) OCR collector number (bottom right)
2) Set symbol classification (small classifier on set symbol region)
3) Art similarity within oracle (future milestone)
4) Frame/border heuristics for old sets (A/B/U/Revised/4th etc.) (future milestone)

MVP target:
- For modern cards, (1)+(2) will often work.
- For old-border or symbol-less, return low confidence and let user select.

## 5. Stage E: Group duplicates
- Cluster card instances by oracle_id
- If printing confidence is high and printings differ, split into separate groups
- Produce `GroupedCard` list with quantities

## 6. Confidence thresholds
Two separate confidences:
- `oracle_confidence` (name match)
- `printing_confidence` (set/collector match)

UI uses thresholds to flag items; export can apply user-selected threshold.

## 7. “Altered card” considerations (future)
- OCR may fail; art similarity may fail.
- Provide a “manual confirm” workflow:
  - user selects oracle name
  - then selects printing
