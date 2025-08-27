from __future__ import annotations
from typing import TypedDict, Dict, Any, List, Optional


class AgentState(TypedDict, total=False):
    customer_name: str
    email: str
    query: str
    priority: str
    ticket_id: str


# Derived / working fields
structured_request: Dict[str, Any]
entities: Dict[str, Any]
normalized: Dict[str, Any]
enrichment: Dict[str, Any]
flags: Dict[str, Any]


# ASK/WAIT
pending_question: Optional[str]
answer: Optional[str]


# RETRIEVE
kb_results: List[Dict[str, Any]]


# DECIDE
solution_score: int
escalated: bool


# UPDATE
ticket_updates: Dict[str, Any]


# CREATE
draft_response: str


# DO
actions_triggered: List[str]


# FINAL
final_payload: Dict[str, Any]


# Meta
logs: List[str]