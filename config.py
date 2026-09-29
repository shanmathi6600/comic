import os
from pathlib import Path
from dotenv import load_dotenv

# Base project paths
BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / ".env")

APP_DIR = BASE_DIR / "app"
TEMPLATES_DIR = APP_DIR / "templates"
STATIC_DIR = APP_DIR / "static"
PANELS_DIR = STATIC_DIR / "panels"
EXPORTS_DIR = STATIC_DIR / "exports"

# Ensure runtime directories exist
STATIC_DIR.mkdir(parents=True, exist_ok=True)
PANELS_DIR.mkdir(parents=True, exist_ok=True)
EXPORTS_DIR.mkdir(parents=True, exist_ok=True)

# --------------------------------------------------
# API KEYS
# --------------------------------------------------
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "").strip()
HF_API_KEY = os.getenv("HF_API_KEY", "").strip()

# --------------------------------------------------
# GEMINI MODELS
# --------------------------------------------------
GEMINI_FLASH_MODEL = os.getenv("GEMINI_FLASH_MODEL", "gemini-3.5-flash-lite").strip()
GEMINI_PRO_MODEL = os.getenv("GEMINI_PRO_MODEL", "gemini-3.5-flash-lite").strip()

# --------------------------------------------------
# IMAGE MODEL & SETTINGS
# --------------------------------------------------
IMAGE_MODEL = os.getenv("IMAGE_MODEL", "stable-diffusion-v1-5/stable-diffusion-v1-5").strip()
IMAGE_PROVIDER = os.getenv("IMAGE_PROVIDER", "auto").lower().strip()
IMAGE_STEPS = int(os.getenv("IMAGE_STEPS", "20"))
IMAGE_WIDTH = int(os.getenv("IMAGE_WIDTH", "512"))
IMAGE_HEIGHT = int(os.getenv("IMAGE_HEIGHT", "512"))

MAX_PROMPT_LENGTH = 1000