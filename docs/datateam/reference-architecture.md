# Architecture

Architecture are based on the needs of our products teams and it is replicated by domain.

```kroki-mermaid
flowchart TD
  api[Api]
  teamA[Product team A]
  dbA[(Product team A DB)]
  queue[[Event stream]]
  storage((Data lake))
  preProcessor[/Metrics generator\]
  warehouse[(Data warehouse)]
  storage[(Data lake)]
  dashboard(Dashboards)
  user((User))
  sink[Data Sink]

  teamA -->|events| queue
  dbA -->|CDC| queue
  queue -->|events| preProcessor
  queue -.->|metrics| domain
  queue -->|metrics & cdc| sink
  preProcessor -->|metrics| queue
  sink -->|all data| storage
  sink -->|metrics & cdc| warehouse
  warehouse --> dashboard
  dashboard --> user
  warehouse --> api
  api -.-> domain

  style queue fill:#f66
```

## Technologies

- **Event stream:** Confluent Kafka.
- **Data lake:** Google Cloud Storage.
- **Data warehouse:** Google BigQuery.
- **Data sink:** Kafka connect.
- **Metrics generator:**
  - [Faust streaming library](https://faust.readthedocs.io/en/latest/).
