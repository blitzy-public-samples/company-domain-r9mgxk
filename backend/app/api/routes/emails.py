from fastapi import APIRouter, Depends, HTTPException
from typing import List
from backend.app.schema.email import Email
from backend.app.services.email_generator import EmailGenerator
from backend.app.services.outreach_integrator import OutreachIntegrator
from backend.app.db.database import get_db
from sqlalchemy.orm import Session

router = APIRouter()

@router.get('/')
async def get_emails(db: Session = Depends(get_db)) -> List[Email]:
    emails = db.query(Email).all()
    return emails

@router.post('/')
async def create_email(email: Email, db: Session = Depends(get_db)) -> Email:
    # HUMAN ASSISTANCE NEEDED
    # This function has a confidence level of 0.7 and may need review for production readiness.
    # The following implementation is a starting point and may need refinement.

    # Validate input data
    if not email.recipient or not email.subject:
        raise HTTPException(status_code=400, detail="Recipient and subject are required")

    # Generate personalized email content
    email_generator = EmailGenerator()
    email.content = email_generator.generate_content(email.recipient, email.subject)

    # Create email entry in database
    db_email = Email(**email.dict())
    db.add(db_email)
    db.commit()
    db.refresh(db_email)

    # Integrate with outreach software
    outreach_integrator = OutreachIntegrator()
    outreach_integrator.send_email(db_email)

    return db_email