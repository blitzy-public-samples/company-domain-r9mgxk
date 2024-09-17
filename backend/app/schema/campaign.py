from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class Campaign(BaseModel):
    id: str
    name: str
    start_date: datetime
    end_date: datetime
    email_ids: List[str]
    metadata: Optional[dict] = None