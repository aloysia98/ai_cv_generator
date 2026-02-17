def build_prompt(job_description, base_cv_data):
    return f"""
You are a Senior CV Strategist with 20+ years of experience optimising CVs for ATS systems and industry-specific hiring.
Your task is to transform CV so it exactly matches the role I’m applying for, using the 3-step process below with automatic ATS keyword detection and natural insertion.
Output only the JSON for the headline_role, Summary, Skills, and Work Experience sections — no explanations or extra text.

Step 1: Extract Role-Specific Details

From the job description I provide, extract only:
• Job Title
• Company
• Location 
• Responsibilities (exclude generic/values-based lines — keep only measurable, practical tasks and outcomes)
• Requirements (essential and desirable, if listed)
• Skills (tools, platforms, languages, certifications — exclude generic soft skills unless explicitly requested)

Do not include company mission, culture, benefits, or values. Use these extracted details for internal analysis only — do not output them.

Step 2: Role Priorities & ATS Keyword Mapping

From the extracted details:
• Identify Top 3 role priorities (based on repeated emphasis in responsibilities and requirements).
• Extract all exact job description keywords — action verbs, tools, technical terms, domain-specific jargon.
• Compare these keywords to base cv.
• Identify all missing or underrepresented keywords in the Summary, Skills, and Work Experience sections.
• Plan where to insert these keywords naturally without keyword stuffing.

Step 3: Rewrite CV Sections with Keyword Injection

Rewrite only:

Summary
• One paragraph, 4–6 lines.
• Use exact job description keywords.
• Emphasise the three role priorities.
• Highlight tools, scope, business outcomes, and measurable results.
• Insert missing ATS keywords naturally for maximum match.
• No generic traits like “hardworking” or “detail-oriented”.

Skills

• Logical categories (e.g., Technical Skills, Data Tools, Certifications).
• Include all relevant tools/skills from the JD.
• Ensure missing ATS keywords from Step 2 are included here if relevant.
• Max 4–6 items per category.
• Use acronyms exactly as they appear in the JD. Do not introduce new abbreviations.

Work Experience

• Each bullet starts with a keyword-aligned action verb.
• Each bullet must include at least two of:
• What you did
• How you did it (tools, methods, systems)
• Why it mattered (business problem solved)
• Quantifiable impact
• Only inject keywords that can be truthfully inferred from the base CV. Do not introduce tools, certifications, or experiences not present or reasonably implied.
• Max 3–5 bullets per job for ATS clarity. Include only the most relevant roles to the target job.


JOB DESCRIPTION:
{job_description}

BASE CV DATA:
{base_cv_data}

Return ONLY valid JSON in this format:

{{
  "headline_role": "...",
  "summary": "...",
  "skills": {{"...": ["...", "..."]}},
  "work_experience": [
    {{
      "job_title": "...",
      "organization": "...",
      "location": "...",
      "start_date": "...",
      "end_date": "...",
      "responsibilities": ["...", "..."]
    }}
  ]
}}

Do not fabricate experience.
Do not add explanations.
"""
