# Data Team - Handbook

> This document is a collaborative guide, and its principles should be used as a mandatory
> reference to any decision related to this scope. It is an open document and could be updated
> by any interested party or related to the role within this scope.

This document aims to provide high-level guidance on how the data team works, its principles
and adopted practices.

Our principal mission as a data team is the **democratization of the data**. Allowing anyone to
explore and exploit them in a **free, secure, and seamless** way, always focus on **self-service and
decentralization**.

## Participants

- **Rodrigo Navarro** · [rodrigo.navarropinto@cencosud.cl](mailto:rodrigo.navarropinto@cencosud.cl)

**What to read Next?**

- [Reference Architecture](reference-architecture.md)
- [Tactic](tactic.md)

## Principles

- **Data as a product**, is a core component at the company and should be treated as such.
- **Cloud-first**, every system, platform, and tool should have to be deployed on the cloud.
- **Stream first**, as the main integration model, we empower the use of streaming platforms to expose
  data raw, pre-processed, or processed.
- **Open source first**, our first option is always an open-source project, also we aim to actively
  collaborate within the community.
- **We aren't data owners**, we provide guidelines, platforms, tools, and flows that help you to build
  data products, ml models, and more.
- **Infrastructure as code**, every platform, system, and tool should have to be deployed using an **IaC**
  approach without exception.
- **Live documentation over static documentation**, we aim the use of diagram as code, documentation as
  code, developer portals, and so on.
- **Manual tasks at most one time**, we aims the automation for repetitive tasks.
- **Continuous verification over normative**, every guideline is willing to changes.
- **Shift left in processing**, we empower the processing of data closer to its creation.
- **Citizen developers by default**, aim to provide seamless systems focused on empowering our citizen
  developers.
- **Behavior over solution**, we are focus on the problem not on a specific solution.
- **Legacy as first class citizen**, each legacy system must be considered as an active part of the ecosystem,
  adopt it and evolve it according to the case.

## Why?, What we address?, Who?

Our focus is not technology, our focus is encourage a **data mindset** on the organization. Our main purpose is:

**ANSWER QUESTIONS**

and our focus is:

**THE DECISION MAKER**

For our culture, _we support the decision maker to answer questions_, but is the decision maker who know the business and who make the questions and declare the Hypothesis. In this context is important to consider:

- We avoid any Bias
- We **DO NOT** make questions and Hypothesis on behalf the decision maker

> In the case that the Decision Maker is not able to make questions, **WE HELP IT TO ARISE QUESTIONS** using unsupervised algorithms to present not biassed correlated data.

For us, a data mindset encourage the scientific method on all pur decisions:

- Hypothesis
- Prediction
- Testing
- Analysis

> Is mandatory that the prediction step deduces the logical consequences of the hypothesis before the outcome is known and is Decision Maker responsibility. **We do not star working without a unbiased decision maker hypothesis and prediction.

To allow generate hypothesis and prediction we encourage the use of sandbox for experimentation.

And finally, we aim for:

**USEFUL RESULTS**

so, avoid biases is fundamental in our culture, mindset and technology.

### Data Classification and Quality

To add value to our decision makers, the results must be usable. This means:

- The data use must follow laws and regulation
- The data must be properly cleaning
- The data must be properly labeled


> We should aspire to the most demandant international rules and regulations. Is not practical be backward compliance if some regulations is demanded. The focus behind data lake is make all data avaliable and usable.
### Correlation and Causality

The goal is answer questions, so **we need go beyond correlation** and allow test causality. To test causality, we can enable A/B testing, but, with a data mindset as principle, we must allow test causality based on data. For this we need provide **huge amount** of data to allow data split with real randomness. With this goal on mind, we must allow ingest any data as possible without lost and **encourage teams to send every single event.**

### Cognitive Biases

To generate useful results que need to be careful avoiding cognitive biases. The mos important bias to avoid is **CONFIRMATION BIAS**
#### Confirmation Bias

> _"Confirmation bias is the tendency to search for, interpret, favor, and recall information in a way that confirms or supports one's prior beliefs or values.[1] People display this bias when they select information that supports their views, ignoring contrary information, or when they interpret ambiguous evidence as supporting their existing attitudes. The effect is strongest for desired outcomes, for emotionally charged issues, and for deeply entrenched beliefs. Confirmation bias cannot be eliminated entirely, but it can be managed, for example, by education and training in critical thinking skills."_ - [Wikipedia](https://en.wikipedia.org/wiki/Confirmation_bias)

#### Suvivorship Bias

> _"Survivorship bias or survival bias is the logical error of concentrating on the people or things that made it past some selection process and overlooking those that did not, typically because of their lack of visibility. This can lead to some false conclusions in several different ways. It is a form of selection bias. Survivorship bias can lead to overly optimistic beliefs because failures are ignored, such as when companies that no longer exist are excluded from analyses of financial performance. It can also lead to the false belief that the successes in a group have some special property, rather than just coincidence (correlation "proves" causality). For example, if three of the five students with the best college grades went to the same high school, that can lead one to believe that the high school must offer an excellent education when, in fact, it may be just a much larger school instead. This can be better understood by looking at the grades of all the other students from that high school, not just the ones who made the top-five selection process."_ - [Wikipedia](https://en.wikipedia.org/wiki/Survivorship_bias)

## How we work

We are a **cross-product** team and work closely with each one, providing data capabilities within teams to
help them create, support, and develop their data products.

We are a combination of Data Engineers, Data Science and DataOps with an strong Software Engineer background.

We beleive that every piece of software we develop have to come with high quality and security standards.

We work based on the definition of [Communuity Driven Platforms](../Community/community-driven-platform.md).

## Data strategy

As data team, our primary mission is the **democratization of the data**, with this in mind, we create a strategy based in 4 blocks:

- Integration
- Experimentation
- Processing
- Consumption

### Integration

Most of the cases, topically involve structured or semi structured data, with this assumption, we encourage the use of event brokers to store and expose data through a continuous data stream, even when this data comes directly from an api, application or another system or if it's comes from a database, or file system. This provide a simple and unique integration point with all the advantage of an event broker, like multiple consumers of data raw or pre-processed, time period retention, useful when you need to re process or create metrics, and so many other features.

```kroki-mermaid
flowchart LR
    DB(Database) -->|push to| EB(Event Broker)
    APP(Some application) -->|push to| EB
    SVC(Some Service) -.->|push to| EB
    FS(File system) -.->|push to| EB
    EB -.->|pull| SC(Service consumer)
    EB -.->|pull| AC(File system)
    EB -.->|pull| DC(Domain consumer)
    EB -.->|pull| SO(So on)
    EB -->|Required| DL[Data lake]
    style DL fill:#f66
    style EB fill:#999
```

**Technology proposed:**

- Apache Kafka and its ecosystem (Kafka connect, Kafka streams, etc).

## Experimentation

It is a fact that many people in the organization needs to experiment with data, this is one the focus of the democratization,  mainly Data Scientist, with this in mind, we proposed a sandbox based on a Big Data processing system, isolated, that could handle large queries, datasets and complex scenarios, connected directly to a data lake.

```kroki-mermaid
flowchart LR
    DB(Database) -->|push to| EB(Event Broker)
    EB -->|Required| DL[Data lake]
    DL --> BD(Big data system)
    U[User] -->|query| BD
    style DL fill:#f66
    style EB fill:#999
```

**Technology proposed:**

- Google Big query.

## Processing

In order to improved data sets for consumption, based on the concept of data products, we proposed a multi level processing systems, we empower the use of near real time data (hot data) to pre process, clean and enrich data and datalakes for reprocessing and pre propcessing of historycal data.

```kroki-mermaid
flowchart LR
    DB(Database) -->|push to| EB(Event Broker)
    EB -->|pull| PS(Pre processing system)
    PS -->|push| EB
    EB -->|Required| DL[Data lake]
    DL --> PS2(Pre processing system)
    PS2 --> DL
    style DL fill:#f66
    style EB fill:#999
```

**Technology proposed:**

- Apache Beam over Dataflow.
- Kafka Streams, Faust.
- Spark, Flink.

## Consumption

Based on the concept of Data Mesh and the requirement of create a consumption layer with government, we propose the use of multi source query system, optimized for end user, starting from the assumption that every dataset expose on this layer is optimize and created using the processing tools.

```kroki-mermaid
flowchart LR
    DB(Database) -->|push to| EB(Event Broker)
    EB -->|pull| PS(Pre processing system)
    PS -->|push| EB
    EB -->|Required, pull| DL[Data lake]
    DL --> PS2(Pre processing system)
    PS2 --> DL
    DL -->|pull| QS(Query system)
    U(user) --> QS
    D(domain) --> QS
    U2(user) --> EB
    D2(domain) --> EB
    style DL fill:#f66
    style EB fill:#999
    style QS fill:#33f
```

**Technology proposed:**

- Dremio.
