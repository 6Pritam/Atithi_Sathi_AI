# 🏨 Otithi Sathi AI

> **An AI-powered hotel guest companion that helps guests discover hotel information, search hotels, check availability, and interact naturally with hotel services through an intelligent conversational assistant.**

![AI Assistant](https://img.shields.io/badge/AI-Guest%20Assistant-7C3AED?style=for-the-badge)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![React](https://img.shields.io/badge/React-Frontend-61DAFB?style=for-the-badge&logo=react&logoColor=black)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-336791?style=for-the-badge&logo=postgresql&logoColor=white)
![AI Tool Calling](https://img.shields.io/badge/AI-Tool%20Calling-FF6B35?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Active-22C55E?style=for-the-badge)

---

## 📌 Overview

**Otithi Sathi AI** is a full-stack AI-powered hotel guest assistant designed to provide guests with a natural, conversational way to discover hotel information and interact with hotel-related services.

Instead of requiring guests to navigate through multiple pages, menus, FAQs, or hotel information documents, Otithi Sathi AI allows them to simply ask questions in natural language.

For example:

```text
"What amenities does the hotel have?"

"Does the hotel have a swimming pool?"

"What is the check-in time?"

"Do you have Wi-Fi?"

"Find me a hotel in Indiranagar."

"I need a room for 2 guests from October 10 to October 12."

"Is there availability for those dates?"


✨ Key Features

🤖 AI Hotel Guest Assistant

Otithi Sathi AI provides a conversational interface where guests can ask questions naturally instead of navigating traditional hotel menus.


🏨 Hotel Information

Guests can ask about different aspects of a hotel or property.

Supported information can include:

Property information
Hotel description
Room information
Amenities
Services
Hotel policies
Check-in information
Check-out information
Frequently asked questions
Guest-related information


🛏️ Room Information

Guests can ask questions about available room types and room-related information.



🧳 Hotel Amenities

Guests can ask about available hotel amenities and services.


📋 Hotel Policies

Guests can ask about hotel policies without manually searching through documents.



❓ Hotel FAQ

Otithi Sathi AI can answer frequently asked hotel-related questions through the conversational interface.

Instead of browsing through a static FAQ page:

Guest:
"Can I get Wi-Fi in my room?"

        ↓

Otithi Sathi AI

        ↓

Relevant hotel information

        ↓

Natural-language response


🔎 Hotel Search

Otithi Sathi AI can understand natural-language hotel search requests.


🔧 AI Tool Calling

One of the core architectural features of Otithi Sathi AI is AI-driven tool calling.

The AI does not directly access the database.

Instead:
Guest Request
      ↓
FastAPI Backend
      ↓
AI Provider
      ↓
Intent / Tool Detection
      ↓
Backend Tool
      ↓
Database / External Service
      ↓
Tool Result
      ↓
AI Provider
      ↓
Natural Language Response
      ↓
Guest

🧠 AI Orchestration

The AI orchestration layer determines what should happen after receiving a guest request.


🛠️ Backend Tools

Otithi Sathi AI uses backend tools to perform deterministic operations.

Examples include:

🏨 Hotel Information Tool

Retrieves hotel/property information.

🛏️ Room Information Tool

Retrieves room-related information.

🏊 Amenity Information Tool

Retrieves available amenities and services.

📋 Policy / FAQ Tool

Retrieves hotel policies and frequently asked questions.

🔎 Hotel Search Tool

Searches available hotel information based on user requirements.

📅 Availability Tool

Checks hotel/room availability using the provided requirements.

The exact available tools are determined by the current backend implementation.


🗄️ Data Architecture

Otithi Sathi AI can use a combination of internal and external data sources.

                  ┌────────────────────┐
                  │    Guest Request   │
                  └─────────┬──────────┘
                            ↓
                  ┌────────────────────┐
                  │    AI Assistant    │
                  └─────────┬──────────┘
                            ↓
                    ┌───────┴───────┐
                    ↓               ↓
             Internal Data     External Data
                    ↓               ↓
             PostgreSQL        External API
                    │               │
                    └───────┬───────┘
                            ↓
                     Tool Response
                            ↓
                      AI Assistant
                            ↓
                    Guest Response



🌐 External Hotel Data

Where required, Otithi Sathi AI can use external hotel data services to supplement internal information.

The architecture supports external hotel search through services such as SerpApi, allowing the system to retrieve current search information when appropriate.

This creates a hybrid data strategy:

Internal Hotel Knowledge
          +
External Hotel Search
          ↓
     AI Orchestration
          ↓
    Unified Response



💬 Conversational Context

Otithi Sathi AI is designed to understand follow-up questions within the conversation.



🧠 Context-Aware Interaction

The assistant can use information from previous turns when processing follow-up requests.



🛡️ Validation

User requests are validated before backend operations are executed.

Validation can include:

Location validation
Date validation
Guest count validation
Required parameter validation
Tool argument validation
API input validation

Example:

Invalid Request
      ↓
Validation
      ↓
Missing Information
      ↓
Ask User for Required Information



🔄 Fallback Handling

The system is designed to handle situations where a preferred data source or service cannot provide a usable result.

For example:

Hotel Information Request
          ↓
Internal Database
          ↓
Data Available?
      ↙        ↘
    YES         NO
     ↓           ↓
Response    External Search
                 ↓
              Results
                 ↓
             Response



🎨 User Experience

The frontend provides a conversational AI experience focused on simplicity.

The primary interaction model is:

┌──────────────────────────────────────────┐
│            Otithi Sathi AI               │
│                                          │
│  AI Hotel Guest Companion                │
│                                          │
│  ┌────────────────────────────────────┐  │
│  │ Ask about hotels, rooms, amenities │  │
│  │ policies or availability...        │  │
│  └────────────────────────────────────┘  │
│                                          │
│  User: Does the hotel have a gym?        │
│                                          │
│  AI: Yes, the hotel has a fitness        │
│      center available for guests.       │
│                                          │
└──────────────────────────────────────────┘

🏗️ System Architecture

<img width="1852" height="411" alt="mermaid-diagram" src="https://github.com/user-attachments/assets/cf21c903-70dc-416c-aa9b-c75d3eec66a4" />

🔄 Complete Request Flow

<img width="3012" height="2398" alt="mermaid-diagram (1)" src="https://github.com/user-attachments/assets/6208540e-aeb3-41d4-8356-fc6b1d077f31" />


🧩 Core Architecture Principles

Otithi Sathi AI follows several architectural principles.

1. AI Does Not Directly Access the Database

The AI model requests a backend tool.

The backend executes the operation.

This provides better control over:

Security
Validation
Business rules
Database access
Error handling
2. AI and Business Logic Are Separated
AI Layer
   ↓
Tool Layer
   ↓
Business Logic
   ↓
Database / External Services

This keeps application logic independent from the AI provider.

3. Provider Abstraction

The AI provider should remain isolated behind the application's AI orchestration/provider layer.

This makes it easier to:

Change AI providers
Add additional providers
Test AI workflows
Centralize error handling
Maintain consistent application behavior


🛠️ Technology Stack


Layer	Technology
Frontend	React
Backend	FastAPI
Language	Python
Database	PostgreSQL
AI	LLM-based conversational AI
AI Orchestration	Provider / orchestration layer
Tool Calling	Backend function/tool calling
Hotel Search	Internal database + external search where required
External Search	SerpApi
API	REST
Version Control	Git / GitHub

Update this table if the implementation uses additional technologies.



📁 Project Structure

The project follows a frontend/backend architecture.

Otithi-Sathi-AI/
│
├── backend/
│   ├── app/
│   │   ├── ai/
│   │   ├── api/
│   │   ├── models/
│   │   ├── schemas/
│   │   ├── services/
│   │   ├── tools/
│   │   └── main.py
│   │
│   ├── tests/
│   ├── requirements.txt
│   └── .env.example
│
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── services/
│   │   └── ...
│   │
│   ├── package.json
│   └── ...
│
├── README.md
└── .gitignore



⚙️ Installation
Prerequisites

Install:

Python 3.11+
Node.js 18+
npm
PostgreSQL
Git


🗄️ Database Setup

Configure PostgreSQL and provide the database connection through the environment configuration.

Example:

DATABASE_URL=postgresql://USER:PASSWORD@HOST:PORT/DATABASE

Run database migrations if the project uses Alembic:

alembic upgrade head


🚀 Start Backend

From the backend directory:

uvicorn app.main:app --reload

The backend will normally be available at:

http://localhost:8000

FastAPI documentation:

http://localhost:8000/docs

ReDoc:

http://localhost:8000/redoc


⚛️ Frontend Setup

Open another terminal.

Navigate to:

cd frontend

Install dependencies:

npm install

Start development server:

npm run dev

The frontend will normally be available at:

http://localhost:5173


🔌 API Architecture

The frontend communicates with the FastAPI backend through HTTP APIs.

React
  ↓
HTTP Request
  ↓
FastAPI
  ↓
Service Layer
  ↓
AI / Tools / Database
  ↓
Response
  ↓
React

The backend is responsible for:

Request validation
AI orchestration
Tool execution
Database operations
External API calls
Error handling
Response formatting


🧪 Testing

The project should test the major AI and application workflows.

Important evaluation scenarios include:

Scenario 1 — Hotel Information
"What amenities does the hotel have?"
Scenario 2 — Room Information
"Tell me about the available rooms."
Scenario 3 — Hotel Policy
"What time is check-in?"
Scenario 4 — Hotel Search
"Find me a hotel in Indiranagar."
Scenario 5 — Availability
"Find a hotel for two guests from October 10 to October 12."
Scenario 6 — Follow-up Context
User:
"Find hotels in Indiranagar."

User:
"Which one has a swimming pool?"
Scenario 7 — Missing Information
"I need a hotel."

The assistant should request the information required to perform the search.

Scenario 8 — Invalid Input

Test invalid:

Dates
Guest counts
Locations
Tool parameters
Scenario 9 — External Data Failure

Test behavior when the external hotel data service is unavailable.

Scenario 10 — AI Provider Failure

Test behavior when the AI provider returns an error.

📊 Evaluation

Otithi Sathi AI should be evaluated across several dimensions:

Category	Evaluation
Intent Detection	Can the AI understand the guest request?
Tool Selection	Does it select the correct backend tool?
Parameter Extraction	Are location/date/guest values extracted correctly?
Tool Execution	Does the backend execute correctly?
Data Accuracy	Is the returned hotel information accurate?
Context Handling	Does the assistant understand follow-ups?
Validation	Are invalid inputs handled correctly?
Error Handling	Are failures handled safely?
Response Quality	Is the final response clear and useful?
Latency	Is the interaction reasonably fast?


🔐 Security Architecture


Security is an important part of the platform.

The application should ensure:

Frontend
   ↓
Public API
   ↓
Backend Validation
   ↓
Authorized Service
   ↓
Database / External API

AI and external API credentials remain on the backend.

The frontend should never directly receive or expose private API credentials.


📈 Scalability

The architecture separates the major application responsibilities:

Frontend
   ↓
API Layer
   ↓
AI Orchestration
   ↓
Tool Layer
   ↓
Services
   ↓
Database / External APIs

This separation makes it easier to scale individual components independently.

Future scaling opportunities include:

Caching
Database optimization
Async processing
Rate limiting
Background tasks
Observability
Horizontal backend scaling
External API caching
AI response optimization


🧠 Why Tool Calling?

Traditional chatbot:

User
 ↓
LLM
 ↓
Text Response

Otithi Sathi AI:

User
 ↓
LLM
 ↓
Determine Required Action
 ↓
Backend Tool
 ↓
Real Data
 ↓
LLM
 ↓
Final Response

This allows the assistant to move beyond static responses and interact with application data and services.


🏨 Product Architecture


Otithi Sathi AI can be viewed as three major layers:

1. Experience Layer
React
Chat Interface
Conversation UI
Loading States
Error States
2. Intelligence Layer
AI Model
Intent Understanding
Tool Selection
Context Handling
Response Generation
3. Action Layer
Hotel Tools
Database
Hotel Search
Availability
External APIs
Validation
Business Logic

Together:

┌─────────────────────────────┐
│       Guest Experience     │
│           React            │
└──────────────┬──────────────┘
               ↓
┌─────────────────────────────┐
│       AI Intelligence       │
│  LLM + Orchestration +      │
│       Tool Calling          │
└──────────────┬──────────────┘
               ↓
┌─────────────────────────────┐
│        Action Layer         │
│ Database + Hotel Tools +    │
│ External Search + APIs      │
└─────────────────────────────┘


🗺️ Roadmap

Future improvements can include:

🏨 Advanced hotel booking workflow
📅 Real-time room availability
💳 Payment integration
🧾 Booking confirmation
📱 Mobile application
🎙️ Voice-based guest assistant
🌐 Multilingual hotel assistance
🧠 Improved conversational memory
🔎 Advanced hotel recommendations
📊 Hotel analytics dashboard
🔔 Notifications
🧑‍💼 Hotel staff dashboard
🔗 Additional hotel data providers
⚡ Response latency optimization
📈 Production monitoring and observability

These items represent potential future enhancements and should not be interpreted as currently implemented functionality unless supported by the codebase.


🔄 Development Workflow

Recommended development workflow:

1. Start PostgreSQL
        ↓
2. Start FastAPI backend
        ↓
3. Start React frontend
        ↓
4. Open Otithi Sathi AI
        ↓
5. Send guest request
        ↓
6. AI determines intent
        ↓
7. Backend tool executes
        ↓
8. Database / external API responds
        ↓
9. AI generates final answer
        ↓
10. Guest receives response


📌 Current Architecture Summary



                    OTITHI SATHI AI
                          │
                          ▼
                  ┌───────────────┐
                  │ React Frontend│
                  └───────┬───────┘
                          │
                          ▼
                  ┌───────────────┐
                  │ FastAPI API   │
                  └───────┬───────┘
                          │
                          ▼
                ┌───────────────────┐
                │ AI Orchestration  │
                └─────────┬─────────┘
                          │
                          ▼
                    ┌───────────┐
                    │    LLM    │
                    └─────┬─────┘
                          │
                    Tool Calling
                          │
             ┌────────────┴────────────┐
             ▼                         ▼
      ┌─────────────┐          ┌──────────────┐
      │ PostgreSQL  │          │ External API │
      └─────────────┘          └──────────────┘
             │                         │
             └────────────┬────────────┘
                          ▼
                    Tool Results
                          │
                          ▼
                         LLM
                          │
                          ▼
                   Final Response
                          │
                          ▼
                    React Frontend
                          │
                          ▼
                        Guest



🎯 Project Goals

Otithi Sathi AI is designed around a simple principle:

Make hotel information and hotel discovery as easy as having a conversation.

Instead of forcing guests to search through:

Menus
   ↓
Pages
   ↓
FAQs
   ↓
Filters
   ↓
Search Results

the platform provides:

Guest Question
      ↓
Natural Conversation
      ↓
AI Understanding
      ↓
Real Data / Tools
      ↓
Useful Answer








