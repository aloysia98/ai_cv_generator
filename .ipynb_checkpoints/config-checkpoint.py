import os
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

TEMPLATE_PATH = os.path.join(BASE_DIR, "templates", "cv_template.tex")
BASE_CV_PATH = os.path.join(BASE_DIR, "base_data", "base_cv.json")
OUTPUT_DIR = os.path.join(BASE_DIR, "output")
LOG_DIR = os.path.join(BASE_DIR, "logs")

MODEL_NAME = "gemini-1.5-flash"

