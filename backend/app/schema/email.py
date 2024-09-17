from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class Email(BaseModel):
    id: str
    subject: str
    body: str
    generated_at: datetime
    status: str
    lead_id: str
    campaign_id: str
    metadata: Optional[dict] = None