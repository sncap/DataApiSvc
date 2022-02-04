terraform {
  backend "gcs" {
    bucket = "architect-certification-289902-20-tfstate"
    prefix = "jenkins"
  }
}