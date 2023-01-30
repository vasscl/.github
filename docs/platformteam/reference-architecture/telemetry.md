# Telemetry

> **What to read previously?** - [Reference Architecture](index.md)

As telemetry we consider 4 kind of instrumentation:

- Logs
- Metrics
- Trace
- Baggage

> :exclamation: **IMPORTANT** Every time that instrumentation is considered **MUST** be analyzed and implemented the correct type. For example, avoid use logs for metrics or tracing. The reason is that proper platform resources will be implemented for each case adn wrng decision could lead to platform issues like latency.
