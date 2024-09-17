import axios, { AxiosInstance } from 'axios';
import { settings } from 'backend.app.core.config';
import { Company } from '../schema/company';
import { Lead } from '../schema/lead';

const API_BASE_URL = settings.API_V1_STR;

const createApiClient = (): AxiosInstance => {
  const instance = axios.create({
    baseURL: API_BASE_URL,
    headers: {
      'Content-Type': 'application/json',
    },
  });

  instance.interceptors.request.use(
    (config) => {
      // Add authentication token if available
      const token = localStorage.getItem('token');
      if (token) {
        config.headers['Authorization'] = `Bearer ${token}`;
      }
      return config;
    },
    (error) => Promise.reject(error)
  );

  instance.interceptors.response.use(
    (response) => response,
    (error) => {
      // Handle common errors (e.g., 401 Unauthorized)
      if (error.response && error.response.status === 401) {
        // Redirect to login or refresh token
      }
      return Promise.reject(error);
    }
  );

  return instance;
};

class ApiService {
  private client: AxiosInstance;

  constructor() {
    this.client = createApiClient();
  }

  async getCompanies(): Promise<Company[]> {
    const response = await this.client.get<Company[]>('/companies');
    return response.data;
  }

  async createLead(leadData: Lead): Promise<Lead> {
    const response = await this.client.post<Lead>('/leads', leadData);
    return response.data;
  }
}

export default new ApiService();