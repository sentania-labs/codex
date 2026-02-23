from __future__ import annotations

from datetime import datetime, timezone
from enum import Enum
from typing import Optional
from uuid import uuid4

from pydantic import BaseModel, Field


class SessionStatus(str, Enum):
    uploaded = "uploaded"
    processing = "processing"
    needs_review = "needs_review"
    ready = "ready"
    exporting = "exporting"
    complete = "complete"
    failed = "failed"


class BoardAssignment(str, Enum):
    main = "main"
    side = "side"
    none = "none"
    unknown = "unknown"


class PrintingCandidate(BaseModel):
    printing_id: str
    set_code: str
    collector_number: str
    confidence: float


class GroupedCard(BaseModel):
    group_id: str = Field(default_factory=lambda: str(uuid4()))
    oracle_id: str
    name: str
    qty: int = 1
    assigned_board: BoardAssignment = BoardAssignment.unknown
    printing_id: Optional[str] = None
    set_code: Optional[str] = None
    collector_number: Optional[str] = None
    printing_confidence: float = 0.0
    printing_candidates: list[PrintingCandidate] = Field(default_factory=list)
    needs_review: bool = False
    user_notes: Optional[str] = None


class SessionData(BaseModel):
    session_id: str = Field(default_factory=lambda: str(uuid4()))
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    status: SessionStatus = SessionStatus.uploaded
    image_id: Optional[str] = None
    progress: Optional[float] = None
    groups: list[GroupedCard] = Field(default_factory=list)


class SessionCreateResponse(BaseModel):
    session_id: str


class UploadImageResponse(BaseModel):
    image_id: str


class ProcessResponse(BaseModel):
    job_id: str


class SessionResponse(BaseModel):
    session_id: str
    status: SessionStatus
    progress: Optional[float]
    groups: list[GroupedCard]
    unassigned_count: int
    needs_review_count: int


class GroupPatch(BaseModel):
    assigned_board: Optional[BoardAssignment] = None
    confirmed_oracle_id: Optional[str] = None
    confirmed_name: Optional[str] = None
    confirmed_printing_id: Optional[str] = None
    confirmed_set_code: Optional[str] = None
    confirmed_collector_number: Optional[str] = None
    user_notes: Optional[str] = None


class ExportPdfRequest(BaseModel):
    template_id: str
    fields: dict[str, str] = Field(default_factory=dict)
    confidence_threshold: Optional[float] = None


class ExportCsvRequest(BaseModel):
    adapter: str = "moxfield_collection"
    confidence_threshold: Optional[float] = None
    strict_printing: bool = False


class ExportResponse(BaseModel):
    export_id: str
    download_url: str
