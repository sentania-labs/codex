# API Spec (Draft)

Base URL: `/api`

## 1. Sessions
### POST /sessions
Create a new session.
Response:
- `session_id`

### POST /sessions/{session_id}/image
Upload a single image (multipart form-data: `file`).
Response:
- `image_id`

### POST /sessions/{session_id}/process
Enqueue processing for the uploaded image.
Response:
- `job_id`

### GET /sessions/{session_id}
Get session status and results (when available).
Response includes:
- `status`
- `progress` (optional)
- `groups`: GroupedCard[]
- `unassigned_count`, `needs_review_count`

## 2. Corrections
### PATCH /sessions/{session_id}/groups/{group_id}
Body (any subset):
- `assigned_board`: `main|side|none|unknown`
- `confirmed_oracle_id`
- `confirmed_printing_id` OR `confirmed_set_code`+`collector_number`
- `user_notes` (optional)
Response:
- updated group

### POST /sessions/{session_id}/groups/{group_id}/split
Split a group into multiple groups (advanced; optional MVP).
Used if one group accidentally merged two different cards/printings.
Body:
- selection of instance IDs per new group

## 3. Exports
### POST /sessions/{session_id}/export/pdf
Body:
- `template_id`
- `fields`: { player_name, event_name, date, format, ... }
- `confidence_threshold` (optional override)
Response:
- `export_id`, `download_url`

### POST /sessions/{session_id}/export/csv
Body:
- `adapter`: `moxfield_collection | canonical`
- `confidence_threshold` (optional override)
- `strict_printing`: boolean (if true, block export when printing below threshold)
Response:
- `export_id`, `download_url`

## 4. Static reference data
### GET /reference/templates
List available PDF templates.

### GET /reference/cards/search?q=
Search oracle names (for correction UI).

### GET /reference/printings?oracle_id=
List printings for a given oracle ID (for printing picker UI).

## Notes
- Provide an OpenAPI schema and generate TS client types.
