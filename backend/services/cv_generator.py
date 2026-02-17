import json
from datetime import datetime

from backend.config import BASE_CV_PATH
from backend.llm.prompts import build_prompt
from backend.llm.hf_client import call_llm
from backend.parser.response_parser import parse_llm_response
from backend.latex.template_engine import render_template
from backend.latex.compiler import compile_latex


def load_base_cv():
    with open(BASE_CV_PATH, "r") as f:
        return json.load(f)


def generate_cv(job_description: str) -> str:
    base_cv = load_base_cv()

    prompt = build_prompt(job_description, base_cv)

    raw_response = call_llm(prompt)

    parsed_data = parse_llm_response(raw_response)

    tex_content = render_template(parsed_data)

    safe_role = parsed_data.headline_role.replace(" ", "_")
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"CV_{safe_role}_{timestamp}"

    pdf_path = compile_latex(tex_content, filename)

    return pdf_path
