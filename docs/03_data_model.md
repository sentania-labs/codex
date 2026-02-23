# Data Model (Conceptual)

## Entities
### Session
- `session_id` (uuid)
- `created_at`
- `status`: `uploaded | processing | needs_review | ready | exporting | complete | failed`
- `settings` (optional): export confidence threshold defaults, template choices

### ImageAsset
- `image_id` (uuid)
- `session_id`
- `original_uri`
- `processed_uri` (normalized)
- width/height

### DetectedCardInstance
Represents a single card found in the photo.
- `card_instance_id`
- `image_id`
- `bbox`: x,y,w,h (in original image space)
- `warp_matrix` or `corners` (for perspective transform)
- `crop_uri`
- `recognition`: status + best match + candidates

### CardRecognition
- `oracle_id` (Scryfall oracle ID or internal canonical ID)
- `name`
- `confidence`
- `candidates`: [{oracle_id, name, confidence}]

### PrintingRecognition (best-effort)
- `printing_id` (Scryfall printing ID) OR {set_code, collector_number}
- `confidence`
- `candidates`: [{printing_id, set_code, collector_number, confidence}]

### GroupedCard (what user edits)
Group card instances by recognized oracle (and optionally printing when confident).
- `group_id`
- `oracle_id`, `name`
- `qty`
- `assigned_board`: `main | side | none | unknown`
- `printing`: best guess + confidence
- `needs_review`: boolean

## Notes
- You will likely store both per-instance results and grouped results.
- User edits should apply to the group, then optionally propagate down to instances.
