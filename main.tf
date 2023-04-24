provider "google" {
  project = "your-gcp-project-id"
  region  = "us-central1"
  zone    = "us-central1-a"
}

resource "google_compute_network" "vpc" {
  name                    = "my-webapp-vpc"
  auto_create_subnetworks = "false"
}

resource "google_compute_subnetwork" "subnet" {
  name          = "my-webapp-subnet"
  ip_cidr_range = "10.0.1.0/24"
  network       = google_compute_network.vpc.self_link
}

resource "google_compute_firewall" "firewall" {
  name    = "my-webapp-firewall"
  network = google_compute_network.vpc.self_link

  allow {
    protocol = "tcp"
    ports    = ["80", "443", "22"]
  }

  source_ranges = ["0.0.0.0/0"]
}

resource "google_compute_instance" "default" {
  name         = "my-webapp-instance"
  machine_type = "f1-micro"

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
                            apt-get install -y apache2
                            systemctl start apache2
                            systemctl enable apache2
                            echo "Hello, World!" > /var/www/html/index.html
                            EOF
}
