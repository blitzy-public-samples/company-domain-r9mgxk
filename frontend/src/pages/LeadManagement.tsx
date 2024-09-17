import React, { useState, useEffect } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import LeadList from '../components/LeadList';
import LeadDetails from '../components/LeadDetails';
import { fetchLeads, updateLead } from '../store/actions';
import { ApiService } from '../services/api';

// HUMAN ASSISTANCE NEEDED
// This component may need additional error handling, loading states, and optimization for production readiness.
// Please review and enhance as necessary.

const LeadManagement: React.FC = () => {
  const [selectedLead, setSelectedLead] = useState<Lead | null>(null);
  const dispatch = useDispatch();
  const leads = useSelector((state: RootState) => state.leads);

  useEffect(() => {
    dispatch(fetchLeads());
  }, [dispatch]);

  const handleLeadSelection = (lead: Lead) => {
    setSelectedLead(lead);
  };

  const handleLeadUpdate = async (updatedLead: Lead) => {
    try {
      await dispatch(updateLead(updatedLead));
      setSelectedLead(updatedLead);
    } catch (error) {
      console.error('Failed to update lead:', error);
      // TODO: Implement proper error handling and user feedback
    }
  };

  return (
    <div className="lead-management">
      <h1>Lead Management</h1>
      <div className="lead-management-content">
        <LeadList 
          leads={leads} 
          onLeadSelect={handleLeadSelection} 
        />
        {selectedLead && (
          <LeadDetails 
            lead={selectedLead} 
            onLeadUpdate={handleLeadUpdate} 
          />
        )}
      </div>
    </div>
  );
};

export default LeadManagement;