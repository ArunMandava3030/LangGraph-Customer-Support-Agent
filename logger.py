from typing import List
from rich.console import Console


console = Console()


def log(logs: List[str], message: str) -> None:
    logs.append(message)
    console.print(f"[bold cyan]LOG[/]: {message}")