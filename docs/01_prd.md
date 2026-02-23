# Product Requirements Document (PRD)

## 1. Problem
Players and collectors want to convert a single photo of MTG cards into:
1) a **tournament deck registration PDF** and
2) a **bulk collection CSV** (Moxfield-compatible),
with minimal manual typing and fast correction when recognition/printing guesses are uncertain.

## 2. Target users
- Tournament player registering a deck quickly (Legacy/Modern/Standard/etc., plus Commander/CEDH)
- Collector doing occasional bulk entry from photos
- TO/Judge who wants a consistent decklist PDF format

## 3. MVP Scope (what must ship)
### 3.1 Input
- **Single image** captured from device camera or uploaded from disk.
- Expected: 10–120 cards visible.
- English-only text recognition.

### 3.2 Output
- Deck registration **PDF**
  - Supports configurable templates (60+15, no-sideboard, other contracted formats)
  - Includes configurable header fields (player name, event, date, format, etc.)
- **Collection CSV** for Moxfield bulk import
  - Best-effort printing resolution (set/collector number) with confidence + user override
  - Must still export even if printings are unknown, unless user chooses strict mode for that export

### 3.3 Core UX
- Upload/capture → processing → review
- Review screen shows recognized cards grouped with quantities
- Board assignment can be edited:
  - Select one or more card groups → Move to Mainboard / Sideboard / (None, for no-sideboard formats)
- Printing identification review:
  - For low-confidence printings, allow user to pick from candidate printings
  - “I don’t care” option: export name-only for those rows

### 3.4 Session model
- No accounts.
- A “session” lives in memory and/or temporary storage; user can download outputs before leaving.
- Optional: “download session bundle” (JSON) for debugging (nice-to-have).

## 4. Out of Scope (MVP)
- Multi-image scans
- Non-English cards
- Pricing/valuation
- Condition/grade
- Fully offline support
- Guaranteed foil/etched/serialized detection

## 5. Acceptance Criteria (MVP)
1. User can upload/capture a single image and see processing status.
2. App detects individual cards and produces a recognized list with quantities.
3. User can correct card identity (name) when wrong.
4. User can assign cards to main/side/none via selection and a move action.
5. App generates:
   - PDF deck registration from a selectable template
   - Moxfield-compatible collection CSV
6. For any card with printing confidence below threshold, UI flags it and offers printing selection; export is still possible using name-only (unless strict export mode selected).

## 6. Future Milestones (high level)
- Multi-image inventory scanning and merging
- Accounts + scan history
- Advanced UI (thumbnail-based drag interactions, altered-card assistance)
- More robust printing classification (symbol classifier + art embedding)
