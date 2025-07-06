# 🧠 Text-to-Video AI (Monorepo)

This is a monorepo for converting text prompts into videos using state-of-the-art open-source AI models.

## 🧱 Projects

- [`/backend`](./backend) - FastAPI backend with Celery
- [`/frontend`](./frontend) - React UI for prompt input
- [`/llm`](./llm) - Mixtral 8x7B prompt-to-structure module
- [`/imagegen`](./imagegen) - SDXL image generator
- [`/videogeneration`](./videogeneration) - AnimateDiff-based video generation

## 🛠 How to Run

See individual folders for setup instructions, or use Docker:

```bash
docker-compose up --build
```

## 📁 Output

Generated images/videos are saved in `/output`.

---
