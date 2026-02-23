# Export Formats

## 1) PDF Deck Registration
### Requirements
- Template-driven so “contracted formats” can be supported:
  - 60+15
  - No-sideboard (Commander/CEDH)
  - Custom variants

### Fields (common)
- Player name
- Event name
- Date
- Format
- Optional: DCI/Wizards ID, phone/email, archetype notes

### Output rules
- Sort cards alphabetically by name (default; template may override)
- Show quantities and card names
- Include main/side/none sections depending on template

### Implementation
- Recommended: HTML template + CSS → PDF rendering engine.
- Store templates in `/templates/pdf/{template_id}/...`.

## 2) CSV (Canonical internal)
Columns:
- `qty`
- `oracle_name`
- `oracle_id` (optional)
- `printing_id` (optional)
- `set_code` (optional)
- `collector_number` (optional)
- `board` (main/side/none)
- `oracle_confidence`
- `printing_confidence`
- `notes`

## 3) CSV (Moxfield Collection Import)
Goal: bulk add to collection.

Strategy:
- Prefer printing_id or set+collector when known.
- Otherwise export name-only rows.

Adapter should output the columns Moxfield expects for **collection** import (not decklist),
and include a settings option to include extras like foil/condition if blank.

(Exact required headers should be verified during implementation; keep adapter isolated so it can evolve.)
