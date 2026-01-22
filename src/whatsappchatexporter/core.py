"""Core logic for WhatsApp chat export workflows."""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class ExportRequest:
    source: Path
    destination: Path
    format: str = "txt"


@dataclass(frozen=True)
class ExportResult:
    exported_chats: int
    output_path: Path


def export_chats(request: ExportRequest) -> ExportResult:
    """Placeholder export logic for WhatsApp chat data.

    Args:
        request: Export configuration including source and destination.

    Returns:
        ExportResult with summary output.
    """
    request.destination.mkdir(parents=True, exist_ok=True)
    summary_path = request.destination / "export-summary.txt"
    summary_path.write_text(
        "Exportación inicial preparada.\n"
        f"Origen: {request.source}\n"
        f"Formato: {request.format}\n",
        encoding="utf-8",
    )
    return ExportResult(exported_chats=0, output_path=summary_path)
