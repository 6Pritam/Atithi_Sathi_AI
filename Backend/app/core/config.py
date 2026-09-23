import os
from dotenv import load_dotenv
from pathlib import Path

env_path = Path(__file__).resolve().parent.parent.parent / ".env"
load_dotenv(dotenv_path=env_path)

GROK_API_KEY = os.getenv("XAI_API_KEY") or os.getenv("GROK_API_KEY")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
SERPAPI_API_KEY = os.getenv("SERPAPI_API_KEY")
AI_PROVIDER = os.getenv("AI_PROVIDER", "gemini").lower()
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./atithi_saathi.db")
FRONTEND_URL = os.getenv("FRONTEND_URL", "http://localhost:5173")
