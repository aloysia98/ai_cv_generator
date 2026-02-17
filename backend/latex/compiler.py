import subprocess
import os
from backend.config import OUTPUT_DIR


def compile_latex(tex_content: str, filename: str) -> str:
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    tex_path = os.path.join(OUTPUT_DIR, f"{filename}.tex")

    with open(tex_path, "w") as f:
        f.write(tex_content)

    result = subprocess.run(
        ["pdflatex", "-interaction=nonstopmode", "-output-directory", output_dir, tex_path],
        capture_output=True,
        text=True
    )

# Do NOT raise error even if LaTeX warnings exist


    return os.path.join(OUTPUT_DIR, f"{filename}.pdf")
