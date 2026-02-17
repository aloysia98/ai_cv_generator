import os

# Hugging Face Space working directory is always /app
BASE_DIR = os.getcwd()

TEMPLATE_PATH = os.path.join(BASE_DIR, "templates", "cv_template.tex")
BASE_CV_PATH = os.path.join(BASE_DIR, "base_data", "base_cv.json")
OUTPUT_DIR = os.path.join(BASE_DIR, "output")
LOG_DIR = os.path.join(BASE_DIR, "logs")

MODEL_NAME = "meta-llama/Meta-Llama-3-8B-Instruct"



