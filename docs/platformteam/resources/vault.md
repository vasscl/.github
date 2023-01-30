# Using Vault for secrets

Hashicorp [Vault](https://www.hashicorp.com/products/vault) defines itself as a tool for "Manage secrets and protect sensitive data. Create and secure access to tokens, passwords, certificates, and encryption keys.".

## Why Vault

As a platform team, security is a native part of our ecosystem, we select Vault as a tool for managing secrets and encryption as a service because of the agility and extensibility that offers. It is possible to connect to a Cloud provider and use dynamics secrets, as well as several other kinds of resources, it is possible to create custom clients and extend this behavior across our own products and services too.

## Reference architecture

```kroki-mermaid
flowchart LR
  user((User))
  vault[Vault]
  consul[Consul]
  github[Github]
  terraform[Terraform]
  k8s1(K8S cluster A)
  k8s2(K8S cluster B)
  k8s3(K8S cluster C)
  cloud[Cloud provider]

  vault -->|Dynamic secrets| cloud
  user -->|Request access and interact| vault
  vault -->|Authorize| github
  github -->|Actions request secrets| vault
  vault -->|Request temp client token| consul
  k8s1 -->|Request secrets and encryption| vault
  k8s2 -->|Request secrets and encryption| vault
  k8s3 -.->|Request secrets and encryption| vault
  terraform -->|Inject secrets| vault
  terraform -->|Inject configuration| consul

  style github fill:#333,color:#fff,stroke:#333
  style vault fill:#000,color:#fff,stroke:#000
  style consul fill:#fff,color:#ff0071,stroke:#fff
  style user fill:#9de0e9,color:#333,stroke:#fff
  style k8s1 fill:#0070ff,color:#fff,stroke:#fff,stroke-width:4px;
  style k8s2 fill:#0070ff,color:#fff,stroke:#fff,stroke-width:4px;
  style k8s3 fill:#0070ff,color:#fff,stroke:#fff,stroke-width:4px;
  style terraform fill:#a000ff,color:#333,stroke:#a000ff
  style cloud fill:#0070ff,color:#fff,stroke:#fff
```

Vault is connected to our **Github** account, this links your **Github** profile with your Vault kv store.

## How to use it

### Connect from your local

You need [install Vault](https://www.vaultproject.io/). Vault is connected to our Github account so, the only thing you need to connect to it, is a personal token with "read:org" permissions. Read the [documentation](https://docs.github.com/es/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token) to create a personal token

With your personal token you can log in to vault:

```shell
export VAULT_ADDR=https://vault.cencosudx.xyz
vault login -method=github -path=github/cencosudx token="<YOUR-PERSONAL-TOKEN>"
```

### Connect from a cluster

All the k8s clusters are already connected and authenticated to Vault through a Vault agent, this uses a service account to relate your Vault KV store with the pod that wants to use the secrets.

To know more about the Vault agent, read the [documentation](https://www.vaultproject.io/docs/platform/k8s/injector).

> For CL teams the nomemclature for TEAM_NAME is `cl-<TEAM>`.

You need to configure:

```yaml
# a service account with...
---
apiVersion: v1
kind: ServiceAccount
metadata:
  name: <TEAM_SA_NAME>-sa
  namespace: <TEAM_NAMESPACE>
```

What is in it:

**name** This have to be the name of the service account resgistered for the team in Vault. Contact with your platform team for more information.
**namespace** The namespace where is gonna be used.

```yaml
# add vault annotations to your deployment
apiVersion: apps/v1
kind: Deployment
metadata:
  name: test-tools
  namespace: <TEAM_NAMESPACE>
spec:
  selector:
    matchLabels:
      app: test-tools
  replicas: 1
  template:
    metadata:
      labels:
        app: test-tools
      annotations:
        vault.hashicorp.com/agent-inject: 'true'
        vault.hashicorp.com/role: '<TEAM_NAME>-cluster-staging-1'
        vault.hashicorp.com/auth-path: "auth/cluster/staging-1"
        # ensure that vault init container run first
        vault.hashicorp.com/agent-init-first: 'true'
        vault.hashicorp.com/agent-inject-secret-config: '<TEAM_NAME>-kv/test'
        vault.hashicorp.com/agent-inject-template-config: |
          {{ with secret "<TEAM_NAME>-kv/test" }}
            {{ range $k, $v := .Data.data }}
              export {{ $k }}={{ $v }}
            {{ end }}
          {{ end }}
        # to import consul token
        vault.hashicorp.com/agent-inject-secret-consul: 'cl/consul/creds/<TEAM_NAME>-role'
        vault.hashicorp.com/agent-inject-template-consul: |
          {{ with secret "cl/consul/creds/<TEAM_NAME>-role" }}
              export CONSUL_HTTP_TOKEN={{ .Data.token }}
          {{ end }}
    spec:
      serviceAccountName: <TEAM_SA_NAME>-sa
      containers:
      - name: master
        image: devops-tools:latest
        resources:
          requests:
            cpu: 100m
            memory: 100Mi
```

What is in it:

**spec.template.spec.serviceAccount** The service account created in the section above.
**spec.template.metadata.annotation** Custom agent annotation to configure vault. To know more about annotations, read the [documentation](https://www.vaultproject.io/docs/platform/k8s/injector/annotations)

Possible values for annotations

| Annotation | Values | Required |
|---|---|---|
|vault.hashicorp.com/agent-inject|true|true|
|vault.hashicorp.com/role|<TEAM_NAME>-cluster-<CLUSTER_NAME>|true|
|vault.hashicorp.com/auth-path|auth/cluster/<CLUSTER_NAME>|true|
|vault.hashicorp.com/agent-inject-secret-<FILE_NAME>|<TEAM_NAME>-kv/<PATH>|true|
|vault.hashicorp.com/agent-inject-template-<FILE_NAME>|Vault template|false|


### In your code

Vault agent runs an init container and mounts a shared volume where the secret is written to in the path `/vault/secrets/<FILE_NAME>`.

```shell
# on your entrypoint.sh using the template on the example
# using annotation vault.hashicorp.com/agent-inject-secret-secret-env
...
if [ -f "/vault/secrets/secret-env" ]; then
  source /vault/secrets/secret-env
fi
...
```

## Secret engines

### Consul

By default [Consul](https://www.consul.io) secret engine is already installed, and you can request a dynamic consul token using Vault. This could be from an init container, CI/CD pipeline and more.

```shell
vault read cl/consul/creds/<TEAM_NAME>-role
# or
vault read -field=token cl/consul/creds/<TEAM_NAME>-role
```

## Tutotials

- [Your first secret](https://learn.hashicorp.com/tutorials/vault/getting-started-first-secret).
- [Versioning secrets](https://learn.hashicorp.com/tutorials/vault/versioned-kv).
- [Using Vault with Terraform](https://learn.hashicorp.com/tutorials/terraform/secrets-vault).
