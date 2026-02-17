import json
from pydantic import BaseModel
from typing import Dict, List, Optional

class ExperienceItem(BaseModel):
    job_title: str
    organization: str
    location: str
    start_date: str
    end_date: str
    responsibilities: List[str]#

class CVOutput(BaseModel):
    headline_role: str
    summary: str
    skills: Dict[str, List[str]]
    work_experience: List[ExperienceItem]

def parse_llm_response(raw_text: str) -> CVOutput:
    data = json.loads(raw_text)
    return CVOutput(**data)
