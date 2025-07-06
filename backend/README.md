# ⚙️ Backend (FastAPI + Celery)

Handles API requests and delegates video generation tasks using Celery workers.

## Features

- `/generate-video`: Accepts prompt and launches job pipeline
- Celery worker to run Mixtral → SDXL → AnimateDiff

## Run Locally

```bash
uvicorn app.main:app --reload
celery -A app.workers.tasks worker --loglevel=info
```

## Dependencies

- FastAPI
- Celery
- Redis
- Uvicorn
