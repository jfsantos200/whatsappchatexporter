"""CLI entrypoint for WhatsApp chat export workflows."""
from __future__ import annotations

from pathlib import Path

import typer

from whatsappchatexporter.core import ExportRequest, export_chats

app = typer.Typer(help="Herramienta para exportar y respaldar chats de WhatsApp.")


@app.command()
def exportar(
    source: Path = typer.Option(
        ..., "--source", "-s", help="Ruta de la copia o carpeta de origen."
    ),
    destination: Path = typer.Option(
        ..., "--destination", "-d", help="Carpeta donde guardar la exportación."
    ),
    format: str = typer.Option("txt", "--format", "-f", help="Formato de salida."),
) -> None:
    """Exporta chats desde una fuente local a archivos de salida."""
    result = export_chats(ExportRequest(source=source, destination=destination, format=format))
    typer.echo(
        "Exportación preparada. "
        f"Archivos: {result.exported_chats}. "
        f"Resumen: {result.output_path}"
    )
