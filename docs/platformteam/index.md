# Platform Team - Handbook

> This document is a collaborative guide, and its principles should be used as a mandatory
> reference to any decision related to this scope. It is an open document and could be updated
> by any interested party or related to the role within this scope.

This document aims to  provide high-level guidance on how the platform team works, its principles
and adopted practices.

## What we do?

We bring **tools and services** to the development teams to **speed up their development cycle** and provide a secure, reliable, and high-quality execution environments where they can monitor and operate their final products always within a self-service approach.

## Our principles

- Global first.
- Event first.
- Inner Source collaboration.
- Legacy as first class citizen.
- Cloud-first, every system, platform, and tool should have to be deployed on the cloud.
- Open source first, our first option is always an open-source project, also we aim to actively
  collaborate within the community.
- Infrastructure as code, every platform, system, and tool should have to be deployed using an IaC
  approach.
- Live documentation over static documentation, we aims the use of diagram as code, documentation as
  code, developer portals, and so on.
- Manual tasks at most one time, we aims the automation for repetitive tasks.
- Continuous verification over normative, every guideline is willing to changes.
- Behavior over solution, we are willing to changes in pro to provide the same behavior no matter the
  current solution.
- TVP Thinnest Viable Platform, have exactly what we need, nothing more.
- End user metrics over technical metrics.
- Native security from scratch with Zero Trust.
- Shift left in security, empowering teams to implant security from day one on their products. We
  provide a seamless environment where to do it.
- DevFirst Security, we giving to the development teams the tools to secure their product from an application and developer perspective.
- Analytics as medium for causal and predictive inference.

## How we work

We are a **cross-product** team and work closely with each one, providing SRE capabilities within teams to
help them create, support, and develop their products.

We are a combination of SRE, DevOps, and DevSecOps with an strong **Software Engineer** background.

We beleive that every piece of software we develop have to come with high quality and security standards.

We work based on the definition of [Communuity Driven Platforms](../Community/community-driven-platform.md).

### Team Members

- **Rodrigo Navarro** · [rodrigo.navarropinto@cencosud.cl](mailto:rodrigo.navarropinto@cencosud.cl)
- **Ricardo Sandoval** · [ricardo.sandoval@externos-cl.cencosud.com](mailto:ricardo.sandoval@externos-cl.cencosud.com)
- **Nicolas Georger** · [nicolas.georger@externos-cl.cencosud.com](mailto:nicolas.georger@externos-cl.cencosud.com)
- **Diego Mondini** · [diego.mondini@externos-cl.cencosud.com](mailto:diego.mondini@externos-cl.cencosud.com)
- **Victor Santos** · [victordanner.gama@cencosud.com.br](mailto:victordanner.gama@cencosud.com.br)
- **Jorge Loayza** · [jorgeantoni.loayzasoloisolo@externos-pe.cencosud.com](mailto:jorgeantoni.loayzasoloisolo@externos-pe.cencosud.com)

### Team organization

```kroki-mermaid
flowchart TB
    subgraph Chile
    DM(Diego Mondini)
    end
    subgraph Brasil
    VS(Victor Santos)
    end
    subgraph Core Regional
    NG(Nicolas Georger)
    end
    subgraph Core Plataform
    RN(Rodrigo Navarro)
    RS(Ricardo Sandoval)
    end
    subgraph Colombia
    TBD1(TBD)
    end
    subgraph Argentina
    TBD2(TBD)
    end
    subgraph Peru
    JL(Jorge Loayza)
    end
    end
```

## Contact and support

- Discord voice channel **Plataforma**
- Discord text channel **Plataforma-text**
- Discord **production incidents** channel **production-incidents**
- Microsoft Teams chat [Soporte plataforma](https://teams.microsoft.com/l/channel/19%3af530dd3d6f2947a08688e912a0690f13%40thread.tacv2/Soporte%2520plataforma?groupId=a5c53460-55f1-401b-9e74-01c35644c882&tenantId=a50762c4-c5ad-413a-a05e-9ffe15752882)
- [Feedback form](https://forms.office.com/Pages/ResponsePage.aspx?id=xGIHpa3FOkGgXp_-FXUogmA0xaXxVRtAnnQBw1ZEyIJURTZQUVNSTDVMNFZZR0tYUEdTVk5SNURMVyQlQCN0PWcu)

## Our Roadmap

```kroki-mermaid
gantt
  title Roadmap Plataforma
  axisFormat %m

  Q1           :milestone,q1, 2022-02-01, Q1
  Q2           :milestone,q2, 2022-04-01, Q2
  Q3           :milestone,q3, 2022-07-01, Q3
  Q4           :milestone,q4, 2022-10-01, Q4

  Manejo de cuentas automatizados :done, 2022-04-01, 90d
  Definir modelo de costos de plataforma :done, 2022-04-01, 90d
  Implementar developer portal MVP :done, 2022-04-01, 90d
  Implementación Trsutr Deployr :active, 2022-04-01, 90d
  Implementar observabilidad de infra :active, 2022-04-01, 90d
  Definir estrategia de nube regional :active, 2022-04-01, 90d

  Implementar observabilidad de artefactos :not, 2022-07-01, 90d
  Implementar politicas en clusters :not, 2022-07-01, 90d
  Visibilidad de costos por producto :not, 2022-07-01, 90d

```

### What to read Next?

- [Documentation definitions](documentation.md)
- [Security definitions](security.md)
- [Reference architecture](reference-architecture/index.md)
- [Multi-Cloud strategy](multi-cloud.md)
- [Resources](resources/index.md)
