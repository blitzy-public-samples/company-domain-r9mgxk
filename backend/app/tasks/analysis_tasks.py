from celery import Celery
from backend.app.services.ai_analyzer import AIAnalyzer
from backend.app.db.database import get_db
from backend.app.schema.lead import Lead

celery_app = Celery('analysis_tasks')

@celery_app.task
def analyze_lead(lead_id: str) -> dict:
    # HUMAN ASSISTANCE NEEDED
    # The following code needs review and potential modifications for production readiness
    # Confidence level: 0.6
    
    # Retrieve lead data from database
    db = next(get_db())
    lead = db.query(Lead).filter(Lead.id == lead_id).first()
    
    if not lead:
        raise ValueError(f"Lead with id {lead_id} not found")
    
    # Initialize AIAnalyzer
    analyzer = AIAnalyzer()
    
    # Perform AI analysis on lead data
    analysis_results = analyzer.analyze(lead.to_dict())
    
    # Update lead with analysis results
    lead.analysis_results = analysis_results
    
    # Store updated lead in database
    db.commit()
    
    # Return analysis results
    return analysis_results