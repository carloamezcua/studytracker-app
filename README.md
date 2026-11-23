# studytracker-app

Aplicación web contenerizada para el registro y análisis de sesiones de estudio, con seguimiento de materias, experiencia (XP), retención (FSRS 1–4), uso de IA e índice de deuda cognitiva.

> **Estado del proyecto:** Fase 0 (estructura base, configuración de entorno y dependencias definidas).  
> La arquitectura completa, los contratos de datos y el plan de desarrollo paso a paso se encuentran en [`docs/GUIA_DESARROLLO.md`](docs/GUIA_DESARROLLO.md).

## Stack tecnológico

- **Contenedores:** Docker y Docker Compose
- **Base de datos:** PostgreSQL 16
- **Backend:** Python 3.12, FastAPI, SQLAlchemy 2.0, Pydantic v2 y Uvicorn
- **Frontend:** HTML5, Tailwind CSS, JavaScript (ES Modules) y Chart.js
- **Pruebas:** pytest y httpx

## Estructura inicial

```text
studytracker-app/
├── .env.example              # Plantilla de variables de entorno
├── .gitignore                # Exclusiones de Git (incluye .env y .venv/)
├── requirements.txt          # Dependencias Python con versiones fijadas
├── docs/
│   └── GUIA_DESARROLLO.md    # Guía de arquitectura y desarrollo por fases
├── app/
│   ├── routers/              # Endpoints REST
│   └── static/               # Interfaz web (HTML, CSS y JS modular)
├── data/                     # Datos de muestra para carga inicial (seed)
└── tests/                    # Pruebas unitarias y de integración
```

## Configuración inicial

### 1. Variables de entorno

Copia la plantilla para crear tu archivo local `.env` (ignorado por Git):

```bash
cp .env.example .env
```

### 2. Entorno virtual de Python (opcional para desarrollo local)

La ejecución principal del proyecto se realiza mediante Docker. Si deseas autocompletado, tipado y ejecución local de herramientas desde tu editor, crea un entorno virtual `.venv` (ya excluido en `.gitignore`):

**Windows (PowerShell):**

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

**Linux / macOS:**

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Convenciones del repositorio

- **Commits:** Conventional Commits en español (`feat`, `fix`, `build`, `chore`, `docs`, `test`, `refactor`, `style`).
- **Versionado:** Semantic Versioning por hitos ejecutables (`v0.1.0` → `v1.0.0`), detallado en [`docs/GUIA_DESARROLLO.md`](docs/GUIA_DESARROLLO.md).
