variable "credentials" {
  description = "my creds"
  default     = "./keys/my-creds.json"

}

variable "project" {
  description = "project name"
  default     = "ny-rides-micah-448019"
}

variable "location" {
  description = "project location"
  default     = "US"
}

variable "region" {
  description = "project region"
  default     = "us-central1"
}

variable "bq_dataset_name" {
  description = "My BiqQuery Dataset Name"
  default     = "demo_dataset"
}

variable "gcs_bucket_name" {
  description = "My storage bucket name"
  default     = "ny-rides-micah-448019-terra-bucket"
}

variable "gsc_storage_clasee" {
  description = "Bucket Storage Class"
  default     = "STANDARD"
}
