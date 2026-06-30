# ShadowBoard AI
Enterprise Multi-Agent Decision Intelligence Platform.

## Structure
* **backend/**: FastAPI app, AI agents, services
* **frontend/**: React + Vite + TypeScript UI
* **infra/docker/**: Docker Compose for Postgres, Redis, Qdrant

## Local Development
1. **Start infrastructure**: `cd infra/docker && docker compose up -d`
2. **Start backend**: `cd backend && source venv/bin/activate && uvicorn app.main:app --reload`
3. **Start frontend**: `cd frontend && npm run dev`

Full setup instructions: see the implementation guide PDFs (Parts 1-8).