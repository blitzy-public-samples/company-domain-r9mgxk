from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class Lead(BaseModel):
    id: str
    company_id: str
    status: str
    created_at: datetime
    updated_at: datetime
    ceo_name: Optional[str] = None
    ceo_linkedin_url: Optional[str] = None
    ceo_email: Optional[str] = None
    ceo_phone: Optional[str] = None
    metadata: Optional[dict] = None