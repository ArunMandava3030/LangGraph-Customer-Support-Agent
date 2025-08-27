from __future__ import annotations
from typing import Any, Dict


class MCPClient:
    name: str


    def __init__(self, name: str):
        self.name = name

    def call_ability(self, ability: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        raise NotImplementedError