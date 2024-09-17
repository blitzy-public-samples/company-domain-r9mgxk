from celery import Celery
from backend.app.services.email_generator import EmailGenerator
from backend.app.services.outreach_integrator import OutreachIntegrator
from backend.app.db.database import get_db
from backend.app.schema.email import Email
from backend.app.schema.lead import Lead

celery_app = Celery('email_tasks')

@celery_app.task
def generate_and_send_email(lead_id: str, campaign_id: str) -> dict:
    # HUMAN ASSISTANCE NEEDED
    # The following code needs review and potential modifications for production readiness.
    # Specific areas that may need attention:
    # - Error handling and logging
    # - Database transaction management
    # - Retry logic for external service calls
    # - Performance optimization for database queries

    db = get_db()
    
    # Retrieve lead data from database
    lead = db.query(Lead).filter(Lead.id == lead_id).first()
    if not lead:
        return {"status": "error", "message": "Lead not found"}

    # Initialize EmailGenerator
    email_generator = EmailGenerator()

    # Generate personalized email content
    email_content = email_generator.generate_email(lead, campaign_id)

    # Create Email object
    email = Email(
        lead_id=lead_id,
        campaign_id=campaign_id,
        content=email_content,
        status="pending"
    )

    # Store Email object in database
    db.add(email)
    db.commit()

    # Initialize OutreachIntegrator
    outreach_integrator = OutreachIntegrator()

    # Send email using outreach software
    send_result = outreach_integrator.send_email(email)

    # Update Email status in database
    email.status = "sent" if send_result["success"] else "failed"
    db.commit()

    # Return email sending status
    return {
        "status": "success" if send_result["success"] else "error",
        "message": send_result.get("message", ""),
        "email_id": str(email.id)
    }