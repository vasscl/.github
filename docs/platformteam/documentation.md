# Documentation

> **What to read previously?** [Platform handbook](index.md)

There is not possible discussion that put on doubt the importance of documentation. Sometimes, its confused agility with lack of documentation and is not the spirit of Agile Manifest at all.

> "Finding the right level of documentation for your team can be quite a struggle. The Agile Manifesto calls for working software over comprehensive documentation, which is often wrongly interpreted as not having any documentation at all. There’s a lot of wiggle room between “no-documentation-at-all” and “everything-documented-to-a-tee”. Lightweight, easy to maintain documentation is the sweet spot you should aim for. Avoid going too heavy on the details, as keeping everything up to date will become a burden as your documentation grows. Include too little details and your documentation will not add value." - [Use Git and Markdown to Store Your Team’s Documentation and Decisions](https://xebia.com/blog/use-git-and-markdown-to-store-your-teams-documentation-and-decisions/)

The problem with maintain documentation is more related with how you find it, how you get the current state and how easy is to modify than with developers believing that is not important (or better **fundamental**).

Historically had been hard to search on distributed documentation and today, most of the solution focus on the user that needs to find and use the documentation and for that, the documentation is centralized to guaranteed proper search and read. This can looks reasonably, but is not. **To proper search and read documentation, is not necessary centralize the content creation, is enough to copy read-only documents and transform if its needed and let content creation responsibility to the owner**.

Centralize content creation rise the next issues:

- Constant doubt about the state of the documentation
- Easy to find for the user but hard to find for the content creator (kind of ironic)
- Hard to track changes, even when its supported by the content manager **
- Unnecessary lock-in features (we just need document, not create advertiser-level documents) *
- Unclear ownership

1. *Still you can send documents to professionals to be formatted if needed. Actually, could be an API, an interesting idea for a Startup ... or maybe exists?. For external user, you will need more quality. At least **Content as a Service** like [Contentful](https://www.contentful.com/) solve the CMS part, just remain a API for Quality Content Review.*

2. *The first problem with this is hwo complex the document format it is. Content manager systems encourage complex layouts. The second problem is source control version itself. Usually, the content manager version control are far from a SCM level like Git and also far from the tooling and community that you get from a SCM. The third is that git is more natural and frictionless for developers over a new version control system.*

---

## Documentation and Diagram as Code

Documentation should be and artifact of your code. Basically, its needed to cover the next aspects:

- Implementation
- Integration
- Bushiness Logic
- Architectural Decisions
- Behavioral Description
- General Description

**Implementation and integration** is mostly accepted for API and reference guides. In both cases, the best practice is literally let live on the code and most of the documentation portals accept it and support it through **Swagger** and **docs generators**. About the **business logic**, unit test are the best place to document it.

So, let focus on the rest of the documentation. This kind of documentation are usually wrote by the product team as free document with diagrams. To write this documentation with encourage the next principles:

- The documentation must be an artifact of the code
- The Diagrams must be and artifact of the code and he changes must be trackable
- Be agile, use the tools that you already have
- The documentation must live as close as possible to the owner (content creator)
- The documentation must be searchable

Follow this principles the next rules must be applied:

- Store the documentation on the same code repository that belong it
- Use Diagram as code (example: [mermaidjs](https://mermaid-js.github.io/mermaid/#/), [Diagrams](https://diagrams.mingrammer.com/))
- Use Markdown to document (frictionless if you store your code on )

The last principle, **"The documentation must be searchable"** following the principle of **"Be agile, use the tools that you already have"** should be implemented using natural git repository tools. Normally is used a developer portal, and this is not excluding and will be achieve pulling **READ ONLY** documentation using [BackStage](https://backstage.io/). The main strategy to allow user find documents will be engaged using **Big Code** concept.

> "Much in the same way as companies harness and process “big data” to extract insights from multiple large and complex data sets, “big code” is a concept that seeks to address the growing volume and variety of source code that businesses have to deal with across their development projects. Big code is chiefly concerned with the extent to which the amount of code; the variety and complexity of languages, systems, and tools; and increased expectations around speedy software cycles impact companies’ ability to function optimally. And this is where Sourcegraph is carving its niche." - [Sourcegraph raises $50 million to tackle ‘big code’ problems with universal search](https://venturebeat.com/2020/12/03/sourcegraph-raises-50-million-to-tackle-big-code-problems-with-universal-search/).

The best tool available for Big Code is [Sourcegraph](https://sourcegraph.com/). We are evaluating it, but search on any Markdown document is as easy as write: `file:\.md$ real time`. Sourcegraph automatically pull and index distributed content for you.

## Finding the right level of documentation

This is not an easy question. We follow the next rules to determine the right level and also, how complex is the documentation itself:

- Document implementation on code and use code generators tools
- Document APIs automatically using OpenApi Frameworks
- Document Business Logic using Unit Tests
- Document Behavior Description using BDD with [Gherkins](https://cucumber.io/docs/gherkin/) files on code
- Document decisions on code using ADR (Architectural Decision Records) with [adr-tools](https://github.com/npryce/adr-tools)

> Any adittional documentation is optional.

The last points are very important. **BDD** and **ADR** is and excellent practice to keep the documentation updated, tracked and minimal.

> To know more of documentation tools, visit [documentation tools](guides/documentation.md)

### What to read Next?

- [Security definitions](security.md)
- [Reference architecture](reference-architecture/index.md)
- [Multi-Cloud strategy](multi-cloud.md)
- [Resources](resources/index.md)
