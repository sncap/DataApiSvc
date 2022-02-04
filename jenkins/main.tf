/*****************************************
  Google Provider Configuration
 *****************************************/
provider "google" {
}

/*****************************************
  Kubernetes provider configuration
 *****************************************/
provider "kubernetes" {
  host                   = "https://${module.jenkins-gke.endpoint}"
  token                  = data.google_client_config.default.access_token
  cluster_ca_certificate = base64decode(module.jenkins-gke.ca_certificate)
}

/*****************************************
  Helm provider configuration
 *****************************************/
provider "helm" {
  kubernetes {
    cluster_ca_certificate = base64decode(module.jenkins-gke.ca_certificate)
    host                   = "https://${module.jenkins-gke.endpoint}"
    token = data.google_client_config.default.access_token
  }
}