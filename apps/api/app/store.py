from __future__ import annotations

from collections.abc import Iterable
from uuid import uuid4

from fastapi import HTTPException

from .models import (
    BoardAssignment,
    ExportCsvRequest,
    GroupPatch,
    GroupedCard,
    SessionData,
    SessionStatus,
)


class SessionStore:
    def __init__(self) -> None:
        self.sessions: dict[str, SessionData] = {}

    def create_session(self) -> SessionData:
        session = SessionData()
        self.sessions[session.session_id] = session
        return session

    def get_session(self, session_id: str) -> SessionData:
        session = self.sessions.get(session_id)
        if session is None:
            raise HTTPException(status_code=404, detail="Session not found")
        return session

    def attach_image(self, session_id: str) -> str:
        session = self.get_session(session_id)
        image_id = str(uuid4())
        session.image_id = image_id
        session.status = SessionStatus.uploaded
        return image_id

    def process(self, session_id: str) -> str:
        session = self.get_session(session_id)
        session.status = SessionStatus.processing
        session.progress = 0.25
        session.groups = self._mock_groups()
        session.progress = 1.0
        session.status = SessionStatus.needs_review if any(g.needs_review for g in session.groups) else SessionStatus.ready
        return str(uuid4())

    def patch_group(self, session_id: str, group_id: str, payload: GroupPatch) -> GroupedCard:
        session = self.get_session(session_id)
        for group in session.groups:
            if group.group_id == group_id:
                if payload.assigned_board is not None:
                    group.assigned_board = payload.assigned_board
                if payload.confirmed_oracle_id:
                    group.oracle_id = payload.confirmed_oracle_id
                if payload.confirmed_name:
                    group.name = payload.confirmed_name
                if payload.confirmed_printing_id:
                    group.printing_id = payload.confirmed_printing_id
                if payload.confirmed_set_code:
                    group.set_code = payload.confirmed_set_code
                if payload.confirmed_collector_number:
                    group.collector_number = payload.confirmed_collector_number
                if payload.user_notes is not None:
                    group.user_notes = payload.user_notes

                group.needs_review = group.printing_confidence < 0.85 and group.assigned_board == BoardAssignment.unknown
                session.status = SessionStatus.needs_review if any(g.needs_review for g in session.groups) else SessionStatus.ready
                return group

        raise HTTPException(status_code=404, detail="Group not found")

    def export_csv(self, session_id: str, payload: ExportCsvRequest) -> None:
        session = self.get_session(session_id)
        if payload.strict_printing:
            failed = [g for g in session.groups if g.printing_confidence < (payload.confidence_threshold or 0.85)]
            if failed:
                raise HTTPException(status_code=400, detail="Strict printing export failed: unresolved printings")

    @staticmethod
    def count_unassigned(groups: Iterable[GroupedCard]) -> int:
        return len([g for g in groups if g.assigned_board == BoardAssignment.unknown])

    @staticmethod
    def count_needs_review(groups: Iterable[GroupedCard]) -> int:
        return len([g for g in groups if g.needs_review])

    @staticmethod
    def _mock_groups() -> list[GroupedCard]:
        return [
            GroupedCard(
                oracle_id="oracle-lightning-bolt",
                name="Lightning Bolt",
                qty=4,
                assigned_board=BoardAssignment.main,
                printing_id="d31b8f58-f2d9-4f36-9f87-a846f9e15f89",
                set_code="2x2",
                collector_number="117",
                printing_confidence=0.96,
                needs_review=False,
            ),
            GroupedCard(
                oracle_id="oracle-brainstorm",
                name="Brainstorm",
                qty=2,
                assigned_board=BoardAssignment.unknown,
                set_code="mystery",
                collector_number="?",
                printing_confidence=0.42,
                needs_review=True,
                printing_candidates=[],
            ),
        ]
