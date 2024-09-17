from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class Company(Base):
    __tablename__ = 'companies'

    id = Column(Integer, primary_key=True)
    domain = Column(String, unique=True, nullable=False)
    name = Column(String, nullable=False)
    description = Column(Text)
    industry = Column(String)
    employee_count = Column(Integer)
    technologies = Column(Text)
    metadata = Column(Text)

    leads = relationship("Lead", back_populates="company")

class Lead(Base):
    __tablename__ = 'leads'

    id = Column(Integer, primary_key=True)
    company_id = Column(Integer, ForeignKey('companies.id'), nullable=False)
    status = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    ceo_name = Column(String)
    ceo_linkedin_url = Column(String)
    ceo_email = Column(String)
    ceo_phone = Column(String)
    metadata = Column(Text)

    company = relationship("Company", back_populates="leads")
    emails = relationship("Email", back_populates="lead")

class Campaign(Base):
    __tablename__ = 'campaigns'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    start_date = Column(DateTime, nullable=False)
    end_date = Column(DateTime)
    email_ids = Column(Text)
    metadata = Column(Text)

    emails = relationship("Email", back_populates="campaign")

class Email(Base):
    __tablename__ = 'emails'

    id = Column(Integer, primary_key=True)
    subject = Column(String, nullable=False)
    body = Column(Text, nullable=False)
    generated_at = Column(DateTime, default=datetime.utcnow)
    status = Column(String, nullable=False)
    lead_id = Column(Integer, ForeignKey('leads.id'), nullable=False)
    campaign_id = Column(Integer, ForeignKey('campaigns.id'), nullable=False)
    metadata = Column(Text)

    lead = relationship("Lead", back_populates="emails")
    campaign = relationship("Campaign", back_populates="emails")