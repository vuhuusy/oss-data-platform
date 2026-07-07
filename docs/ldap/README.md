helm repo add openldap https://jp-gouin.github.io/helm-openldap/
helm repo update

helm search repo openldap

kubectl create namespace iam

helm show values openldap/openldap-stack-ha > infra/ldap/values.yaml

helm upgrade --install openldap openldap/openldap-stack-ha -n iam -f infra/ldap/values.yaml

kubectl cp infra/ldap/ldap-bootstrap.ldif   iam/openldap-0:/tmp/ldap-bootstrap.ldif