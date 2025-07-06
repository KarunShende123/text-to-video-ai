from fastapi import APIRouter, BackgroundTasks, Request
from backend.app.workers.tasks import generate_video_pipeline

router = APIRouter()

@router.post("/generate-video")
async def generate_video(request: Request, background_tasks: BackgroundTasks):
    data = await request.json()
    prompt = data.get("prompt")
    task = generate_video_pipeline.delay(prompt)
    return {"task_id": task.id}
