import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.models import Company, Lead, Campaign, Email
from app.database import get_db
from sqlalchemy.orm import Session

client = TestClient(app)

@pytest.fixture
def db_session(monkeypatch):
    def mock_get_db():
        return Session()
    monkeypatch.setattr("app.database.get_db", mock_get_db)

# Test cases for company-related API endpoints
def test_create_company(db_session):
    response = client.post("/companies/", json={"name": "Test Company", "website": "https://testcompany.com"})
    assert response.status_code == 201
    assert response.json()["name"] == "Test Company"

def test_get_company(db_session):
    company_id = 1
    response = client.get(f"/companies/{company_id}")
    assert response.status_code == 200
    assert response.json()["id"] == company_id

def test_update_company(db_session):
    company_id = 1
    response = client.put(f"/companies/{company_id}", json={"name": "Updated Company", "website": "https://updatedcompany.com"})
    assert response.status_code == 200
    assert response.json()["name"] == "Updated Company"

def test_delete_company(db_session):
    company_id = 1
    response = client.delete(f"/companies/{company_id}")
    assert response.status_code == 204

# Test cases for lead-related API endpoints
def test_create_lead(db_session):
    response = client.post("/leads/", json={"name": "John Doe", "email": "john@example.com", "company_id": 1})
    assert response.status_code == 201
    assert response.json()["name"] == "John Doe"

def test_get_lead(db_session):
    lead_id = 1
    response = client.get(f"/leads/{lead_id}")
    assert response.status_code == 200
    assert response.json()["id"] == lead_id

def test_update_lead(db_session):
    lead_id = 1
    response = client.put(f"/leads/{lead_id}", json={"name": "Jane Doe", "email": "jane@example.com", "company_id": 1})
    assert response.status_code == 200
    assert response.json()["name"] == "Jane Doe"

def test_delete_lead(db_session):
    lead_id = 1
    response = client.delete(f"/leads/{lead_id}")
    assert response.status_code == 204

# Test cases for campaign-related API endpoints
def test_create_campaign(db_session):
    response = client.post("/campaigns/", json={"name": "Test Campaign", "description": "A test campaign"})
    assert response.status_code == 201
    assert response.json()["name"] == "Test Campaign"

def test_get_campaign(db_session):
    campaign_id = 1
    response = client.get(f"/campaigns/{campaign_id}")
    assert response.status_code == 200
    assert response.json()["id"] == campaign_id

def test_update_campaign(db_session):
    campaign_id = 1
    response = client.put(f"/campaigns/{campaign_id}", json={"name": "Updated Campaign", "description": "An updated campaign"})
    assert response.status_code == 200
    assert response.json()["name"] == "Updated Campaign"

def test_delete_campaign(db_session):
    campaign_id = 1
    response = client.delete(f"/campaigns/{campaign_id}")
    assert response.status_code == 204

# Test cases for email-related API endpoints
def test_create_email(db_session):
    response = client.post("/emails/", json={"subject": "Test Email", "body": "This is a test email", "campaign_id": 1})
    assert response.status_code == 201
    assert response.json()["subject"] == "Test Email"

def test_get_email(db_session):
    email_id = 1
    response = client.get(f"/emails/{email_id}")
    assert response.status_code == 200
    assert response.json()["id"] == email_id

def test_update_email(db_session):
    email_id = 1
    response = client.put(f"/emails/{email_id}", json={"subject": "Updated Email", "body": "This is an updated email", "campaign_id": 1})
    assert response.status_code == 200
    assert response.json()["subject"] == "Updated Email"

def test_delete_email(db_session):
    email_id = 1
    response = client.delete(f"/emails/{email_id}")
    assert response.status_code == 204

# Test cases for scrape-related API endpoints
def test_scrape_company(db_session):
    company_id = 1
    response = client.post(f"/scrape/company/{company_id}")
    assert response.status_code == 200
    assert "scraped_data" in response.json()

def test_scrape_lead(db_session):
    lead_id = 1
    response = client.post(f"/scrape/lead/{lead_id}")
    assert response.status_code == 200
    assert "scraped_data" in response.json()

# HUMAN ASSISTANCE NEEDED
# The following test cases might need to be adjusted based on the actual implementation of the scraping functionality
# and the expected response format. Please review and modify as necessary.

def test_scrape_company_error(db_session):
    non_existent_company_id = 9999
    response = client.post(f"/scrape/company/{non_existent_company_id}")
    assert response.status_code == 404

def test_scrape_lead_error(db_session):
    non_existent_lead_id = 9999
    response = client.post(f"/scrape/lead/{non_existent_lead_id}")
    assert response.status_code == 404