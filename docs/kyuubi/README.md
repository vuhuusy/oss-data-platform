# Build Spark custom image
```bash
docker build -t apache/spark:3.5.8-iceberg -f infra/kyuubi/Dockerfile.spark .
docker build -t apache/kyuubi:1.11.1-spark-iceberg infra/kyuubi/

kind load docker-image apache/spark:3.5.8-iceberg --name lakehouse
kind load docker-image apache/kyuubi:1.11.1-spark-iceberg --name lakehouse
```

# Helm chart

```bash
helm repo add helmforge https://repo.helmforge.dev
helm repo update

helm show values helmforge/zookeeper > infra/kyuubi/zookeeper/values.yaml

kubectl create ns compute

helm upgrade --install zookeeper helmforge/zookeeper -f infra/kyuubi/zookeeper/values.yaml -n metastore --timeout 15m 

kubectl apply -f infra/kyuubi/configmap.yaml -n compute

kubectl apply -f infra/kyuubi/spark-rbac.yaml -n compute

helm upgrade --install kyuubi infra/kyuubi/chart -f infra/kyuubi/chart/values.yaml -n compute

kubectl port-forward svc/kyuubi-thrift-binary 10009:10009 -n compute &
```

# Delete
```bash
helm uninstall kyuubi -n compute
helm uninstall zookeeper -n metastore
kubectl delete -f infra/kyuubi/configmap.yaml -n compute
kubectl delete -f infra/kyuubi/spark-rbac.yaml -n compute
```