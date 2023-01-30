# Security

> **What to read previously?** [Documentation definitions](documentation.md)

## Dev First Approach

We are empowering teams in defferent areas, now more than ever the developer is the principal actor, from coding, deploying infrastructure, to operate it in production, that's why we are getting the approach of [Dev First security](https://about.gitlab.com/topics/devsecops/what-is-developer-first-security/) considering security aspects from the first line of code.

## Pro active ecosystem

In terms on pro-active security, we beleive that the first step is make our security flaws visible, for this, we use the Git repository as base for running security checks and make it visibles trought the developer portal.

```kroki-mermaid
flowchart LR
  user((User))
  git[Git]
  portal[Developer portal]
  codescan(Code scan)
  leaks(Secret leaks)
  dependencies(Dependencies scan)

  user -->|Push event| git
  git -->|trigger| codescan
  git -->|trigger| leaks
  git -->|trigger| dependencies
  codescan -.->|report| portal
  leaks -.->|report| portal
  dependencies -.->|report| portal

  style github fill:#333,color:#fff,stroke:#333
```

## Scope

- Default definitions
- Git repository
- Docker images
- Secret management

### Default definitions

- Use https by default
- API connections using JWT
- No exposure secrets in repositories
- Use SSL to connect to external services

### Git repository

We rely on git security primarily on Github using the [advanced security tools](https://docs.github.com/en/enterprise-server@3.5/get-started/learning-about-github/about-github-advanced-security). Additional to this we encourage the use of the [Pre-commit](https://pre-commit.com) tool to run in your local before to commit your changes.

> You can find sample pre-commit files for your proyects [here](guides/pre-commit.md).

### Docker Images

To ensure the use of security images, we provide an internal container registry per cloud, and provide a tool called [Trustr](https://github.com/Cencosud-X/trustr) to build, inspect, scan and sign images.

We encourage the build and of 3 types of images:

- **Build**: base images used in your building process as first steps on your Docker file like alpine, ubuntu, and more.
- **Golden**: commonly [distrolles](https://github.com/GoogleContainerTools/distroless) images, ready to use as base for run your application in the last step of your Docker file.
- **Custom**: this is your application image built using build and golden images as base.

> You can find and contribute to base and golden image definitions and building process in this [repository](https://github.com/Cencosud-X/x-images).

The next rules must be follow for any Docker Image:

1. Only use verified images from Cencosud or buil it yourself using [Trustr](https://github.com/Cencosud-X/trustr)
2. Try to run one process per image (remember that a pod can run more than one image)
3. Do not run containers as root users (rootless mode)
4. Utilise user namespaces
5. Drop capabilities if they're not needed
6. Do not mount the Docker unix socket in your containers (/var/run/docker.sock)
7. Take care to protect /var/run/docker.sock with appropriate filesystem protects
8. Use Multi Stage Builds to reduce image size

### Secret management

Our default secret management system is [Vault](https://www.hashicorp.com/products/vault) and we are in continuous growth of features, this is our main touch point for every interaction with the ecosystem. To know more how to acces and use, vault visit [using vault](guides/vault.md).

Vault features:

- Access secret key-value store
- Dynamic token to access to Configuration management Consul
- Dynamic access to kubernetes clusters

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

### What to read Next?

- [Reference architecture](reference-architecture/index.md)
- [Multi-Cloud strategy](multi-cloud.md)
- [Resources](resources/index.md)
