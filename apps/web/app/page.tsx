"use client";

import { useMemo, useState } from "react";
import type { GroupedCard, SessionResponse } from "@shared/client";

const API_BASE = process.env.NEXT_PUBLIC_API_URL ?? "http://localhost:8000/api";

async function createSession() {
  const res = await fetch(`${API_BASE}/sessions`, { method: "POST" });
  return (await res.json()) as { session_id: string };
}

export default function HomePage() {
  const [sessionId, setSessionId] = useState<string>("");
  const [session, setSession] = useState<SessionResponse | null>(null);
  const [error, setError] = useState<string>("");

  const groups = useMemo(() => session?.groups ?? [], [session]);

  const onStart = async () => {
    setError("");
    const created = await createSession();
    setSessionId(created.session_id);
  };

  const onProcess = async () => {
    if (!sessionId) {
      setError("Create a session first");
      return;
    }

    const fakeFile = new File(["stub"], "cards.txt", { type: "text/plain" });
    const formData = new FormData();
    formData.append("file", fakeFile);

    await fetch(`${API_BASE}/sessions/${sessionId}/image`, {
      method: "POST",
      body: formData
    });

    await fetch(`${API_BASE}/sessions/${sessionId}/process`, { method: "POST" });
    const next = await fetch(`${API_BASE}/sessions/${sessionId}`);
    setSession((await next.json()) as SessionResponse);
  };

  const updateBoard = async (group: GroupedCard, assigned: GroupedCard["assigned_board"]) => {
    const res = await fetch(`${API_BASE}/sessions/${sessionId}/groups/${group.group_id}`, {
      method: "PATCH",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ assigned_board: assigned })
    });
    const updated = (await res.json()) as GroupedCard;

    setSession((prev) => {
      if (!prev) return prev;
      const updatedGroups = prev.groups.map((g) => (g.group_id === updated.group_id ? updated : g));
      return {
        ...prev,
        groups: updatedGroups,
        unassigned_count: updatedGroups.filter((g) => g.assigned_board === "unknown").length,
        needs_review_count: updatedGroups.filter((g) => g.needs_review).length
      };
    });
  };

  return (
    <main>
      <h1>MTG Session MVP</h1>
      <p>No auth session workflow with board assignment editing and review flags.</p>

      <div className="card row">
        <button onClick={onStart}>1) Create session</button>
        <button onClick={onProcess} className="secondary">
          2) Upload + process sample image
        </button>
        <span>Session: {sessionId || "(none)"}</span>
      </div>

      {error && <p>{error}</p>}

      {session && (
        <div className="card">
          <p className="status">Status: {session.status}</p>
          <p>
            Unassigned: {session.unassigned_count} | Needs review: {session.needs_review_count}
          </p>

          {groups.map((group) => (
            <div key={group.group_id} className="card">
              <strong>
                {group.qty}x {group.name}
              </strong>
              <p>
                Board: {group.assigned_board} · Printing confidence: {Math.round(group.printing_confidence * 100)}%
              </p>
              <div className="row">
                <button onClick={() => updateBoard(group, "main")}>Main</button>
                <button onClick={() => updateBoard(group, "side")} className="secondary">
                  Side
                </button>
                <button onClick={() => updateBoard(group, "none")} className="secondary">
                  None
                </button>
              </div>
            </div>
          ))}
        </div>
      )}
    </main>
  );
}
