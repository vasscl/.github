# Challenge 1

## Operational safety and static security

Our first challenge is about to be compliance on security and strength our operational continuity.

|Team|Hardened images|Secret manager|Challenge 3|Challenge 4|Challenge 5|Extras|
|---|---|---|---|---|---|---|
|Arcus    |0.4|0|||||
|Shopping |1|0|||||
|Janus    |0|0||||0.4|
|Pactolus |0.7|0|||||
|Pim      |0|0|||||

**The winners**

- Challenge Hardened images #1 - Shopping Team 02/03/22
- Challenge Hardened images #2 - Pactolus Team 02/03/22
- Challenge Hardened images #3 - Arcus Team 02/03/22

Extras Challenge Hardened images

Janus team collaborate with the ecosystem providing a way to inyect configuration on deployment using init containers. To learn more review the [document](../guides/environment-configuration.md).

## Secret manager

As part of our strategy to strengthen the security, we provide a new service, [Vault](https://www.hashicorp.com/products/vault) which is a tool with a lot of functionalities that help us to manage the complexity of secret management. To know how to use this service, read the [guide](https://github.com/Cencosud-X/handbooks/blob/main/EN/Platform-team/guides/vault.md).

The team that implements this service in its development cycle first, this includes: deployment of artifacts using the agent and use Vault to get consul token on pipelines, will win the challenge.

## Hardened images

The idea is to start using only hardened images for our building and running process, as platform team we provide a [repository](https://github.com/Cencosud-X/x-images) where those images are building and signing, it is open to collaboration, so anyone can register new images.

### How to browse images on registry

To list the available images on our repository you have to:

Set the project

```shell
gcloud config set project cencosudx
```

List images on golden or build

```shell
gcloud container images list --repository us.gcr.io/cencosudx/golden
... or
gcloud container images list --repository us.gcr.io/cencosudx/build
```

Inspect available tags, replace <IMAGE-NAME> for the name of the image you want to inspect

```shell
gcloud container images list-tags us.gcr.io/cencosudx/golden/<IMAGE-NAME>
```

You have to see something like this

```shell
gcloud container images list-tags us.gcr.io/cencosudx/golden/node
DIGEST        TAGS                                                                         TIMESTAMP
78e68a7ce93a  v14                                                                          1969-12-31T21:00:00
ce679ba6634d  v16                                                                          1969-12-31T21:00:00
53d4a561c9b2  sha256-78e68a7ce93a482b4df3d76a2500b8e2f4292e35c8985289a2f2e2f773bf94c8.sig
f976e0b3361f  sha256-ce679ba6634d79f84baf2f9390bc6ce14ffa30a442edaa0d8518f96157885d5f.sig
```

The team that implement this images in their Dockerfiles first, and it is verified by the platform team, will win the challenge.
