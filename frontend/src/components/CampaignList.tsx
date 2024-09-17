import React from 'react';
import { Campaign } from '../schema/campaign';
import { CampaignCard } from './CampaignCard';

// HUMAN ASSISTANCE NEEDED
// The following component may need additional styling and error handling for production readiness.
// Consider adding loading states, error boundaries, and empty state handling.

const CampaignList: React.FC<{ campaigns: Campaign[] }> = ({ campaigns }) => {
  return (
    <div className="campaign-list">
      {campaigns.map((campaign) => (
        <CampaignCard key={campaign.id} campaign={campaign} />
      ))}
    </div>
  );
};

export default CampaignList;