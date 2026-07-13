helm repo add openldap https://jp-gouin.github.io/helm-openldap/
helm repo update

helm search repo openldap

kubectl create namespace iam

helm show values openldap/openldap-stack-ha > infra/ldap/values.yaml

helm upgrade --install openldap openldap/openldap-stack-ha -n iam -f infra/ldap/values.yaml --create-namespace

kubectl cp infra/ldap/ldap-bootstrap.ldif   iam/openldap-0:/tmp/ldap-bootstrap.ldif

kubectl exec -n iam -it openldap-0 -c openldap-stack-ha -- \
  ldapadd \
  -H ldap://127.0.0.1:1389 \
  -x \
  -D "cn=admin,dc=lakehouse,dc=local" \
  -w 'Not@SecurePassw0rd' \
  -f /tmp/ldap-bootstrap.ldif