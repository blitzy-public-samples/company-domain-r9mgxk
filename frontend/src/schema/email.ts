interface Email {
  id: string;
  subject: string;
  body: string;
  generatedAt: Date;
  status: string;
  leadId: string;
  campaignId: string;
  metadata: Record<string, any>;
}