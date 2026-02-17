import subprocess
import os
from backend.config import OUTPUT_DIR


def compile_latex(tex_content: str, filename: str) -> str:
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    tex_path = os.path.join(OUTPUT_DIR, f"{filename}.tex")

    with open(tex_path, "w", encoding="utf-8") as f:
        f.write(tex_content)

    subprocess.run(
        [
            "pdflatex",
            "-interaction=nonstopmode",
            "-output-directory",
            OUTPUT_DIR,
            tex_path,
        ],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )

    return os.path.join(OUTPUT_DIR, f"{filename}.pdf")
