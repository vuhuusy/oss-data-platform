# Helm
```bash
helm repo add starrocks https://starrocks.github.io/starrocks-kubernetes-operator
helm repo update
helm search repo starrocks

helm show values starrocks/kube-starrocks > infra/starrocks/values.yaml

helm install starrocks starrocks/kube-starrocks -f infra/starrocks/values.yaml -n compute
```

kubectl port-forward svc/kube-starrocks-fe-service 8030:8030 -n compute &