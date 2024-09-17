# Main Terraform configuration for B2B lead generation and outreach solution

# Provider configuration for Google Cloud Platform
provider "google" {
  project = var.project_id
  region  = var.region
}

# VPC network and subnet definitions
resource "google_compute_network" "vpc_network" {
  name                    = "b2b-lead-gen-network"
  auto_create_subnetworks = false
}

resource "google_compute_subnetwork" "subnet" {
  name          = "b2b-lead-gen-subnet"
  ip_cidr_range = "10.0.0.0/24"
  region        = var.region
  network       = google_compute_network.vpc_network.id
}

# Google Kubernetes Engine (GKE) cluster configuration
resource "google_container_cluster" "primary" {
  name     = "b2b-lead-gen-cluster"
  location = var.region

  remove_default_node_pool = true
  initial_node_count       = 1

  network    = google_compute_network.vpc_network.name
  subnetwork = google_compute_subnetwork.subnet.name
}

resource "google_container_node_pool" "primary_nodes" {
  name       = "b2b-lead-gen-node-pool"
  location   = var.region
  cluster    = google_container_cluster.primary.name
  node_count = var.gke_num_nodes

  node_config {
    oauth_scopes = [
      "https://www.googleapis.com/auth/logging.write",
      "https://www.googleapis.com/auth/monitoring",
    ]

    labels = {
      env = var.project_id
    }

    machine_type = "n1-standard-1"
    tags         = ["gke-node", "b2b-lead-gen-gke"]
    metadata = {
      disable-legacy-endpoints = "true"
    }
  }
}

# Cloud SQL instance for PostgreSQL
resource "google_sql_database_instance" "main" {
  name             = "b2b-lead-gen-db-instance"
  database_version = "POSTGRES_13"
  region           = var.region

  settings {
    tier = "db-f1-micro"
  }

  deletion_protection = false
}

resource "google_sql_database" "database" {
  name     = "b2b_lead_gen_db"
  instance = google_sql_database_instance.main.name
}

# Cloud Storage buckets for data storage
resource "google_storage_bucket" "data_bucket" {
  name     = "b2b-lead-gen-data-bucket"
  location = var.region
}

# Cloud Pub/Sub topics and subscriptions
resource "google_pubsub_topic" "lead_updates" {
  name = "lead-updates"
}

resource "google_pubsub_subscription" "lead_updates_sub" {
  name  = "lead-updates-sub"
  topic = google_pubsub_topic.lead_updates.name
}

# IAM roles and service accounts
resource "google_service_account" "b2b_lead_gen_sa" {
  account_id   = "b2b-lead-gen-sa"
  display_name = "B2B Lead Generation Service Account"
}

resource "google_project_iam_member" "b2b_lead_gen_sa_roles" {
  project = var.project_id
  role    = "roles/editor"
  member  = "serviceAccount:${google_service_account.b2b_lead_gen_sa.email}"
}

# HUMAN ASSISTANCE NEEDED
# Please review the following:
# 1. Ensure that the VPC and subnet CIDR ranges are appropriate for your network design
# 2. Verify that the GKE node pool configuration meets your requirements (e.g., machine type, node count)
# 3. Review the Cloud SQL instance configuration and adjust the tier if necessary
# 4. Confirm that the IAM roles assigned to the service account are appropriate and follow the principle of least privilege