# 🏨 Atithi Sathi AI

<p align="center">

  <img src="https://img.shields.io/badge/🤖-AI%20Hotel%20Concierge-7C3AED?style=for-the-badge" />
  <img src="https://img.shields.io/badge/⚡-FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white" />
  <img src="https://img.shields.io/badge/⚛️-React-61DAFB?style=for-the-badge&logo=react&logoColor=black" />
  <img src="https://img.shields.io/badge/🗄️-PostgreSQL-336791?style=for-the-badge&logo=postgresql&logoColor=white" />
  <img src="https://img.shields.io/badge/🧠-Gemini%20AI-4285F4?style=for-the-badge&logo=google&logoColor=white" />

</p>

<p align="center">

  <img src="https://img.shields.io/badge/🔧-Tool%20Calling-FF6B35?style=for-the-badge" />
  <img src="https://img.shields.io/badge/🌐-Hotel%20Search-06B6D4?style=for-the-badge" />
  <img src="https://img.shields.io/badge/🔐-Secure%20Backend-16A34A?style=for-the-badge" />
  <img src="https://img.shields.io/badge/🚀-Production%20Ready-22C55E?style=for-the-badge" />

</p>

---

# 🌟 What is Atithi Sathi AI?

> **Atithi Sathi AI is an intelligent AI-powered hotel guest companion that allows guests to search hotels, discover hotel information, ask questions, and interact with hotel services using natural language.**

Instead of making guests navigate through multiple hotel pages, menus, filters, FAQs, and search screens, Atithi Sathi AI provides a conversational experience.

### 💬 Simply ask:

```text
"Find me a hotel in Indiranagar."

"Does this hotel have a swimming pool?"

"What amenities are available?"

"What time is check-in?"

"Do you have Wi-Fi?"

"Show me hotels near Bangalore."

"Which hotel has a gym?"

"I need a hotel for two guests."

✨ Core Features

| Feature              | Description                        |
| -------------------- | ---------------------------------- |
| 🤖 AI Concierge      | Conversational hotel assistant     |
| 🔎 Hotel Search      | Natural-language hotel discovery   |
| 🏨 Hotel Information | Property and hotel information     |
| 🛏️ Room Information | Room-related information           |
| 🏊 Amenities         | Hotel facilities and services      |
| 📋 Policies          | Hotel policies and FAQs            |
| 📅 Availability      | Availability-oriented workflows    |
| 🔧 Tool Calling      | AI can invoke backend capabilities |
| 🗄️ Database         | Structured hotel information       |
| 🌐 External Search   | External hotel search integration  |
| 💬 Conversation      | Natural multi-turn interaction     |
| 🛡️ Validation       | Request and tool validation        |
| ⚠️ Error Handling    | Controlled failure handling        |


🤖 AI HOTEL CONCIERGE

Atithi Sathi AI is designed around natural conversation.


┌─────────────────────────────────────────────┐
│              ATITHI SATHI AI                │
├─────────────────────────────────────────────┤
│                                             │
│ 👤 Does the hotel have a swimming pool?     │
│                                             │
│ 🤖 Yes! The hotel has a swimming pool       │
│    available for guests.                    │
│                                             │
└─────────────────────────────────────────────┘

🧠 AI TOOL CALLING

The most important architectural concept is that the AI does not directly access the database.

Instead, the AI can request a backend tool.

                 USER
                   │
                   ▼
          ┌─────────────────┐
          │ React Frontend  │
          └────────┬────────┘
                   │
                   ▼
          ┌─────────────────┐
          │ FastAPI Backend │
          └────────┬────────┘
                   │
                   ▼
          ┌─────────────────┐
          │   AI Provider   │
          └────────┬────────┘
                   │
                   ▼
             ┌───────────┐
             │  Gemini   │
             └─────┬─────┘
                   │
             Tool Required?
              ┌────┴────┐
             YES        NO
              │          │
              ▼          ▼
       Backend Tool   AI Response
              │
       ┌──────┴──────┐
       ▼             ▼
   Database      External API
       │             │
       └──────┬──────┘
              ▼
         Tool Result
              │
              ▼
            Gemini
              │
              ▼
        Final Response
              │
              ▼
            Guest


🌐 EXTERNAL HOTEL SEARCH

Atithi Sathi AI can use external hotel search services when additional hotel information is required.

Where configured, external hotel search can be integrated through services such as SerpApi.

Architecture:

Guest
  ↓
AI
  ↓
Hotel Search Tool
  ↓
External Search API
  ↓
Search Results
  ↓
AI
  ↓
Guest

🗄️ DATABASE ARCHITECTURE

Structured hotel information is handled through the backend data layer.

                BACKEND
                   │
                   ▼
             Service Layer
                   │
                   ▼
              PostgreSQL
                   │
          ┌────────┴────────┐
          ▼                 ▼
       Hotels            Rooms
          │                 │
          ▼                 ▼
      Amenities          Services


🔄 COMPLETE REQUEST LIFECYCLE

01. Guest sends message
            ↓
02. React sends API request
            ↓
03. FastAPI receives request
            ↓
04. AI Provider processes request
            ↓
05. Gemini understands intent
            ↓
06. Gemini determines whether a tool is required
            ↓
07. Backend validates tool request
            ↓
08. Backend executes tool
            ↓
09. Database / External API provides result
            ↓
10. Tool result returned to Gemini
            ↓
11. Gemini generates final response
            ↓
12. FastAPI returns response
            ↓
13. React displays response
            ↓
14. Guest receives answer


🏗️ SYSTEM ARCHITECTURE

<img width="2028" height="820" alt="mermaid-diagram" src="https://github.com/user-attachments/assets/91f5681a-9f85-4ff6-b49c-39464589620b" />

🔄 AI REQUEST FLOW

<img width="3064" height="2618" alt="mermaid-diagram (1)" src="https://github.com/user-attachments/assets/87453974-6d6a-4b9b-b493-f55d393ca666" />


🧠 GEMINI INTEGRATION

Atithi Sathi AI uses Google Gemini as the primary AI provider where configured.

The application follows a centralized provider architecture.

Application
      │
      ▼
 AI Provider
      │
      ▼
   Gemini
      │
      ▼
 Tool Calling
      │
      ▼
Backend Tools

🔐 AI PROVIDER CONFIGURATION


AI_PROVIDER=gemini
GEMINI_API_KEY=YOUR_GEMINI_API_KEY


🛡️ SECURITY

Security is a core part of the application architecture.


┌───────────────┐
│ React Client  │
└───────┬───────┘
        │
        ▼
┌──────────────────┐
│ FastAPI Backend  │
└───────┬──────────┘
        │
        ▼
┌──────────────────┐
│ Validation       │
└───────┬──────────┘
        │
        ▼
┌──────────────────┐
│ Services / Tools │
└───────┬──────────┘
        │
        ▼
┌──────────────────┐
│ DB / External API│
└──────────────────┘

🛠️ TECHNOLOGY STACK


| Layer                 | Technology                    |
| --------------------- | ----------------------------- |
| 🎨 Frontend           | React                         |
| ⚡ Backend             | FastAPI                       |
| 🐍 Backend Language   | Python                        |
| 🗄️ Database          | PostgreSQL                    |
| 🧠 AI                 | Google Gemini                 |
| 🔧 AI Capability      | Tool / Function Calling       |
| 🌐 External Search    | SerpApi                       |
| 🔌 API Style          | REST                          |
| 🔐 Configuration      | Environment Variables         |
| 🧪 Testing            | Project-configured test suite |
| 📦 Package Management | npm / pip                     |
| 🔀 Version Control    | Git / GitHub                  |


📁 PROJECT STRUCTURE


Atithi-Sathi-AI/
│
├── backend/
│   │
│   ├── app/
│   │   ├── ai/
│   │   │   ├── provider.py
│   │   │   └── ...
│   │   │
│   │   ├── api/
│   │   │   └── ...
│   │   │
│   │   ├── models/
│   │   │   └── ...
│   │   │
│   │   ├── schemas/
│   │   │   └── ...
│   │   │
│   │   ├── services/
│   │   │   └── ...
│   │   │
│   │   ├── tools/
│   │   │   └── ...
│   │   │
│   │   ├── config.py
│   │   └── main.py
│   │
│   ├── tests/
│   ├── requirements.txt
│   └── .env.example
│
├── frontend/
│   │
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── services/
│   │   └── ...
│   │
│   ├── public/
│   ├── package.json
│   └── ...
│
├── README.md
├── .gitignore
└── ...


💻 LOCAL DEVELOPMENT SETUP

🟢 Step 1 — Install Prerequisites

Make sure the following are installed:

Tool	Recommended
🐍 Python	3.11+
⚛️ Node.js	18+
📦 npm	9+
🗄️ PostgreSQL	14+
🔀 Git	Latest

Check versions:

python --version
node --version
npm --version
git --version

📥 Step 2 — Clone Repository

git clone YOUR_REPOSITORY_URL

Then:

cd Otithi-Sathi-AI

🐍 STEP 3 — BACKEND SETUP

Move to backend:

cd backend

Create virtual environment:

Windows
python -m venv venv

Activate:

venv\Scripts\activate
macOS / Linux
python3 -m venv venv

Activate:

source venv/bin/activate

📦 STEP 4 — INSTALL BACKEND DEPENDENCIES

pip install -r requirements.txt

Verify installation:

pip list

🗄️ STEP 5 — DATABASE SETUP

Create a PostgreSQL database.

Example:

CREATE DATABASE otithi_sathi_ai;

Configure:

DATABASE_URL=YOUR_DATABASE_URL

Example local format:

DATABASE_URL=postgresql://username:password@localhost:5432/Atithi_sathi_ai

🔐 STEP 6 — CREATE ENVIRONMENT FILE

Inside:

backend/

create:

.env

Example:

AI_PROVIDER=gemini

GEMINI_API_KEY=YOUR_GEMINI_API_KEY

DATABASE_URL=YOUR_DATABASE_URL

SERPAPI_API_KEY=YOUR_SERPAPI_API_KEY

SECRET_KEY=YOUR_SECRET_KEY

🤖 STEP 7 — CONFIGURE GEMINI

Get a Gemini API key from Google AI Studio.

Then add it to:

GEMINI_API_KEY=YOUR_GEMINI_API_KEY

Do not place the key in:

React frontend
GitHub
README.md
JavaScript source

The key should remain server-side.

🌐 STEP 8 — CONFIGURE EXTERNAL HOTEL SEARCH

If external hotel search is enabled, configure:

SERPAPI_API_KEY=YOUR_SERPAPI_API_KEY

The frontend should never directly use this key.

🗃️ STEP 9 — DATABASE MIGRATIONS

If Alembic is configured:

alembic upgrade head

Check current migration:

alembic current

Create a migration when required:

alembic revision --autogenerate -m "update database schema"

Then:

alembic upgrade head

🚀 STEP 10 — START BACKEND

From:

backend/

run:

uvicorn app.main:app --reload

Backend:

http://localhost:8000

Swagger:

http://localhost:8000/docs

ReDoc:

http://localhost:8000/redoc

⚛️ STEP 11 — FRONTEND SETUP

Open a second terminal.

Move to project:

cd Otithi-Sathi-AI

Then:

cd frontend

Install:

npm install

▶️ STEP 12 — START FRONTEND
npm run dev

Frontend:

http://localhost:5173


🔌 FRONTEND → BACKEND FLOW

React
  │
  │ HTTP
  ▼
FastAPI
  │
  ├── Authentication
  ├── Validation
  ├── AI
  ├── Tools
  ├── Services
  └── Database
  │
  ▼
Response
  │
  ▼
React



🧪 END-TO-END TEST FLOW

The most important test is the complete real-world flow.

┌─────────────────────────────────────────────┐
│             E2E AI TEST                     │
├─────────────────────────────────────────────┤
│                                             │
│  1. Open Frontend                           │
│             ↓                               │
│  2. Send Guest Message                     │
│             ↓                               │
│  3. React → FastAPI                         │
│             ↓                               │
│  4. FastAPI → Gemini                        │
│             ↓                               │
│  5. Gemini Selects Tool                     │
│             ↓                               │
│  6. Backend Executes Tool                   │
│             ↓                               │
│  7. Database / External API                 │
│             ↓                               │
│  8. Tool Result → Gemini                    │
│             ↓                               │
│  9. Gemini Generates Response               │
│             ↓                               │
│ 10. FastAPI → React                         │
│             ↓                               │
│ 11. Guest Sees Response                     │
│                                             │
└─────────────────────────────────────────────┘


☁️ DEPLOYMENT ARCHITECTURE

                    INTERNET
                        │
             ┌──────────┴──────────┐
             │                     │
             ▼                     ▼
       Frontend Host          Backend Host
             │                     │
             │                 FastAPI
             │                     │
             │                AI Provider
             │                     │
             │              ┌──────┴──────┐
             │              ▼             ▼
             │         PostgreSQL    External API
             │
             └──────────────┬─────────────
                            │
                            ▼
                          USERS



🧠 FUTURE AI ARCHITECTURE

The long-term architecture can evolve toward:


                    ATITHI SATHI AI
                           │
                           ▼
                    AI ORCHESTRATOR
                           │
          ┌────────────────┼────────────────┐
          │                │                │
          ▼                ▼                ▼
      Hotel Search      Availability     Guest Services
          │                │                │
          ▼                ▼                ▼
       Search API        Database       Hotel Systems
          │                │                │
          └────────────────┼────────────────┘
                           ▼
                    Unified AI Context
                           │
                           ▼
                    Guest Response


🌍 MULTILINGUAL VISION

Future versions can support multilingual guest conversations.

Example:

English
Hindi
Odia
Bengali
Tamil
Telugu
Kannada


🎙️ VOICE ASSISTANT VISION

Future architecture:

Guest Voice
    ↓
Speech-to-Text
    ↓
AI Understanding
    ↓
Tool Calling
    ↓
Hotel Data
    ↓
AI Response
    ↓
Text-to-Speech
    ↓
Guest Voice






