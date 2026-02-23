# MTG Card Photo → Deck PDF + Collection CSV (Design Docs)

These docs define an MVP web app that takes a **single image** of Magic: The Gathering cards and outputs:
- a **Deck Registration PDF** (supports 60+15, Commander/CEDH/no-sideboard, and other “contracted formats” via templates)
- a **Collection/Inventory CSV** compatible with Moxfield bulk collection import (and a canonical internal CSV)

**MVP constraints**
- Single image input (upload or device camera capture)
- English-only recognition
- No accounts; single-session workflow
- Board assignment editing via **select cards → Move to Main/Side**
- Printing detection is best-effort with confidence; export strictness is configurable per export

Date: 2026-02-23

## Where to start in Codex
See:
- `docs/11_codex_prompts.md` (copy/paste prompts)
- `docs/01_prd.md` (product requirements)
- `docs/02_architecture.md` (recommended stack + components)

## Repo layout suggestion (future implementation)
```
/apps/web        # Next.js frontend
/apps/api        # FastAPI backend (or Node alternative)
/packages/shared # shared types (OpenAPI generated), utilities
/docs            # these docs
```
