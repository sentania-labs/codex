# Architecture & Tech Design (MVP)

## 1. Recommended approach
A web app with a backend API that runs computer-vision + OCR. Keep the UI and API boundaries stable so a future iOS/Android client can reuse the same backend.

### Why backend-first for recognition?
- Realistic card detection + OCR + printing resolution benefits from Python CV tooling.
- A later mobile app can capture photos and call the same API.

## 2. Components
### 2.1 Web Client (Next.js + TypeScript)
- Capture (camera) and upload flows
- Status/progress UI
- Review & correction UI
- Export PDF/CSV actions

### 2.2 API (FastAPI recommended for MVP)
- Session lifecycle (create, upload image, process, get results)
- Recognition pipeline (detect → OCR/name match → printing guess)
- Stores intermediate results for correction
- Export generation (PDF, CSV)

### 2.3 Storage (MVP)
- Object storage: local disk in dev; S3-compatible in prod.
- Metadata: SQLite in dev; Postgres in prod.

### 2.4 Async processing
- MVP can run inline for smaller images, but design as job-based to avoid request timeouts:
  - Job queue: RQ/Celery (Python)
  - Worker: CPU (GPU optional later)

## 3. Deployment
- Dev: docker-compose (web, api, redis, db)
- Prod: container platform of your choice; allow scaling worker separately

## 4. Security & Privacy (MVP defaults)
- No accounts; use random unguessable session IDs.
- Default retention: delete images/results after N hours (config).
- Provide explicit “Download outputs” actions; avoid long-term retention unless user opts in later.

## 5. Portability for iOS/Android
- Keep API stateless with explicit session tokens.
- Use OpenAPI-generated TS client for web; reuse in mobile later.
