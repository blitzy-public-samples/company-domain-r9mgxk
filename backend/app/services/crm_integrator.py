import requests
from typing import Dict
from backend.app.core.config import settings

class CRMIntegrator:
    def __init__(self, api_key: str, base_url: str):
        self.api_key = api_key
        self.base_url = base_url

    # HUMAN ASSISTANCE NEEDED
    # The sync_lead function needs more details on the specific CRM system's API structure and error handling.
    # Additional error handling and logging should be implemented for production readiness.
    def sync_lead(self, lead_data: Dict[str, str]) -> bool:
        # Prepare lead data for CRM format
        crm_formatted_data = self._format_lead_data(lead_data)

        # Send API request to CRM system
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        response = requests.post(f"{self.base_url}/leads", json=crm_formatted_data, headers=headers)

        # Handle response and check for success
        if response.status_code == 200:
            return True
        else:
            # Log error details here
            return False

    def _format_lead_data(self, lead_data: Dict[str, str]) -> Dict[str, str]:
        # This method should be implemented based on the specific CRM system's requirements
        # For now, we'll just return the original data
        return lead_data