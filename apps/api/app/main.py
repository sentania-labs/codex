from __future__ import annotations

from uuid import uuid4

from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware

from .models import (
    ExportCsvRequest,
    ExportPdfRequest,
    ExportResponse,
    GroupPatch,
    GroupedCard,
    ProcessResponse,
    SessionCreateResponse,
    SessionResponse,
    UploadImageResponse,
)
from .store import SessionStore

app = FastAPI(title="MTG Session API", version="0.1.0")
store = SessionStore()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/api/sessions", response_model=SessionCreateResponse)
def create_session() -> SessionCreateResponse:
    session = store.create_session()
    return SessionCreateResponse(session_id=session.session_id)


@app.post("/api/sessions/{session_id}/image", response_model=UploadImageResponse)
async def upload_image(session_id: str, file: UploadFile = File(...)) -> UploadImageResponse:
    _ = await file.read()
    image_id = store.attach_image(session_id)
    return UploadImageResponse(image_id=image_id)


@app.post("/api/sessions/{session_id}/process", response_model=ProcessResponse)
def process_session(session_id: str) -> ProcessResponse:
    job_id = store.process(session_id)
    return ProcessResponse(job_id=job_id)


@app.get("/api/sessions/{session_id}", response_model=SessionResponse)
def get_session(session_id: str) -> SessionResponse:
    session = store.get_session(session_id)
    return SessionResponse(
        session_id=session.session_id,
        status=session.status,
        progress=session.progress,
        groups=session.groups,
        unassigned_count=store.count_unassigned(session.groups),
        needs_review_count=store.count_needs_review(session.groups),
    )


@app.patch("/api/sessions/{session_id}/groups/{group_id}", response_model=GroupedCard)
def patch_group(session_id: str, group_id: str, payload: GroupPatch) -> GroupedCard:
    return store.patch_group(session_id, group_id, payload)


@app.post("/api/sessions/{session_id}/export/pdf", response_model=ExportResponse)
def export_pdf(session_id: str, payload: ExportPdfRequest) -> ExportResponse:
    store.get_session(session_id)
    export_id = str(uuid4())
    return ExportResponse(export_id=export_id, download_url=f"/downloads/{export_id}.pdf")


@app.post("/api/sessions/{session_id}/export/csv", response_model=ExportResponse)
def export_csv(session_id: str, payload: ExportCsvRequest) -> ExportResponse:
    store.export_csv(session_id, payload)
    export_id = str(uuid4())
    return ExportResponse(export_id=export_id, download_url=f"/downloads/{export_id}.csv")


@app.get("/api/reference/templates")
def list_templates() -> list[dict[str, str]]:
    return [
        {"template_id": "constructed_60_15", "label": "Constructed 60 + 15"},
        {"template_id": "commander_100", "label": "Commander 100"},
        {"template_id": "no_sideboard", "label": "No Sideboard"},
    ]
