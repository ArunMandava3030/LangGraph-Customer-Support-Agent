from __future__ import annotations
from typing import Any, Dict
from .base import MCPClient


class CommonClient(MCPClient):
    def __init__(self):
        super().__init__("COMMON")

    def call_ability(self, ability: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        if ability == "accept_payload":
            return {"accepted": True}
        if ability == "parse_request_text":
            text = payload.get("query", "")
            return {"structured_request": {"intent": "support_request", "text": text}}
        if ability == "normalize_fields":
            return {"normalized": {"priority": payload.get("priority", "medium").lower()}}
        if ability == "add_flags_calculations":
            pr = payload.get("normalized", {}).get("priority", "medium")
            return {"flags": {"sla_risk": pr in ("high", "urgent")}}
        if ability == "store_answer":
            return {"answer": payload.get("answer")}
        if ability == "store_data":
            return {"kb_results": payload.get("kb_results", [])}
        if ability == "solution_evaluation":
            base = 70 + (10 if payload.get("kb_results") else 0) + (10 if payload.get("answer") else 0)
            return {"solution_score": min(base, 100)}
        if ability == "update_payload":
            return {"decision": "recorded"}
        if ability == "response_generation":
            text = payload.get("query", "")
            return {"draft_response": f"Hi {payload.get('customer_name','')}, we are working on: {text}"}
        if ability == "output_payload":
            return {"final_payload": payload}
        return {}