import pytest
from unittest.mock import patch, MagicMock
from celery.exceptions import Retry
from app.tasks import scrape_company, analyze_lead, generate_and_send_email
from app.models import Company, Lead

@pytest.fixture
def mock_company():
    return Company(name="Test Company", website="https://testcompany.com")

@pytest.fixture
def mock_lead():
    return Lead(company_name="Test Company", email="test@example.com")

@patch('app.tasks.scrape_website')
def test_scrape_company_success(mock_scrape):
    mock_scrape.return_value = {"name": "Test Company", "website": "https://testcompany.com"}
    result = scrape_company.delay("https://testcompany.com")
    assert result.get() == {"name": "Test Company", "website": "https://testcompany.com"}
    mock_scrape.assert_called_once_with("https://testcompany.com")

@patch('app.tasks.scrape_website')
def test_scrape_company_retry(mock_scrape):
    mock_scrape.side_effect = Exception("Connection error")
    with pytest.raises(Retry):
        scrape_company.delay("https://testcompany.com")

@patch('app.tasks.analyze_company_data')
def test_analyze_lead_success(mock_analyze, mock_company):
    mock_analyze.return_value = {"score": 0.8, "summary": "Good lead"}
    result = analyze_lead.delay(mock_company.id)
    assert result.get() == {"score": 0.8, "summary": "Good lead"}
    mock_analyze.assert_called_once_with(mock_company)

@patch('app.tasks.analyze_company_data')
def test_analyze_lead_retry(mock_analyze, mock_company):
    mock_analyze.side_effect = Exception("Analysis error")
    with pytest.raises(Retry):
        analyze_lead.delay(mock_company.id)

@patch('app.tasks.generate_email_content')
@patch('app.tasks.send_email')
def test_generate_and_send_email_success(mock_send, mock_generate, mock_lead):
    mock_generate.return_value = "Email content"
    result = generate_and_send_email.delay(mock_lead.id)
    assert result.get() == "Email sent successfully"
    mock_generate.assert_called_once_with(mock_lead)
    mock_send.assert_called_once_with(mock_lead.email, "Email content")

@patch('app.tasks.generate_email_content')
def test_generate_and_send_email_retry(mock_generate, mock_lead):
    mock_generate.side_effect = Exception("Generation error")
    with pytest.raises(Retry):
        generate_and_send_email.delay(mock_lead.id)

# HUMAN ASSISTANCE NEEDED
# The following test cases might need additional assertions or mocking depending on the exact implementation of the tasks:
# - Test for edge cases in scrape_company (e.g., invalid URLs)
# - Test for different analysis outcomes in analyze_lead
# - Test for email sending failures in generate_and_send_email
# Please review and add these test cases as needed.