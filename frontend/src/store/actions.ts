import { createAction } from '@reduxjs/toolkit';
import { Lead } from '../schema/lead';
import { Company } from '../schema/company';
import { Campaign } from '../schema/campaign';
import { Email } from '../schema/email';

export const setCompanies = createAction<Company[]>('setCompanies');
export const setLeads = createAction<Lead[]>('setLeads');
export const setCampaigns = createAction<Campaign[]>('setCampaigns');
export const setEmails = createAction<Email[]>('setEmails');