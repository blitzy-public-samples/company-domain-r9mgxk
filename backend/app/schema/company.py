from pydantic import BaseModel
from typing import Optional, List

class Company(BaseModel):
    id: str
    domain: str
    name: str
    description: Optional[str] = None
    industry: Optional[str] = None
    employee_count: Optional[int] = None
    technologies: Optional[List[str]] = None
    metadata: Optional[dict] = None