# Real Time

> **What to read previously?** - [Reference Architecture](index.md)

When we talk about real time we refer to the wider definition useful on distributed computing:

> Real-time or real time describes various operations in computing or other processes that must guarantee response times within a specified time (deadline), usually a relatively short time. A real-time process is generally one that happens in defined time steps of maximum duration and fast enough to affect the environment in which it occurs, such as inputs to a computing system.

For external integration, RPC APIs (REST) are the best choice to expose services and data, but for internal services asynchronous and event based communication should be preferred to take advantage of serverless computing and allow distribution. Still RPC APIs are the best solution is guaranteed sub-seconds responses is mandatory. To choose the best solution we recommend start defining the real-time guarantee response times and use the next guidance:

1. **Sub-Second response time:** RPC technologies like gRPC or REST (http2) running on stateless micro-services (PaaS or k8s) are best suited
2. **Second response time**: Serverless lambda functions like GCP Cloud Functions or k8s OpenFaaS are best suited. Prefer Event triggers over RPC or command triggers to execute functions and communicate between them.
3. **Minutes response time**: Container as a Service like ACI or Fargate running on micro-vms are best suited to run on minutes or more guaranteed workloads. Consider that Google do not have a Container as a Service offer but Google compute instance actually are similar on design as Container as a Service AWS and Azure offers and can be used on the same way.

> :information_source: **INFO** A good pattern to run tasks is launch GCP compute instances based on events (pub/sub, cloud schedule or http triggers) and Cloud functions. A GCP compute instance is created on 30 seconds, can be initialized with a Docker Image and can be scripted to be destroyed itself after finish the task. Even can be created cluster to process complex workloads. This approach is very powerful, secure and resource efficient.
