provider "google" {
  project = var.project_id
  region  = "europe-west8"
  zone    = "europe-west8-a"
}

variable "project_id" {
  type        = string
  description = "GPC ID"
}

resource "google_compute_network" "vpc" {
  name                    = "webmaptracker-vpc"
  auto_create_subnetworks = "false"
}

resource "google_compute_subnetwork" "subnet" {
  name          = "my-webapp-subnet"
  ip_cidr_range = "10.0.1.0/24"
  region        = "europe-west8"
  network       = google_compute_network.vpc.self_link
}

resource "google_compute_firewall" "firewall" {
  name    = "my-webapp-firewall"
  network = google_compute_network.vpc.self_link

  allow {
    protocol = "tcp"
    ports    = ["80", "443"]
  }

  source_ranges = ["0.0.0.0/0"]
}

resource "google_compute_instance" "default" {
  name         = "webmaptracker"
  machine_type = "e2-micro"

  boot_disk {
    initialize_params {
      image = "projects/debian-cloud/global/images/family/debian-10"
    }
  }

  network_interface {
    subnetwork = google_compute_subnetwork.subnet.self_link

    access_config {
      // Ephemeral external IP
    }
  }

  metadata_startup_script = <<-EOF
                            #!/bin/bash
                            apt-get update
                            apt-get install -y docker.io
                            docker pull johankovamees/wmt_be:latest
                            docker pull johankovamees/wmt_fe:latest
                            docker run -d --name wmt_be -p 5000:5000 johankovamees/wmt_be:latest
                            docker run -d --name wmt_fe -p 80:80 -p 443:443 johankovamees/wmt_fe:latest
                            EOF
}
