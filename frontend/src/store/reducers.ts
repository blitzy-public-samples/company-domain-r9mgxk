import { createReducer } from '@reduxjs/toolkit';
import { setCompanies, setLeads, setCampaigns, setEmails } from './actions';
import { Lead } from '../schema/lead';
import { Company } from '../schema/company';
import { Campaign } from '../schema/campaign';
import { Email } from '../schema/email';

export const companiesReducer = createReducer<Company[]>([], (builder) => {
  builder.addCase(setCompanies, (state, action) => {
    return action.payload;
  });
});

export const leadsReducer = createReducer<Lead[]>([], (builder) => {
  builder.addCase(setLeads, (state, action) => {
    return action.payload;
  });
});

export const campaignsReducer = createReducer<Campaign[]>([], (builder) => {
  builder.addCase(setCampaigns, (state, action) => {
    return action.payload;
  });
});

export const emailsReducer = createReducer<Email[]>([], (builder) => {
  builder.addCase(setEmails, (state, action) => {
    return action.payload;
  });
});