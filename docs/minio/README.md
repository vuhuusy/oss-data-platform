# Add the Minio Helm repository
helm repo add minio https://charts.min.io/
helm repo update minio

# Search for the exact chart name
helm search repo minio

# Save default values to a file
helm show values minio/minio > infra/minio/values.yaml

# Create a namespace for Minio
kubectl create namespace storage

# Installing the Chart (toy-setup)
helm upgrade --install minio -f infra/minio/values.yaml minio/minio --namespace storage --timeout 15m

# To access MinIO Console & API
kubectl port-forward svc/minio-console 9001:9001 -n storage
kubectl port-forward svc/minio 9000:9000 -n storage

# Set TTL for Kyuubi Spark Staging Files in MinIO

```bash
mc alias set minio http://localhost:9000 minioadmin minioadmin

mc ilm rule add minio/jars \
  --prefix "kyuubi/spark-upload/" \
  --expire-days 1

mc ilm rule list minio/jars
```