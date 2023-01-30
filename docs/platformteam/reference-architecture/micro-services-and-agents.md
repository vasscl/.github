# Micro-Services, Actors and Agents

> **What to read previously?** - [Reference Architecture](index.md)

## Services Communication

The communication  to share data and commands between services is fundamental to achieve high availability, security, availability and cost efficiency. The next guide **MUST** be preferred when communication is selected:

|  Type | Client | Scale | Solution |
|---|---|---|---|
| Internal | Service | < tenths micro-service | gRPC / events |
| Internal | Service | > tenths micro-service| events |
| External | Service | < millions tuples | API REST |
| External | Service | > millions tuples | Batch/Storage |
| External | App     | * | GraphQL  |
| External | App     | * | GraphQL  |

> :exclamation: **IMPORTANT** Every service **MUST** be a good citizen and protect calls to other services using techniques like circuit breaking, rate limit, local cache, etc.

### Patterns

#### External APIs with large data

When large data set is needed to transfer, is not recommendable use http to transfer data. The best solution is use cloud Storages technologies to transfer data. The next patter is useful to transfer large data sets:

1. API call request transfer with webhook to receive updates
2. Service create a cloud storage token with expiration and reserve a unique file name
3. The requester receive the token and upload the dataset to the file
4. The service listen cloud storage events and validate and load data when is uploaded. Any info like errors or success messages will be sent to the webhook
5. The requester listen the webhook to update status

> The same pattern can be used internally changing the webhook with a pub/sub topic.
