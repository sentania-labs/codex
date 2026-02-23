# Codex Prompts (copy/paste)

Use these prompts with Codex to generate code incrementally. Treat each prompt as a task.

---

## Prompt 1 — Scaffold repo + dev environment
You are a senior full-stack engineer.
Create a monorepo with:
- `apps/web`: Next.js (TypeScript) web app
- `apps/api`: FastAPI (Python) API
- `docker-compose.yml` for local dev: web, api, redis (optional), db (sqlite ok for MVP)
- Shared OpenAPI client generation in `packages/shared` (typescript types)
Include basic linting/formatting and a `make dev` target.
The app should implement the session model described in `/docs` with no authentication.

Acceptance:
- `docker compose up` starts web and api
- web can call api health endpoint

---

## Prompt 2 — Session + image upload API
Implement API endpoints:
- POST `/api/sessions` → returns `session_id`
- POST `/api/sessions/{session_id}/image` → upload single image (multipart)
- GET `/api/sessions/{session_id}` → status
Store images locally under `./data/{session_id}/original.jpg`.
Return JSON with `image_id`, dimensions, and status transitions.

Acceptance:
- Upload works via web UI
- GET session shows uploaded image metadata

---

## Prompt 3 — Stub recognition pipeline (no ML yet)
Implement a placeholder processor:
- When `/process` is called, it produces a deterministic fake result with 5–10 grouped cards
  matching the `GroupedCard` schema from docs.
- Add PATCH group corrections and persist session state to disk as JSON.

Acceptance:
- Review screen renders groups and supports select+move main/side/none
- Corrections persist across refresh

---

## Prompt 4 — PDF export (template-driven)
Implement `/export/pdf`:
- Use HTML templates (Jinja2) and render to PDF
- Provide two templates:
  - `60_15`
  - `no_sideboard`
Sort cards alphabetically in each section.
Return `download_url`.

Acceptance:
- PDF downloads and matches selected template

---

## Prompt 5 — CSV export with adapters
Implement `/export/csv`:
- Canonical CSV
- `moxfield_collection` adapter (name-only fallback supported)
Support `confidence_threshold` and `strict_printing` behavior as in docs.

Acceptance:
- CSV downloads; strict printing blocks when required and returns actionable errors

---

## Prompt 6 — Integrate real detection + OCR (incremental)
Replace stub recognition with real pipeline stages:
- Detect cards (start with a simple baseline; iterate)
- OCR name region
- Fuzzy match to oracle index (start with a local oracle name list from Scryfall data dump)
Return candidates + confidence.

Acceptance:
- For a clear photo, recognizes most card names correctly
- Low-confidence items are flagged and editable

---

## Prompt 7 — Printing resolution (incremental)
Add:
- OCR collector number
- Set symbol classifier stub (can be rule-based at first)
- Printing picker using Scryfall printings list per oracle

Acceptance:
- For modern cards, set+collector often resolves
- User can override printing for low-confidence cases

---

### Implementation notes for Codex
- Keep the `GroupedCard` JSON schema stable.
- Prefer simple, debuggable steps with good logging and saved intermediate crops.
- Add a “debug bundle download” endpoint that zips session JSON + crops for troubleshooting.
