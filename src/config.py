from pathlib import Path
import os

from dotenv import load_dotenv


BASE_DIR = Path(__file__).parent.parent
PATH_TO_RESOURCES = BASE_DIR / "src" / "resources"
PATH_TO_MESSAGES = BASE_DIR / "resources" / "messages"
PATH_TO_ENV = BASE_DIR / ".env"
PATH_TO_IMAGES = BASE_DIR / "resources" / "images"
PATH_TO_MENUS = BASE_DIR / "resources" / "menus"
PATH_TO_PROMPTS = BASE_DIR / "resources" / "prompts"

load_dotenv(PATH_TO_ENV)

OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]
TG_BOT_API_KEY = os.environ["TG_BOT_API_KEY"]

