import requests
from bs4 import BeautifulSoup
from typing import List, Dict
from backend.app.core.config import settings

class WebScraper:
    def __init__(self, headers: Dict[str, str] = None):
        self.session = requests.Session()
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        if headers:
            self.headers.update(headers)
        self.session.headers.update(self.headers)

    def scrape_company_info(self, domain: str) -> Dict[str, str]:
        # HUMAN ASSISTANCE NEEDED
        # This function needs more robust error handling and data validation.
        # The exact structure of company websites may vary, so the scraping logic
        # might need to be adjusted based on specific website structures.
        url = f"https://{domain}"
        response = self.session.get(url)
        response.raise_for_status()

        soup = BeautifulSoup(response.content, 'html.parser')

        company_info = {}
        
        # Attempt to extract company name
        company_name = soup.find('meta', property='og:site_name')
        if company_name:
            company_info['name'] = company_name['content']
        else:
            company_info['name'] = soup.title.string if soup.title else ''

        # Attempt to extract company description
        description = soup.find('meta', attrs={'name': 'description'})
        if description:
            company_info['description'] = description['content']
        else:
            company_info['description'] = ''

        # Additional scraping logic can be added here based on common website structures

        return company_info