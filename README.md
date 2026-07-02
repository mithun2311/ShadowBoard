# ShadowBoard AI

> **Enterprise Multi-Agent Decision Intelligence Platform powered by Google ADK, Gemini, Qdrant, and FastAPI.**

ShadowBoard AI is an enterprise-grade decision intelligence platform that combines **Google Agent Development Kit (ADK)**, **Gemini**, **Qdrant**, and a **multi-agent architecture** to help organizations make strategic decisions through collaborative AI reasoning, Retrieval-Augmented Generation (RAG), and executive intelligence.

---

# Features

- Multi-Agent Executive AI Architecture
- Google Agent Development Kit (ADK)
- Google Gemini 2.5 Flash
- Retrieval-Augmented Generation (RAG)
- Qdrant Vector Database
- Semantic Document Search
- Enterprise Knowledge Base
- JWT Authentication
- Project Management
- Document Upload & Processing
- PDF / DOCX / PPTX / TXT Support
- Executive Decision Intelligence
- Agent-to-Agent (A2A) Collaboration Framework
- Model Context Protocol (MCP) Ready Architecture
- Lyzr-Compatible Workflow Integration
- FastAPI REST APIs
- React + TypeScript Frontend

---

# Tech Stack

## Backend

- FastAPI
- SQLAlchemy
- PostgreSQL
- Alembic
- Redis
- Celery
- JWT Authentication

## Frontend

- React
- TypeScript
- Vite
- Tailwind CSS

## AI & Agentic Stack

- Google Agent Development Kit (ADK)
- Google Gemini 2.5 Flash
- Multi-Agent Executive Architecture
- Retrieval-Augmented Generation (RAG)
- Qdrant Vector Database
- Agent-to-Agent (A2A)
- Model Context Protocol (MCP)
- Lyzr-Compatible Workflow Integration

---

# Executive Agents

ShadowBoard AI consists of specialized executive agents:

- CEO (Root Agent)
- CFO Agent
- Product Strategy Agent
- Engineering Agent
- Marketing Agent
- Legal Agent
- Risk Management Agent
- Moderator Agent

Each specialist independently analyzes the problem before contributing to a consolidated executive recommendation.

---

# Project Structure

```
ShadowBoard
│
├── backend
│   ├── agents
│   │   ├── specialists
│   │   ├── tools
│   │   ├── prompts
│   │   ├── runtime.py
│   │   └── root_agent.py
│   │
│   ├── app
│   │   ├── api
│   │   ├── core
│   │   ├── db
│   │   ├── schemas
│   │   ├── services
│   │   └── utils
│   │
│   ├── alembic
│   ├── uploads
│   └── requirements.txt
│
├── frontend
│   ├── src
│   ├── public
│   └── package.json
│
├── infra
│   └── docker
│       └── docker-compose.yml
│
└── README.md
```

---

# Architecture

```
                     User
                       │
                       ▼
               FastAPI Backend
                       │
          Google ADK Runtime Runner
                       │
                       ▼
                CEO Root Agent
                       │
      ┌────────────────────────────────┐
      │        Executive Routing        │
      └────────────────────────────────┘
        │      │      │      │      │
        ▼      ▼      ▼      ▼      ▼
      CFO   Product Engineering Legal Marketing Risk
        │      │      │      │      │
        └──────────────┬──────────────┘
                       ▼
              A2A Collaboration Layer
                       ▼
              Moderator Executive Agent
                       ▼
             Final Executive Response
```

---

# RAG Pipeline

```
Upload Document
        │
        ▼
Text Extraction
        │
        ▼
Chunking
        │
        ▼
Gemini Embeddings
        │
        ▼
Qdrant Indexing
        │
        ▼
Semantic Retrieval
        │
        ▼
Executive AI Agents
```

---

# AI Workflow

1. User submits a business query.
2. CEO Root Agent receives the request.
3. Relevant specialist agents are selected.
4. Agents independently analyze the problem.
5. A2A collaboration exchanges executive insights.
6. Moderator Agent consolidates recommendations.
7. Final executive response is generated.

---

# Document Intelligence

Supported formats:

- PDF
- DOCX
- PPTX
- TXT

Pipeline:

- Upload
- Text Extraction
- Chunking
- Embedding Generation
- Vector Indexing
- Semantic Retrieval
- Executive AI Reasoning

---

# Local Development

## 1. Clone Repository

```bash
git clone https://github.com/mithun2311/ShadowBoard.git

cd ShadowBoard
```

---

## 2. Start Infrastructure

```bash
cd infra/docker

docker compose up -d
```

Services started:

- PostgreSQL
- Redis
- Qdrant

---

## 3. Backend Setup

```bash
cd backend

python -m venv venv
```

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run database migrations

```bash
alembic upgrade head
```

Start backend

```bash
uvicorn app.main:app --reload
```

Backend:

```
http://localhost:8000
```

Swagger UI:

```
http://localhost:8000/docs
```

---

## 4. Frontend Setup

```bash
cd frontend

npm install

npm run dev
```

Frontend:

```
http://localhost:5173
```

---

# Environment Variables

Create a `.env` file inside the backend directory.

```env
DATABASE_URL=

JWT_SECRET_KEY=
JWT_ALGORITHM=HS256
JWT_EXPIRE_MINUTES=60

GEMINI_API_KEY=

QDRANT_URL=
QDRANT_API_KEY=
QDRANT_COLLECTION=

REDIS_URL=
```

---

# API Modules

- Authentication
- Projects
- Documents
- AI Query
- Executive Agents
- Semantic Search

---

# Deployment

## Backend

- Render

## Frontend

- Vercel

## Database

- Neon PostgreSQL

## Vector Database

- Qdrant Cloud

## AI Infrastructure

- Google Agent Development Kit (ADK)
- Google Gemini
- Multi-Agent Architecture
- Retrieval-Augmented Generation (RAG)
- A2A Collaboration Framework
- MCP-Ready Architecture
- Lyzr-Compatible Workflow Integration

---

# Future Enhancements

- Full MCP Tool Integration
- Live Agent-to-Agent Messaging
- Lyzr Workflow Automation
- Enterprise RBAC
- Agent Memory Persistence
- Multi-Tenant Support
- Analytics Dashboard
- Streaming AI Responses

---

# License

MIT License



---

# Acknowledgements

- Google Agent Development Kit (ADK)
- Google Gemini API
- Qdrant Vector Database
- FastAPI
- React
- SQLAlchemy
- Vite
- Render
- Neon PostgreSQL
