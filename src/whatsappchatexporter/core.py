"""Core logic for WhatsApp chat export workflows."""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import shutil


@dataclass(frozen=True)
class ExportRequest:
    source: Path
    destination: Path
    format: str = "txt"


@dataclass(frozen=True)
class ExportResult:
    exported_chats: int
    output_path: Path
    exported_files: tuple[Path, ...]


class ExportError(ValueError):
    """Raised when export configuration is invalid."""


def _copy_txt_files(source: Path, destination: Path) -> tuple[Path, ...]:
    if source.is_file():
        target = destination / source.name
        shutil.copy2(source, target)
        return (target,)

    exported: list[Path] = []
    for txt_file in sorted(source.glob("*.txt")):
        target = destination / txt_file.name
        shutil.copy2(txt_file, target)
        exported.append(target)
    return tuple(exported)


def export_chats(request: ExportRequest) -> ExportResult:
    """Export chat data to the requested format.

    Args:
        request: Export configuration including source and destination.

    Returns:
        ExportResult with summary output.
    """
    if request.format.lower() != "txt":
        raise ExportError("Formato no soportado. Usa 'txt'.")

    if not request.source.exists():
        raise ExportError(f"Origen no encontrado: {request.source}")

    request.destination.mkdir(parents=True, exist_ok=True)
    exported_files = _copy_txt_files(request.source, request.destination)

    summary_path = request.destination / "export-summary.txt"
    summary_path.write_text(
        "Exportación completada.\n"
        f"Origen: {request.source}\n"
        f"Formato: {request.format}\n"
        f"Archivos exportados: {len(exported_files)}\n",
        encoding="utf-8",
    )
    return ExportResult(
        exported_chats=len(exported_files),
        output_path=summary_path,
        exported_files=exported_files,
    )
