# Data Platform Architecture

This document outlines the overall architecture of the data platform and provides deep-dive installation guides for each component.

# Prerequisites

## Install make

```bash
sudo apt update
sudo apt install build-essential make -y
```

## Install kubectl

```bash
# Download the latest stable binary
curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"

# Make the binary executable
chmod +x ./kubectl

# Move it to your local bin directory
sudo mv ./kubectl /usr/local/bin/kubectl

# Verify the installation
kubectl version --client
```

## Install kind

```bash
# Download the stable amd64 binary for Linux
curl -Lo ./kind https://kind.sigs.k8s.io/dl/v0.24.0/kind-linux-amd64

# Make the binary executable
chmod +x ./kind

# Move it to your local bin directory
sudo mv ./kind /usr/local/bin/kind

# Verify the installation
kind --version
```

## Install helm

```bash
# Fetch the installer script
curl -fsSL -o get_helm.sh https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3

# Grant execution permissions
chmod 700 get_helm.sh

# Run the script
./get_helm.sh

# Clean up the installation script
rm get_helm.sh

# Verify the installation
helm version
```

## Usefull bash aliases

```bash
nano ~/.bashrc

```

alias k='kubectl'

alias kgp='kubectl get pods'
alias kgpa='kubectl get pods -A'
alias kgn='kubectl get nodes'
alias kgs='kubectl get svc'
alias kga='kubectl get all'
alias kd='kubectl describe'
alias kdp='kubectl describe pod'
alias kl='kubectl logs'
alias kx='kubectl exec -it'
alias kaf='kubectl apply -f'
```

source ~/.bashrc
```

# System Components

## Set up a 3-node Kubernetes cluster using Kind

* **Role:** Manages and orchestrates containers in the local environment.
* **Infra Configuration:** [infra/kind/config.yaml](../infra/kind/config.yaml) *(Note: `../` goes up one level to the root, then into `infra`)*
* **Installation Guide:** [View Kind Deployment Guide](./kind/README.md)

## Install MinIO