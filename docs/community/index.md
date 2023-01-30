# Community Driven Platforms

We are changing the way of thinks about platform and operations. Centralized teams doesn't scale and are inefficient on resources and persons use as the team growth.

No matter how big the team are, they are always becomes a bottle neck, one way to avoid this is spread the knowledge and responsabilities across the entire organization.

We choose and organic approach. We use a product approach **based on community governance (inner source)**. The platform team is designed as a **bootstrapping team** responsible to ignite the products and start the moderators community. We start with a **"[Founder Leader](https://www.redhat.com/en/blog/understanding-open-source-governance-models)"** governance approach, but we aim to evolve to a **"[Do-ocracy](https://www.redhat.com/en/blog/understanding-open-source-governance-models)"** governance approach.

_"Open source projects adopting the "do-ocracy" governance model tend to ignore formal and elaborate governance conventions. Instead, they insist that those who do the work are those who make the decisions. In other words: In a do-ocracy, participants who invest the most time, energy, and attention in specific aspects of the project have the most authority and influence over decisions in those areas of the project. Peer review is common under this model, but individual contributors tend to retain de facto decision-making power over project components they've worked on closely. For this reason, some do-ocracies will claim to have no governance at all, but for most do-ocracies, the governance model is simply implicit in the everyday interactions of project members. As a result, joining them can be difficult and intimidating for newcomers who may not immediately know how to participate or seek approval for their contributions."_ - [Understanding open source governance models](https://www.redhat.com/en/blog/understanding-open-source-governance-models)

Based on the definition above, we have our definition of do-ocracy.

To ensure the continuous growth of the products and services provided by the platform, we propose a minimum centralized team (bootstrapping team), where principal doers are concentrated, and, each member of the team is part of a cross-organization rotation structure, ensuring that everyone in the organization has the time and focus to work in the platform, and, just like do-ocracy, every participant who has time or needs can and should contribute directly to the platform, whether or not they are part of this team at the time.

```kroki-mermaid
flowchart TB
  subgraph CentralizedTeam
  TT1(Temp team member 1)
  TT2(Temp team member 2)
  TT3(Temp team member 3)
  end
  subgraph Product team A
  TT4(Temp team member 4)
  end
  subgraph Product team B
  TT5(Temp team member 5)
  end
  subgraph Product team C
  TT6(Temp team member 6)
  end
  TT4 -.->|Eventual rotation| TT1
  TT5 -.->|Eventual rotation| TT2
  TT6 -.->|Eventual rotation| TT3
  TT1 -.->|Eventual rotation| TT4
  TT2 -.->|Eventual rotation| TT5
  TT3 -.->|Eventual rotation| TT6
  NT(New team member) --> CentralizedTeam
```

## How to become a do-ocracy?

The problem with a do-ocracy governance is that is intimidating if the community is not mature enough, and if we do not present a strategy for new incomers.

> Our ideal case is that exists a majority of mature teams so any proposal that add value to the organization, quickly will attract contributors and maintainers from the teams and is not needed keep growing a centralize team.

On our current organization, the level of maturity is not enough to bootstrap a do-ocracy naturally. We decide to start with a Founder Leader approach. To achieve evolve to a do-ocracy effectively, we aim to incorporate moderators and contributors to our products as **platform team members for a limited period of time** to share a common culture and then distribute the new moderators and contributors on the teams that require the capacity and capabilities to start working for the new team as team member but being active participants of the community.

> Our Goal is maintain the platform team as small as possible and distribute the maintainers and contributors on the teams that needs gains maturity to be part of the community.

## Our Hypothesis

_If we attract (hire) and distributed enough capable persons we will reach a level of organization maturity that we allow us release the moderation control and drop most of our "[Benevolent Dictators](https://www.theatlantic.com/technology/archive/2014/01/on-the-reign-of-benevolent-dictators-for-life-in-software/283139/)" to let the community organic take decisions._

## Implementation

The implementation consider:

**Stage 1:** Hire the founding benevolent dictators (Founders).

**Stage 2:** Bootstrap principles, guidelines and practices (handbooks).

**Stage 3:** Deliver first Road Map and core products.

**Stage 4:** Hire maintainers and contributors as team members.

**Stage 5:** Attract maintainers and contributors from teams with high maturity.

**Stage 6:** Create a first cross-organization rotation structure.

**Stage 7:** Distributed maintainers and contributors.

**Stage 8:** Keep the wheel spinning and LET THE COMMUNITY CHANGE THIS DOCUMENT!!!
