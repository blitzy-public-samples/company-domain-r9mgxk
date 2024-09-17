#!/bin/bash

# Check for required system dependencies
command -v python3 >/dev/null 2>&1 || { echo >&2 "Python 3 is required but not installed. Aborting."; exit 1; }
command -v node >/dev/null 2>&1 || { echo >&2 "Node.js is required but not installed. Aborting."; exit 1; }
command -v npm >/dev/null 2>&1 || { echo >&2 "npm is required but not installed. Aborting."; exit 1; }

# Install necessary software packages
sudo apt-get update
sudo apt-get install -y build-essential libssl-dev libffi-dev python3-dev

# Set up Python virtual environment
python3 -m venv venv
source venv/bin/activate

# Install Python dependencies from requirements.txt
pip install -r requirements.txt

# Set up Node.js environment and install npm packages
npm install

# Configure environment variables
cat << EOF > .env
DEBUG=False
SECRET_KEY=$(openssl rand -hex 32)
DATABASE_URL=postgresql://user:password@localhost:5432/dbname
EOF

# Initialize database schemas
# HUMAN ASSISTANCE NEEDED
# The following block needs to be adjusted based on the specific database and ORM being used
python manage.py db init
python manage.py db migrate
python manage.py db upgrade

echo "Environment setup complete!"