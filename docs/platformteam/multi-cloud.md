# Multi-Cloud Strategy

> **What to read previously?** [Reference architecture](reference-architecture/index.md)

## Multi-Cloud based on workload and DRP

To understand the Multi-Cloud Strategy is necessary make the difference between High Availability and DRP/Backup.

**High availability (HA)** is a component of a technology system that eliminates single points of failure to ensure continuous operations or uptime for an extended period. High availability clusters are groups of servers that support business-critical applications that require minimal downtime and continuous availability.

**Disaster Recovery Plan (DRP)** is a series of steps an enterprise will take to resume normal business operations following a disaster that disrupts business operations. A DRP is similar to a Business Continuity Plan (BCP) except that a DRP is specially concerned with the steps taken after the disaster has struck, and with post-disaster kinds of recovery.

Multi-Cloud **won't be used to increase High Availability** due that multi-region cloud event are uncommon and do not justify the effort to maintain a functional replica active/active ot active/passive replica that also imply fit to the common minimun feature set between all used clouds. To increase HA will be used multi-zone and multi-region within the same cloud per workload.

Multi-cloud **will be used to support DRP** on special to maintain copy of sensible and critical data and configuration to prevent complete lost of application state.

Per workload use means that the cloud selection will be evaluated per workload and application could have workloads on different clouds if is justified. Platform team will ensure that proper communication with low latency will be in place between supported clouds.

### What to read Next?

- [Resources](resources/index.md)
