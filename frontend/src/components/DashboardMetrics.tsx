import React, { useState, useEffect } from 'react';
import { ApiService } from '../services/api';
import { formatNumber } from '../utils/formatters';

// HUMAN ASSISTANCE NEEDED
// The following component may need additional styling and error handling for production readiness.
// Consider adding loading states, error handling, and responsive design.

const DashboardMetrics: React.FC = () => {
  const [metrics, setMetrics] = useState({
    totalUsers: 0,
    activeUsers: 0,
    revenue: 0,
    conversionRate: 0,
  });

  useEffect(() => {
    const fetchMetrics = async () => {
      try {
        const data = await ApiService.getMetrics();
        setMetrics(data);
      } catch (error) {
        console.error('Failed to fetch metrics:', error);
        // TODO: Implement proper error handling
      }
    };

    fetchMetrics();
  }, []);

  return (
    <div className="dashboard-metrics">
      <div className="metric-card">
        <i className="icon icon-users"></i>
        <h3>Total Users</h3>
        <p>{formatNumber(metrics.totalUsers)}</p>
      </div>
      <div className="metric-card">
        <i className="icon icon-active-users"></i>
        <h3>Active Users</h3>
        <p>{formatNumber(metrics.activeUsers)}</p>
      </div>
      <div className="metric-card">
        <i className="icon icon-revenue"></i>
        <h3>Revenue</h3>
        <p>${formatNumber(metrics.revenue, 2)}</p>
      </div>
      <div className="metric-card">
        <i className="icon icon-conversion"></i>
        <h3>Conversion Rate</h3>
        <p>{formatNumber(metrics.conversionRate, 2)}%</p>
      </div>
    </div>
  );
};

export default DashboardMetrics;