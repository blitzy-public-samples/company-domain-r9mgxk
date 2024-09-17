import React, { useState, useEffect } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { CampaignList } from '../components/CampaignList';
import { CampaignCreator } from '../components/CampaignCreator';
import { CampaignDetails } from '../components/CampaignDetails';
import { fetchCampaigns, createCampaign, updateCampaign } from '../store/actions';
import { ApiService } from '../services/api';

// HUMAN ASSISTANCE NEEDED
// The following component may need additional error handling, loading states, and optimization.
// Please review and enhance as necessary for production readiness.

const CampaignManagement: React.FC = () => {
  const dispatch = useDispatch();
  const campaigns = useSelector((state: any) => state.campaigns);
  const [selectedCampaign, setSelectedCampaign] = useState<any>(null);

  useEffect(() => {
    dispatch(fetchCampaigns());
  }, [dispatch]);

  const handleCreateCampaign = async (campaignData: any) => {
    try {
      await dispatch(createCampaign(campaignData));
      // Refresh campaigns list after creation
      dispatch(fetchCampaigns());
    } catch (error) {
      console.error('Failed to create campaign:', error);
      // TODO: Add proper error handling and user feedback
    }
  };

  const handleSelectCampaign = (campaign: any) => {
    setSelectedCampaign(campaign);
  };

  const handleUpdateCampaign = async (updatedCampaign: any) => {
    try {
      await dispatch(updateCampaign(updatedCampaign));
      // Refresh campaigns list after update
      dispatch(fetchCampaigns());
      setSelectedCampaign(updatedCampaign);
    } catch (error) {
      console.error('Failed to update campaign:', error);
      // TODO: Add proper error handling and user feedback
    }
  };

  return (
    <div className="campaign-management">
      <h1>Campaign Management</h1>
      <div className="campaign-management__content">
        <CampaignList 
          campaigns={campaigns} 
          onSelectCampaign={handleSelectCampaign} 
        />
        <CampaignCreator onCreateCampaign={handleCreateCampaign} />
        {selectedCampaign && (
          <CampaignDetails 
            campaign={selectedCampaign} 
            onUpdateCampaign={handleUpdateCampaign} 
          />
        )}
      </div>
    </div>
  );
};

export default CampaignManagement;