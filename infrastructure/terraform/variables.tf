variable "project_id" {
  description = "The ID of the Google Cloud project"
  type        = string
}

variable "region" {
  description = "The region to deploy resources"
  type        = string
  default     = "us-central1"
}

variable "zone" {
  description = "The zone within the region to deploy resources"
  type        = string
  default     = "us-central1-a"
}

variable "vpc_network_name" {
  description = "The name of the VPC network"
  type        = string
  default     = "main-vpc"
}

variable "vpc_cidr_range" {
  description = "The CIDR range for the VPC network"
  type        = string
  default     = "10.0.0.0/16"
}

variable "gke_node_count" {
  description = "The number of nodes in the GKE cluster"
  type        = number
  default     = 3
}

variable "gke_machine_type" {
  description = "The machine type for GKE nodes"
  type        = string
  default     = "n1-standard-2"
}

variable "db_instance_name" {
  description = "The name of the database instance"
  type        = string
}

variable "db_version" {
  description = "The database engine version"
  type        = string
  default     = "POSTGRES_13"
}

variable "db_tier" {
  description = "The machine type of the database instance"
  type        = string
  default     = "db-f1-micro"
}

variable "storage_bucket_names" {
  description = "A list of storage bucket names to create"
  type        = list(string)
}

variable "service_account_names" {
  description = "A map of service account names and their roles"
  type        = map(list(string))
  default     = {
    "gke-sa" = ["roles/container.nodeServiceAccount"],
    "app-sa" = ["roles/storage.objectViewer", "roles/cloudsql.client"]
  }
}

# HUMAN ASSISTANCE NEEDED
# Consider adding more specific variables for GKE cluster configuration,
# such as cluster_ipv4_cidr, services_ipv4_cidr, cluster_secondary_range_name,
# and services_secondary_range_name for more granular network control.
# Also, consider adding variables for enabling specific GKE features like
# workload identity, network policy, etc.