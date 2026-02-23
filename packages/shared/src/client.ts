// Generated from apps/api OpenAPI schema. Run `make generate-types` to refresh.

export type SessionStatus =
  | "uploaded"
  | "processing"
  | "needs_review"
  | "ready"
  | "exporting"
  | "complete"
  | "failed";

export type BoardAssignment = "main" | "side" | "none" | "unknown";

export interface PrintingCandidate {
  printing_id: string;
  set_code: string;
  collector_number: string;
  confidence: number;
}

export interface GroupedCard {
  group_id: string;
  oracle_id: string;
  name: string;
  qty: number;
  assigned_board: BoardAssignment;
  printing_id?: string | null;
  set_code?: string | null;
  collector_number?: string | null;
  printing_confidence: number;
  printing_candidates: PrintingCandidate[];
  needs_review: boolean;
  user_notes?: string | null;
}

export interface SessionResponse {
  session_id: string;
  status: SessionStatus;
  progress?: number | null;
  groups: GroupedCard[];
  unassigned_count: number;
  needs_review_count: number;
}
