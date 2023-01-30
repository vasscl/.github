# Cluster Internal Components

Our GKE cluster are deployed using IaC, you can check the source in the [x-cluster](https://github.com/Cencosud-X/x-clusters) repository

## Components

- [Cert-manager](https://cert-manager.io): Cloud native certificate management. X.509 certificate management for Kubernetes and OpenShift.
- [Vault Agent](https://www.vaultproject.io/docs/agent): Vault Agent allows easy authentication to Vault in a wide variety of environments.
- [Kong Gateway](https://docs.konghq.com/gateway/latest/): Kong Gateway is a lightweight, fast, and flexible cloud-native API gateway. An API gateway is a reverse proxy that lets you manage, configure, and route requests to your APIs.
- [Flux CD](https://fluxcd.io): Flux is a set of continuous and progressive delivery solutions for Kubernetes that are open and extensible.
- [External DNS](https://github.com/kubernetes-sigs/external-dns): ExternalDNS synchronizes exposed Kubernetes Services and Ingresses with DNS providers.
- [Instana Agent](https://www.instana.com): Observablity and Monitoring for Kubernetes.
