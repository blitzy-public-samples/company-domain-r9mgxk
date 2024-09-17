export interface Company {
  id: string;
  domain: string;
  name: string;
  description: string;
  industry: string;
  employeeCount: number;
  technologies: string[];
  metadata: Record<string, any>;
}