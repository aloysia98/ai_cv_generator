def build_prompt(job_description, base_cv_data):
    return f"""
You are a senior CV strategist specialising in ATS optimisation and keyword alignment.

Your task:
Rewrite the CV so it aligns precisely with the job description while remaining truthful to the base CV data.

OUTPUT REQUIREMENTS:
• Return ONLY valid JSON.
• No explanations.
• No markdown.
• No code fences.
• No extra text.
• If a value is unknown, return an empty string or empty list.
• Do not fabricate experience, tools, or certifications.

CONTENT OBJECTIVES:
1. Identify the 3 core role priorities from the job description.
2. Extract exact keywords (tools, systems, terminology, action verbs).
3. Insert missing but relevant keywords naturally.
4. Maintain professional, human tone.
5. Prioritise clarity and impact over length.

LENGTH CONTROL:
• Total word count (summary + skills + experience): 380–420 words.
• Absolute maximum: 430 words.
• Summary: 70–90 words.
• 3–5 bullets per role.
• At least half of the bullets should include measurable impact.
• When including metrics, integrate them naturally into the sentence.

WRITING RULES:
• Use strong action verbs aligned with the job description.
• Avoid: “responsible for”, “worked on”, “assisted with”.
• Avoid filler words such as “various”, “multiple”, “successfully”.
• Do not exaggerate seniority beyond the base CV.
• Avoid repetitive sentence openings across bullets.
• Do not compress ideas unnaturally for density.
• Every sentence must read like a complete professional thought.

SUMMARY RULES:
• Avoid generic openings such as “Results-driven” or “Experienced professional”.
• Begin with domain positioning, specialisation, or business impact.
• Blend tools into context rather than listing them.
• Avoid excessive commas.
• Focus on business outcomes, not responsibilities.
• Keep tone natural and mid-level professional.

SKILLS RULES:
• 3–4 categories maximum.
• Max 4 skills per category.
• Use exact acronyms from the job description.
• Do not repeat heavily emphasised tools from experience unless required for ATS.
• Remove overlapping or redundant skills.

WORK EXPERIENCE RULES:
• Bullets must be full professional sentences.
• Integrate metrics directly into the sentence — never use parentheses.
• Each bullet should include at least two of:
  - What was done
  - How it was done (tools/methods)
  - Why it mattered (business context)
  - Quantifiable impact
• Add light business context explaining why the work mattered.
• Avoid KPI-fragment style phrasing.
• Vary sentence structure across bullets.
• Ensure bullets sound human-written, not generated.
• Avoid identical structural patterns across roles.

FINAL NATURALNESS CHECK:
Before returning output, internally refine once to remove robotic phrasing or compressed KPI-style structure.

JOB DESCRIPTION:
{job_description}

BASE CV DATA:
{base_cv_data}

Return ONLY valid JSON in this exact structure:

{{
  "headline_role": "...",
  "summary": "...",
  "skills": {{
    "Category Name": ["Skill 1", "Skill 2", "Skill 3"]
  }},
  "work_experience": [
    {{
      "job_title": "...",
      "organization": "...",
      "location": "...",
      "start_date": "...",
      "end_date": "...",
      "responsibilities": ["Bullet 1", "Bullet 2", "Bullet 3"]
    }}
  ]
}}
"""


# def build_prompt(job_description, base_cv_data):
#     return f"""
# You are a Senior CV Strategist with 20+ years of experience optimising CVs for ATS systems and industry-specific hiring.
# Your task is to transform CV so it exactly matches the role I’m applying for, using the 3-step process below with automatic ATS keyword detection and natural insertion.
# Output only the JSON for the headline_role, Summary, Skills, and Work Experience sections — no explanations or extra text.

# ADDITIONAL OUTPUT CONSTRAINTS:

# • Target total word count (Summary + Skills + Work Experience combined): 380–420 words.
# • Absolute maximum: 430 words.
# • Prioritise density over length — remove redundant phrasing.
# • Avoid repeating similar impact statements across roles.
# • Avoid long multi-clause sentences.
# • Keep writing sharp, executive, and results-focused.
# • Every sentence must add new information.
# • Do not exceed 18–22 words per bullet point.


# Step 1: Extract Role-Specific Details

# From the job description I provide, extract only:
# • Job Title
# • Company
# • Location 
# • Responsibilities (exclude generic/values-based lines — keep only measurable, practical tasks and outcomes)
# • Requirements (essential and desirable, if listed)
# • Skills (tools, platforms, languages, certifications — exclude generic soft skills unless explicitly requested)

# Do not include company mission, culture, benefits, or values. Use these extracted details for internal analysis only — do not output them.

# Step 2: Role Priorities & ATS Keyword Mapping

# From the extracted details:
# • Identify Top 3 role priorities (based on repeated emphasis in responsibilities and requirements).
# • Extract all exact job description keywords — action verbs, tools, technical terms, domain-specific jargon.
# • Compare these keywords to base cv.
# • Identify all missing or underrepresented keywords in the Summary, Skills, and Work Experience sections.
# • Plan where to insert these keywords naturally without keyword stuffing.

# Density Optimisation Rules:

# • At least 60% of bullets must contain quantifiable impact (%, volume, frequency, scale, speed, revenue, risk reduction).
# • Avoid generic phrases such as:
#   - "responsible for"
#   - "worked on"
#   - "involved in"
#   - "assisted with"
# • Prefer strong action verbs aligned with the JD.
# • Remove filler words such as:
#   - "various"
#   - "multiple"
#   - "successfully"
#   - "effectively"
# • Avoid repeating the same keyword more than twice unless critical to ATS match.


# Step 3: Rewrite CV Sections with Keyword Injection

# Rewrite only:

# Summary
# • One paragraph, 4–6 lines.
# • Use exact job description keywords.
# • Emphasise the three role priorities.
# • Highlight tools, scope, business outcomes, and measurable results.
# • Insert missing ATS keywords naturally for maximum match.
# • No generic traits like “hardworking” or “detail-oriented”.

# Humanisation Rules for Summary:

# • Write in natural professional language, not robotic or keyword-stacked.
# • Blend keywords into flowing sentences.
# • Avoid listing tools in a row.
# • Avoid overly academic phrasing.
# • Avoid excessive commas.
# • Maximum 90 words.
# • Target 70–85 words for optimal density.
# • Focus on impact and business outcomes rather than responsibilities.
# • Avoid compressed KPI-style phrasing.
# • Ensure summary reads like a senior professional introduction, not a metrics list.



# Skills

# • Logical categories (e.g., Technical Skills, Data Tools, Certifications).
# • Include all relevant tools/skills from the JD.
# • Ensure missing ATS keywords from Step 2 are included here if relevant.
# • Max 4–6 items per category.
# • Use acronyms exactly as they appear in the JD. Do not introduce new abbreviations.

# Skills Density Rules:

# • Maximum 3–4 categories only.
# • Maximum 4 items per category.
# • Remove overlapping skills.
# • Do not repeat tools already emphasised heavily in Work Experience unless required for ATS.
# • Prioritise tools explicitly mentioned in the JD.


# Work Experience

# • Each bullet starts with a keyword-aligned action verb.
# • Each bullet must include at least two of:
# • What you did
# • How you did it (tools, methods, systems)
# • Why it mattered (business problem solved)
# • Quantifiable impact
# • Only inject keywords that can be truthfully inferred from the base CV. Do not introduce tools, certifications, or experiences not present or reasonably implied.
# • Max 3–5 bullets per job for ATS clarity. Include only the most relevant roles to the target job.

# Bullet Structure Enforcement:

# • Write bullets as full professional sentences.
# • Do not use parentheses for metrics.
# • Integrate metrics into the sentence naturally.
# • Include light business context (why it mattered).
# • Avoid KPI-fragment structure.
# • Ensure each bullet reads like it was written by a human analyst, not generated.
# • Avoid identical sentence structures across bullets.
# • Avoid slide-deck or CV-template phrasing.
# • Bullets must sound like mid-level professional experience.


# Flow & Tone Adjustment:

# • Write bullets as natural professional statements, not KPI fragments.
# • Do not use parentheses for impact metrics.
# • Integrate metrics into the sentence.
# • Ensure each bullet reads as one complete professional thought.
# • Vary sentence openings (avoid repeating same structure).
# • Prioritise clarity and readability over compression.


# Model Precision Constraint:

# • Do not expand sentences unnecessarily.
# • Do not add leadership framing unless explicitly present.
# • Avoid high-level strategy language unless stated in base CV.
# • Avoid repeating the same impact metric phrasing.
# • Keep tone mid-level professional unless JD demands seniority.

# JOB DESCRIPTION:
# {job_description}

# BASE CV DATA:
# {base_cv_data}

# Length Control Enforcement:

# Before returning output:
# • Recalculate total word count internally.
# • If above 420 words, remove lowest-impact bullet(s).
# • If still above 420, compress summary.
# • Maintain density score ≥ 8 (high quantification, low redundancy).
# • Never exceed 430 words.
# • If total word count falls below 360 words, expand Summary with stronger business context and expand most relevant role with one additional high-impact bullet.

# Return ONLY valid JSON in this format:

# {{
#   "headline_role": "...",
#   "summary": "...",
#   "skills": {{"...": ["...", "..."]}},
#   "work_experience": [
#     {{
#       "job_title": "...",
#       "organization": "...",
#       "location": "...",
#       "start_date": "...",
#       "end_date": "...",
#       "responsibilities": ["...", "..."]
#     }}
#   ]
# }}

# Do not fabricate experience.
# Do not add explanations.
# """
