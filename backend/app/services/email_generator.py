from jinja2 import Template
from typing import Dict
from backend.app.core.config import settings
import os

class EmailGenerator:
    def __init__(self):
        self.templates: Dict[str, Template] = {}
        self._load_templates()

    def _load_templates(self):
        template_dir = settings.EMAIL_TEMPLATE_DIR
        for filename in os.listdir(template_dir):
            if filename.endswith('.html') or filename.endswith('.txt'):
                template_name = os.path.splitext(filename)[0]
                with open(os.path.join(template_dir, filename), 'r') as file:
                    template_content = file.read()
                    self.templates[template_name] = Template(template_content)

    def generate_email(self, template_name: str, lead_data: Dict[str, str]) -> str:
        if template_name not in self.templates:
            raise ValueError(f"Template '{template_name}' not found")
        
        template = self.templates[template_name]
        return template.render(**lead_data)

# HUMAN ASSISTANCE NEEDED
# The following aspects might need review or additional implementation:
# 1. Error handling for file operations in _load_templates method
# 2. Validation of lead_data in generate_email method
# 3. Logging of template loading and email generation processes
# 4. Potential caching mechanism for frequently used templates
# 5. Handling of different template formats (HTML/plain text)