from celery import Celery
import subprocess

celery = Celery("worker", broker="redis://redis:6379/0")

@celery.task
def generate_video_pipeline(prompt: str):
    subprocess.run(["python", "llm/run_mixtral.py", prompt])
    subprocess.run(["python", "imagegen/generate_image.py", prompt])
    subprocess.run(["python", "videogeneration/animate.py", prompt])
    return "Video generated"
