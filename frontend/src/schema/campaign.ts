import { Email } from './email';

export interface Campaign {
  id: string;
  name: string;
  startDate: Date;
  endDate: Date;
  emails: Email[];
  metadata: Record<string, any>;
}