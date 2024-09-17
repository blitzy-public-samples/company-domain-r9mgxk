import React from 'react';
import { Lead } from '../schema/lead';

const LeadCard: React.FC<{ lead: Lead }> = ({ lead }) => {
  const { name, email, phone, status, company } = lead;

  const getStatusColor = (status: string) => {
    switch (status.toLowerCase()) {
      case 'new':
        return 'bg-blue-100 text-blue-800';
      case 'contacted':
        return 'bg-yellow-100 text-yellow-800';
      case 'qualified':
        return 'bg-green-100 text-green-800';
      case 'lost':
        return 'bg-red-100 text-red-800';
      default:
        return 'bg-gray-100 text-gray-800';
    }
  };

  return (
    <div className="bg-white shadow-md rounded-lg p-6 mb-4">
      <h2 className="text-xl font-semibold mb-2">{name}</h2>
      <p className="text-gray-600 mb-1">{company}</p>
      <p className="text-gray-600 mb-1">{email}</p>
      <p className="text-gray-600 mb-3">{phone}</p>
      <span className={`px-2 py-1 rounded-full text-sm font-semibold ${getStatusColor(status)}`}>
        {status}
      </span>
    </div>
  );
};

export default LeadCard;