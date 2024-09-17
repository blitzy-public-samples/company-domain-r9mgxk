from fastapi import APIRouter, Depends, HTTPException
from typing import List
from backend.app.schema.campaign import Campaign
from backend.app.services.email_generator import EmailGenerator
from backend.app.db.database import get_db
from sqlalchemy.orm import Session

router = APIRouter()

@router.get('/')
def get_campaigns(db: Session = Depends(get_db)) -> List[Campaign]:
    # Query database for campaigns
    campaigns = db.query(Campaign).all()
    return campaigns

@router.post('/')
def create_campaign(campaign: Campaign, db: Session = Depends(get_db)) -> Campaign:
    # Validate input data
    if not campaign.name or not campaign.description:
        raise HTTPException(status_code=400, detail="Campaign name and description are required")

    # Create campaign entry in database
    db_campaign = Campaign(**campaign.dict())
    db.add(db_campaign)
    db.commit()
    db.refresh(db_campaign)

    # Generate email templates for campaign
    email_generator = EmailGenerator()
    email_generator.generate_templates(db_campaign)

    return db_campaign

# HUMAN ASSISTANCE NEEDED
# The following aspects might need human review:
# 1. Error handling: Add more specific error handling for database operations.
# 2. Input validation: Implement more comprehensive input validation for the create_campaign function.
# 3. Authentication and authorization: Add proper authentication and authorization checks.
# 4. Pagination: Implement pagination for the get_campaigns function to handle large datasets.
# 5. Logging: Add logging for important operations and errors.