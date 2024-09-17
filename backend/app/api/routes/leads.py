from fastapi import APIRouter, Depends, HTTPException
from typing import List
from backend.app.schema.lead import Lead
from backend.app.services.ai_analyzer import AIAnalyzer
from backend.app.services.crm_integrator import CRMIntegrator
from backend.app.db.database import get_db
from sqlalchemy.orm import Session

router = APIRouter()

@router.get('/')
def get_leads(db: Session = Depends(get_db)) -> List[Lead]:
    # Query database for leads
    leads = db.query(Lead).all()
    return leads

@router.post('/')
def create_lead(lead: Lead, db: Session = Depends(get_db)) -> Lead:
    # HUMAN ASSISTANCE NEEDED
    # This function has a confidence level of 0.7 and may need additional review or modifications for production readiness.
    # The following implementation attempts to cover all steps, but may require refinement.

    # Validate input data
    if not lead.email or not lead.name:
        raise HTTPException(status_code=400, detail="Email and name are required fields")

    # Analyze lead using AI
    ai_analyzer = AIAnalyzer()
    lead_score = ai_analyzer.analyze_lead(lead)
    lead.ai_score = lead_score

    # Check CRM for existing lead
    crm_integrator = CRMIntegrator()
    existing_lead = crm_integrator.find_lead(lead.email)
    if existing_lead:
        raise HTTPException(status_code=409, detail="Lead already exists in CRM")

    # Create lead entry in database
    db_lead = Lead(**lead.dict())
    db.add(db_lead)
    db.commit()
    db.refresh(db_lead)

    # Sync lead with CRM
    crm_integrator.sync_lead(db_lead)

    return db_lead