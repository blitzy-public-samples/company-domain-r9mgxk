import requests
from typing import Dict
from backend.app.core.config import settings

class OutreachIntegrator:
    def __init__(self, api_key: str, base_url: str):
        self.api_key = api_key
        self.base_url = base_url

    # HUMAN ASSISTANCE NEEDED
    # The following function has a confidence level of 0.7 and may need adjustments for production readiness
    def send_email(self, email_data: Dict[str, str]) -> bool:
        # Prepare email data for outreach software format
        formatted_data = {
            "recipient": email_data.get("to"),
            "subject": email_data.get("subject"),
            "body": email_data.get("body"),
            # Add more fields as required by the outreach software
        }

        # Send API request to outreach software
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        try:
            response = requests.post(f"{self.base_url}/send_email", json=formatted_data, headers=headers)
            response.raise_for_status()
        except requests.RequestException as e:
            # Log the error
            print(f"Error sending email: {str(e)}")
            return False

        # Handle response and check for success
        if response.status_code == 200:
            return True
        else:
            # Log the error
            print(f"Failed to send email. Status code: {response.status_code}")
            return False