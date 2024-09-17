import React, { useState } from 'react';
import { Email } from '../schema/email';

// HUMAN ASSISTANCE NEEDED
// The confidence level for this component is below 0.8. 
// Please review and refine the implementation, especially the form structure and state management.

const EmailTemplate: React.FC<{ template: Email; onUpdate: (updatedTemplate: Email) => void }> = ({ template, onUpdate }) => {
  const [currentTemplate, setCurrentTemplate] = useState<Email>(template);

  const handleInputChange = (e: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement>) => {
    const { name, value } = e.target;
    setCurrentTemplate(prev => ({ ...prev, [name]: value }));
  };

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    onUpdate(currentTemplate);
  };

  return (
    <form onSubmit={handleSubmit}>
      <div>
        <label htmlFor="subject">Subject:</label>
        <input
          type="text"
          id="subject"
          name="subject"
          value={currentTemplate.subject}
          onChange={handleInputChange}
        />
      </div>
      <div>
        <label htmlFor="body">Body:</label>
        <textarea
          id="body"
          name="body"
          value={currentTemplate.body}
          onChange={handleInputChange}
        />
      </div>
      <button type="submit">Update Template</button>
    </form>
  );
};

export default EmailTemplate;