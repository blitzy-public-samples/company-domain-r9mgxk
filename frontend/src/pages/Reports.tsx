import React, { useState, useEffect } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import ReportGenerator from '../components/ReportGenerator';
import ReportViewer from '../components/ReportViewer';
import { fetchReports, generateReport } from '../store/actions';
import { ApiService } from '../services/api';

// HUMAN ASSISTANCE NEEDED
// The confidence level is below 0.8, so this component may need review and improvements.
// Please check the implementation and make necessary adjustments.

const Reports: React.FC = () => {
  const [reports, setReports] = useState<any[]>([]);
  const [selectedReport, setSelectedReport] = useState<any | null>(null);
  const dispatch = useDispatch();

  useEffect(() => {
    const fetchReportsData = async () => {
      try {
        const fetchedReports = await dispatch(fetchReports());
        setReports(fetchedReports);
      } catch (error) {
        console.error('Error fetching reports:', error);
      }
    };
    fetchReportsData();
  }, [dispatch]);

  const handleGenerateReport = async (reportData: any) => {
    try {
      const newReport = await dispatch(generateReport(reportData));
      setReports([...reports, newReport]);
    } catch (error) {
      console.error('Error generating report:', error);
    }
  };

  const handleReportSelection = (report: any) => {
    setSelectedReport(report);
  };

  return (
    <div className="reports-page">
      <h1>Reports</h1>
      <ReportGenerator onGenerateReport={handleGenerateReport} />
      <div className="reports-list">
        <h2>Available Reports</h2>
        <ul>
          {reports.map((report) => (
            <li key={report.id} onClick={() => handleReportSelection(report)}>
              {report.name}
            </li>
          ))}
        </ul>
      </div>
      {selectedReport && <ReportViewer report={selectedReport} />}
    </div>
  );
};

export default Reports;