# MTG Card Photo MVP Monorepo

This repository now contains a full-stack monorepo implementation for the session-based MTG scan workflow described in `/docs`.

## Structure

- `apps/web`: Next.js + TypeScript web UI for creating and reviewing an anonymous session.
- `apps/api`: FastAPI backend implementing the no-auth session lifecycle, group corrections, and export endpoints.
- `packages/shared`: Shared TypeScript API types generated from OpenAPI.

## Local development

```bash
make dev
```

This starts:

- `web` on `http://localhost:3000`
- `api` on `http://localhost:8000`
- `redis` on `localhost:6379`
- `db` (Postgres for future parity; API currently uses SQLite for MVP defaults) on `localhost:5432`

## Useful commands

```bash
make api-dev
make web-dev
make lint
make generate-types
```

## Session model (no authentication)

The API follows the doc spec:

1. Create session: `POST /api/sessions`
2. Upload image: `POST /api/sessions/{session_id}/image`
3. Process image: `POST /api/sessions/{session_id}/process`
4. Review and edit groups: `GET/PATCH /api/sessions/{session_id}` + group patch
5. Export PDF/CSV: `POST /api/sessions/{session_id}/export/*`

For MVP, processing is mocked with deterministic sample grouped cards and review confidence behavior.
