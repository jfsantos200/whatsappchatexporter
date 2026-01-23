# La Herramienta Definitiva para Transferir Chats de WhatsApp

Transfiere o exporta los chats de WhatsApp (Business) de Android o PC sin complicaciones. **No. 1**

## Características destacadas

### ✅ Sin necesidad de reinicio
Transfiere o exporta los chats de WhatsApp (Business) de Android o PC sin complicaciones.

### ⭐ Restauración rápida (DESTACADO)
Restaura los chats de WhatsApp desde Google Drive a `.txt` de forma masiva y sin esfuerzo.

### 🆓 Copia de seguridad gratuita
Realiza respaldos de los chats de WhatsApp (Business) en tu computadora. **Gratis**: solo conecta tu smartphone por USB para hacerlo.

## Objetivo del proyecto

Este proyecto busca **exportar chats directamente desde WhatsApp Business**, sin pasos manuales ni exportaciones previas. La meta es permitir la extracción de chats desde el dispositivo o desde copias de seguridad legítimas (por ejemplo, Google Drive), con un flujo claro y automatizado.

## Estado actual

- La herramienta **aún no se conecta directamente a WhatsApp Business**.
- Actualmente **solo copia archivos `.txt` locales** a una carpeta de destino y genera un resumen.
- La conexión directa con WhatsApp Business está planificada como siguiente fase del desarrollo.

## Cómo funciona

1. Conecta tu smartphone por USB a tu computadora.
2. Selecciona los chats o grupos que deseas transferir o exportar.
3. Elige el formato de salida: `.txt` para lectura rápida o exportación masiva.
4. Inicia el proceso y guarda los archivos en tu carpeta de destino.

## Casos de uso

- Migrar conversaciones entre dispositivos sin perder historial.
- Exportar chats para auditorías, soporte o cumplimiento.
- Crear respaldos personales accesibles sin conexión.

## Compatibilidad

- WhatsApp y WhatsApp Business.
- Android y copias desde Google Drive.
- Exportación a texto plano (`.txt`) para archivado y lectura sin internet.

## Beneficios clave

- No requiere reinicio de fábrica.
- Conserva el historial completo de mensajes.
- Ideal para migraciones, auditorías o respaldo personal.
- Proceso guiado con resultados en minutos.

## Stack recomendado

Para un desarrollo estable, seguro y multiplataforma, proponemos el siguiente stack:

- **Backend (core de exportación):** Python 3.11 con librerías para cifrado, descompresión y parsing de bases de datos.
- **CLI:** Typer para automatizar flujos y permitir exportaciones masivas.
- **Desktop (UI):** Electron + React para una interfaz clara en Windows/macOS/Linux.
- **Android companion (opcional):** Kotlin para automatizar permisos y lectura local cuando sea necesario.
- **Automatización:** GitHub Actions para builds y validaciones.

Este stack permite cubrir PC y Android, mantener la lógica en un core reutilizable y ofrecer experiencia de usuario sencilla.

## Inicio rápido (CLI)

```bash
pip install -e .
whatsappchatexporter exportar --source /ruta/origen --destination /ruta/salida
```

El comando copiará los `.txt` desde la ruta de origen y generará un resumen de exportación en la carpeta de destino.

### Formatos soportados

- `.txt` (por ahora). La ruta de origen puede ser un archivo o una carpeta con varios `.txt`.

## Cómo probar la exportación a `.txt`

1. Crea una carpeta de origen con archivos `.txt` de ejemplo:

```bash
mkdir -p /tmp/wa-origen
printf "Chat de prueba\n" > /tmp/wa-origen/chat1.txt
printf "Otro chat\n" > /tmp/wa-origen/chat2.txt
```

2. Ejecuta la exportación hacia una carpeta de destino:

```bash
mkdir -p /tmp/wa-salida
whatsappchatexporter exportar --source /tmp/wa-origen --destination /tmp/wa-salida
```

3. Verifica los resultados:

```bash
ls -la /tmp/wa-salida
cat /tmp/wa-salida/export-summary.txt
```

Deberías ver los `.txt` copiados y un archivo `export-summary.txt` con el resumen de la exportación.

## Preguntas frecuentes

**¿Necesito iniciar sesión en mi cuenta de Google?**
Sí, solo para acceder a tus propias copias de seguridad de Google Drive.

**¿Se pueden exportar chats en lote?**
Sí, la exportación masiva permite generar múltiples archivos `.txt` en una sola ejecución.

**¿Se borran mis chats originales?**
No, el proceso es de lectura y exportación. Tus chats se mantienen intactos.

## Nota importante

Este proyecto solo exporta tus propios datos. Asegúrate de cumplir con las políticas de WhatsApp y la normativa local sobre privacidad.
