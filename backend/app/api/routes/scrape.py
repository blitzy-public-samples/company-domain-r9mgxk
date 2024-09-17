from fastapi import APIRouter, Depends, HTTPException
from backend.app.services.web_scraper import WebScraper
from backend.app.services.data_processor import DataProcessor
from backend.app.db.database import get_db
from sqlalchemy.orm import Session

router = APIRouter()

# HUMAN ASSISTANCE NEEDED
# The following function has a confidence level of 0.6, which is below the threshold of 0.8.
# Additional review and modifications may be required to ensure production readiness.

@router.post('/scrape')
async def scrape_company(domain: str, db: Session = Depends(get_db)):
    # Validate input domain
    if not domain or not isinstance(domain, str):
        raise HTTPException(status_code=400, detail="Invalid domain provided")

    try:
        # Initialize web scraper
        scraper = WebScraper()

        # Scrape company website
        scraped_data = await scraper.scrape_website(domain)

        # Process scraped data
        processor = DataProcessor(db)
        processed_data = await processor.process_company_data(scraped_data)

        # Return processed company data
        return processed_data

    except Exception as e:
        # Handle exceptions and provide appropriate error responses
        raise HTTPException(status_code=500, detail=f"An error occurred during scraping: {str(e)}")

# Additional error handling, input validation, and security measures may be needed
# Proper logging and monitoring should be implemented for production use
# Consider adding rate limiting and authentication for the API endpoint