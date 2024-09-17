import axios from 'axios';
import { settings } from 'backend.app.core.config';

const AUTH_TOKEN_KEY = 'auth_token';

export function setAuthToken(token: string): void {
  localStorage.setItem(AUTH_TOKEN_KEY, token);
}

export function getAuthToken(): string | null {
  return localStorage.getItem(AUTH_TOKEN_KEY);
}

export class AuthService {
  private client: axios.AxiosInstance;

  constructor() {
    this.client = axios.create({
      baseURL: settings.API_BASE_URL,
    });
  }

  async login(username: string, password: string): Promise<boolean> {
    try {
      const response = await this.client.post('/auth/login', { username, password });
      if (response.data && response.data.token) {
        setAuthToken(response.data.token);
        return true;
      }
      return false;
    } catch (error) {
      console.error('Login failed:', error);
      return false;
    }
  }

  logout(): void {
    localStorage.removeItem(AUTH_TOKEN_KEY);
    // HUMAN ASSISTANCE NEEDED
    // Additional steps might be needed to clear user-related data from application state
    // Depending on the state management solution used (e.g., Redux, MobX, React Context),
    // you may need to dispatch an action or update a global state to reflect the logout
    // Example:
    // store.dispatch(clearUserData());
    // or
    // setUserContext(null);
  }
}