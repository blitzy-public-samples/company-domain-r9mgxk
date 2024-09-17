import React, { useState, useEffect } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import DashboardMetrics from '../components/DashboardMetrics';
import RecentActivity from '../components/RecentActivity';
import QuickActions from '../components/QuickActions';
import { fetchDashboardData } from '../store/actions';
import { ApiService } from '../services/api';

const Dashboard: React.FC = () => {
  const [dashboardData, setDashboardData] = useState<any>(null);
  const dispatch = useDispatch();
  const { loading, error } = useSelector((state: any) => state.dashboard);

  useEffect(() => {
    const fetchData = async () => {
      try {
        dispatch(fetchDashboardData());
        const data = await ApiService.getDashboardData();
        setDashboardData(data);
      } catch (error) {
        console.error('Error fetching dashboard data:', error);
      }
    };

    fetchData();
  }, [dispatch]);

  if (loading) return <div>Loading...</div>;
  if (error) return <div>Error: {error}</div>;
  if (!dashboardData) return null;

  return (
    <div className="dashboard">
      <h1>Dashboard</h1>
      <DashboardMetrics metrics={dashboardData.metrics} />
      <RecentActivity activities={dashboardData.recentActivities} />
      <QuickActions actions={dashboardData.quickActions} />
    </div>
  );
};

export default Dashboard;