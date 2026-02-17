from backend.latex.sanitizer import escape_latex
from backend.config import TEMPLATE_PATH#
from typing import Dict


def render_template(cv_data):
    with open(TEMPLATE_PATH, "r") as f:
        template = f.read()

    role = escape_latex(cv_data.headline_role)
    summary = escape_latex(cv_data.summary)

    # Skills (grouped by category)
    skills_sections = []

    for category, skills_list in cv_data.skills.items():
        escaped_category = escape_latex(category)

        items = "\n".join(
            [f"\\item {escape_latex(skill)}" for skill in skills_list]
        )

        section = f"""
\\textbf{{{escaped_category}}}
\\begin{{itemize}}
{items}
\\end{{itemize}}
"""
        skills_sections.append(section)

    skills_latex = "\n".join(skills_sections)

    experience_sections = []

    for job in cv_data.work_experience:
        responsibilities = "\n".join(
            [f"\\item {escape_latex(r)}" for r in job.responsibilities]
        )

        section = f"""
\\textbf{{{escape_latex(job.job_title)}}} — {escape_latex(job.organization)} \\\\
{escape_latex(job.location)} \\\\
{escape_latex(job.start_date)} -- {escape_latex(job.end_date)}
\\begin{{itemize}}
{responsibilities}
\\end{{itemize}}
"""
        experience_sections.append(section)

    experience_latex = "\n".join(experience_sections)

    template = template.replace("{{ROLE}}", role)
    template = template.replace("{{SUMMARY}}", summary)
    template = template.replace("{{SKILLS}}", skills_latex)
    template = template.replace("{{EXPERIENCE}}", experience_latex)

    return template
