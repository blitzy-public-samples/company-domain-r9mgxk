from fastapi import APIRouter, Depends, HTTPException
from typing import List
from backend.app.schema.company import Company
from backend.app.services.web_scraper import WebScraper
from backend.app.services.data_processor import DataProcessor
from backend.app.db.database import get_db
from sqlalchemy.orm import Session

router = APIRouter()

@router.get('/')
def get_companies(db: Session = Depends(get_db)) -> List[Company]:
    companies = db.query(Company).all()
    return companies

@router.post('/')
def create_company(company: Company, db: Session = Depends(get_db)) -> Company:
    # HUMAN ASSISTANCE NEEDED
    # This function needs additional error handling and input validation
    # The confidence level is 0.7, indicating potential issues
    
    # Validate input data
    if not company.name or not company.website:
        raise HTTPException(status_code=400, detail="Company name and website are required")
    
    # Scrape company website
    web_scraper = WebScraper()
    scraped_data = web_scraper.scrape(company.website)
    
    # Process scraped data
    data_processor = DataProcessor()
    processed_data = data_processor.process(scraped_data)
    
    # Create company entry in database
    new_company = Company(**company.dict(), **processed_data)
    db.add(new_company)
    db.commit()
    db.refresh(new_company)
    
    return new_company