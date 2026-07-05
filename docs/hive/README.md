# Add the Bitnami Helm repository
helm repo add bitnami https://charts.bitnami.com/bitnami
helm repo update bitnami

# Search for the exact chart name
helm search repo bitnami/postgresql

# Save default values to a file
helm show values bitnami/postgresql > infra/hive/hms-postgresql/values.yaml

# Create a namespace for Hive
kubectl create namespace metastore

# Installing the Chart (toy-setup)
helm upgrade --install hms-postgresql -f infra/hive/hms-postgresql/values.yaml bitnami/postgresql --namespace metastore --timeout 15m

# Build the Hive Docker image
docker build -t hive-metastore:3.0.0 infra/hive/

# Build the Hive init Docker image
docker build -t hive-init:4.2.0 infra/hive/init/

# Load the Hive Docker image into the kind cluster
kind load docker-image hive-metastore:3.0.0 --name lakehouse
kind load docker-image hive-init:4.2.0 --name lakehouse

# Deploy Hive Metastore
kubectl apply -f infra/hive/init/job.yaml -n metastore
kubectl apply -f infra/hive/configmap.yaml -n metastore
kubectl apply -f infra/hive/deployment.yaml -n metastore
kubectl apply -f infra/hive/service.yaml -n metastore