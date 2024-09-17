#!/bin/bash

set -e

# Authenticate with Google Cloud
echo "Authenticating with Google Cloud..."
gcloud auth activate-service-account --key-file=${GCP_SERVICE_ACCOUNT_KEY}

# Set up Google Cloud project
echo "Setting up Google Cloud project..."
gcloud config set project ${GCP_PROJECT_ID}
gcloud config set compute/zone ${GCP_COMPUTE_ZONE}

# Build and push Docker images
echo "Building and pushing Docker images..."
docker build -t gcr.io/${GCP_PROJECT_ID}/myapp:${VERSION} .
docker push gcr.io/${GCP_PROJECT_ID}/myapp:${VERSION}

# Apply Terraform configurations
echo "Applying Terraform configurations..."
cd terraform
terraform init
terraform apply -auto-approve

# Deploy application to Google Kubernetes Engine
echo "Deploying application to Google Kubernetes Engine..."
gcloud container clusters get-credentials ${GKE_CLUSTER_NAME}
kubectl apply -f k8s/

# Run database migrations
echo "Running database migrations..."
kubectl exec -it $(kubectl get pods -l app=myapp -o jsonpath="{.items[0].metadata.name}") -- ./manage.py migrate

# Perform post-deployment checks
echo "Performing post-deployment checks..."
kubectl get pods
kubectl get services

# Update DNS settings if needed
echo "Updating DNS settings..."
# HUMAN ASSISTANCE NEEDED
# The following block needs to be customized based on the specific DNS provider and requirements
# gcloud dns record-sets transaction start --zone=${DNS_ZONE}
# gcloud dns record-sets transaction add ${LOAD_BALANCER_IP} --name=${DOMAIN} --ttl=300 --type=A --zone=${DNS_ZONE}
# gcloud dns record-sets transaction execute --zone=${DNS_ZONE}

echo "Deployment completed successfully!"