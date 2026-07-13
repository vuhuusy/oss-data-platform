docker build -t apache/airflow-dbt-cosmos:slim-3.2.2-python3.12 infra/airflow/
kind load docker-image apache/airflow-dbt-cosmos:slim-3.2.2-python3.12 --name lakehouse

helm repo add airflow https://airflow.apache.org
helm repo update
helm search repo airflow
helm show values airflow/airflow > infra/airflow/values.yaml


k apply -f infra/airflow/configmap.yaml -n operation
k apply -f infra/airflow/secret.yaml -n operation
helm upgrade --install airflow airflow/airflow -f infra/airflow/values.yaml -n operation --create-namespace

kubectl port-forward svc/airflow-api-server 8080:8080 -n operation &


helm uninstall airflow -n operation