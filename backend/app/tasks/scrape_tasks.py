from celery import Celery
from backend.app.services.web_scraper import WebScraper
from backend.app.services.data_processor import DataProcessor
from backend.app.db.database import get_db
from backend.app.schema.company import Company

celery_app = Celery('scrape_tasks')

@celery_app.task
def scrape_company(domain: str) -> dict:
    # HUMAN ASSISTANCE NEEDED
    # This function needs review for production readiness and error handling
    
    # Initialize WebScraper
    scraper = WebScraper()
    
    # Scrape company website
    scraped_data = scraper.scrape_website(domain)
    
    # Process scraped data using DataProcessor
    processor = DataProcessor()
    processed_data = processor.process_company_data(scraped_data)
    
    # Create Company object
    company = Company(**processed_data)
    
    # Store Company object in database
    db = next(get_db())
    db.add(company)
    db.commit()
    db.refresh(company)
    
    # Return processed company data
    return processed_data