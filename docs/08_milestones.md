# Milestones

## M1 — MVP (single image, name-first)
- Web UI: upload/camera capture
- Backend: session + image ingestion
- Card detection + crop/normalize
- Name OCR + oracle match
- Grouping duplicates
- Review UI: correct name, assign board via select+move
- Export:
  - PDF via template (60+15 + no-sideboard templates)
  - CSV: canonical + Moxfield collection adapter (name-only fallback)

## M2 — Printing best-effort
- Collector number OCR improvements
- Set symbol classifier
- Printing candidates + printing picker UI
- CSV includes set/collector/printing where confident

## M3 — Robustness
- Better glare handling
- Art similarity embeddings to confirm oracle/printing
- Smarter grouping and false-positive handling
- Processing queue + worker scaling

## M4 — Multi-image & inventory mode
- Multiple images per session
- Merge duplicates across images
- “Inventory scanning mode” (large volume)

## M5 — Accounts
- Auth
- Saved history and exports
- Opt-in training data collection for model improvement
