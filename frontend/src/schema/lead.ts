import { Company } from './company';

export interface Lead {
  id: string;
  company: Company;
  status: string;
  createdAt: Date;
  updatedAt: Date;
  ceoName: string;
  ceoLinkedinUrl: string;
  ceoEmail: string;
  ceoPhone: string;
  metadata: Record<string, any>;
}