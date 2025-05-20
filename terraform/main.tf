terraform {
  required_version = ">= 1.3"

  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "~> 5.0"
    }
  }
}

provider "google" {
  project = "psychic-empire-453222-i1"   # Replace this with your actual GCP project ID
  region  = "us-central"            # Or whatever region you're using (e.g., "us-west1")
}

# Example resource: App Engine application (required before deploying to App Engine)
resource "google_app_engine_application" "app" {
  location_id = "us-central"        # Should match your region
}
