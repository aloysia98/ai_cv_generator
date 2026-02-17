import os

# Root of the project (/app inside Hugging Face Space)
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

# Paths
TEMPLATE_PATH = os.path.join(BASE_DIR, "templates", "cv_template.tex")
BASE_CV_PATH = os.path.join(BASE_DIR, "base_data", "base_cv.json")
OUTPUT_DIR = os.path.join(BASE_DIR, "output")
LOG_DIR = os.path.join(BASE_DIR, "logs")

# Hugging Face model
MODEL_NAME = "meta-llama/Meta-Llama-3-8B-Instruct"


