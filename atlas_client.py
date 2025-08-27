from __future__ import annotations
from typing import Any, Dict, List
from .base import MCPClient


class AtlasClient(MCPClient):
    def __init__(self):
        super().__init__("ATLAS")

    def call_ability(self, ability: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        if ability == "extract_entities":
            text = payload.get("query", "")
            entities: Dict[str, Any] = {}
            if "order" in text.lower():
                entities["topic"] = "order"
            if "payment" in text.lower():
                entities["topic"] = "payment"
            return {"entities": entities}

        if ability == "enrich_records":
            return {
                "enrichment": {
                    "sla_hours": 24,
                    "history": [{"ticket_id": "T-100", "status": "closed"}],
                }
            }

        if ability == "clarify_question":
            missing = []
            if not payload.get("ticket_id"):
                missing.append("ticket_id")
            return {
                "pending_question": (
                    f"Could you confirm {', '.join(missing)}?" if missing else ""
                )
            }

        if ability == "extract_answer":
            ans = payload.get("simulated_answer", "")
            return {"answer": ans}

        if ability == "knowledge_base_search":
            q = payload.get("query", "")
            kb: List[Dict[str, Any]] = []
            if q:
                kb.append(
                    {"id": "KB-42", "title": "Track your order", "confidence": 0.92}
                )
            return {"kb_results": kb}

        if ability == "escalation_decision":
            score = int(payload.get("solution_score", 0))
            return {
                "escalated": score < 90,
                "reason": "Low confidence score" if score < 90 else "Auto-resolved",
            }

        if ability == "update_ticket":
            return {"ticket_updated": True, "ticket_id": payload.get("ticket_id")}

        if ability == "close_ticket":
            return {"ticket_closed": True, "ticket_id": payload.get("ticket_id")}

        if ability == "execute_api_calls":
            return {"api_executed": True, "details": "CRM system updated"}

        if ability == "trigger_notifications":
            return {"notification_sent": True, "channel": "email"}

        raise ValueError(f"[AtlasClient] Unknown ability: {ability}")
