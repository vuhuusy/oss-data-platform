# Helm
```bash
helm repo add starrocks https://starrocks.github.io/starrocks-kubernetes-operator
helm repo update
helm search repo starrocks

helm show values starrocks/kube-starrocks > infra/starrocks/values.yaml

helm upgrade --install starrocks starrocks/kube-starrocks -f infra/starrocks/values.yaml -n compute

kubectl port-forward svc/kube-starrocks-fe-service 9030:9030 -n compute &
```

# Create External Catalog in StarRocks

```sql
CREATE EXTERNAL CATALOG lakehouse
PROPERTIES
(
    "type" = "unified",
    "unified.metastore.type" = "hive",
    "hive.metastore.uris" = "thrift://hive-metastore.metastore.svc.cluster.local:9083",
    "aws.s3.enable_ssl" = "false",
    "aws.s3.enable_path_style_access" = "true",
    "aws.s3.endpoint" = "http://minio.storage.svc.cluster.local:9000",
    "aws.s3.access_key" = "minioadmin",
    "aws.s3.secret_key" = "minioadmin"
);
```

# Delete
```bash
helm uninstall starrocks -n compute
```