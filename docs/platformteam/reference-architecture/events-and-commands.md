# Event Strategy

> **What to read previously?** - [Suppported stack](stack.md)

To correctly choose technology to sent messages is important agree on the difference between a command and a event:

- Streams represents a group of ordered events.

- Events represent a past, something that already happened and can’t be undone.

- Command represent a wish, an action in the future which can be rejected and should contains all the parameters needed it to perform the action.

> To review how create topics on our confluent kafka cluster, go [here](https://github.com/Cencosud-X/manage-kafka-with-terraform)

An event has typically multiple consumers, but a command is addressed to only one. Commands are imperatives to a concrete action, typically the result of a user act. There’s usually no room for the called service to make any business decisions or reasoning about the action. Events are part of the business domain and its ubiquitous language, while commands are a pure technical concern.

Overall, commands encourage and are using on orchestration models and events on choreography models. Both are complementary, but events are fundamental because allow integration on distributed systems and support behaviors not yet considered.

A Event is immutable (persists), related with an entity and have an order that compose a stream that represents an entity related behavior behavior. The concept of order and stream is supported for few tools. Commands do not need order and also do not compose a stream. also persistence is not needed as far the delivery is guaranteed. Taking this on account, the next technologies are supported on CencosudX:

- Events: Kafka is mandatory
- Commands: The pub/sub pattern is enough and Kafka is supported as well GCP pub/sub.

> Kafka is an overkill to just implement pub/sub and commands, but giving that CencosudX use a managed solution, is the preferred solution due tha is OSS and supported on all clouds. Pub/Sub should be justify, for example, when its native integration with GCP services is useful.

#### Transactional Events topics

> To understand why we are making a difference between can be reviewed tne nex [article](https://www.confluent.io/blog/put-several-event-types-kafka-topic/).

When Transactional Events are used (order matter), the Topic should contain every event related with an entity behavior to take full advantage of Kafka goodness like transactions and Exactly Once delivery.

> :warning: **WARNING!** Avoid fine grained topics when events are used. The performance depend more on partitions than topics and [topic filter](https://kafka-tutorials.confluent.io/filter-a-stream-of-events/confluent.html) can be applied to get specific events.


Use the next structure:

```=
<country>.<domain>.<entity(noun)>.<behavior(root-verb)>.<version>
```

Example:

```
cl.parking.car.park.v1
```

#### Independent Events topics

When independent events are used (order do not matter) is not necessary keep al related event on the same topic. Use the next structure:

```
<country>.<domain>.<entity(noun)>.<past-participle-verb>.<version>
```

Example:

```
cl.parking.car.exited.v1
```

#### Commands and actions topics

When commands are used, the Topic name should correspond to the action verb of the command.

```
<country>.<domain>.<entity(noun)>.<simple-present-verb>
```

Example:

```
cl.payment.order.create.v1
```
