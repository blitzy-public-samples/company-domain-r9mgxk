output "vpc_network_id" {
  description = "The ID of the VPC network"
  value       = google_compute_network.vpc_network.id
}

output "gke_cluster_endpoint" {
  description = "The endpoint for accessing the GKE cluster"
  value       = google_container_cluster.primary.endpoint
}

output "gke_cluster_credentials" {
  description = "The credentials for accessing the GKE cluster"
  value       = google_container_cluster.primary.master_auth
  sensitive   = true
}

output "cloud_sql_instance_connection_name" {
  description = "The connection name of the Cloud SQL instance"
  value       = google_sql_database_instance.main.connection_name
}

output "storage_bucket_urls" {
  description = "The URLs of the created storage buckets"
  value = {
    for bucket in google_storage_bucket.buckets :
    bucket.name => bucket.url
  }
}

output "service_account_emails" {
  description = "The email addresses of the created service accounts"
  value = {
    gke     = google_service_account.gke_sa.email
    cloudsql = google_service_account.cloudsql_sa.email
    storage = google_service_account.storage_sa.email
  }
}

# HUMAN ASSISTANCE NEEDED
# Please verify that all necessary resources (VPC network, GKE cluster, Cloud SQL instance, storage buckets, and service accounts)
# are correctly referenced in the outputs. Adjust resource names if they differ from the assumed names used here.