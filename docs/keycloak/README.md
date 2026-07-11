helm repo add helmforge https://repo.helmforge.dev
helm search repo keycloak

helm show values helmforge/keycloak > infra/keycloak/values.yaml

helm upgrade --install keycloak helmforge/keycloak -f infra/keycloak/values.yaml -n iam

kubectl port-forward -n iam service/keycloak-keycloak 8082:8080 &