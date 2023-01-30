# High Availability

> **What to read previously?** - [Reference Architecture](index.md)

Is mandatory support multi-zone high availability in all production deployments. Multi-Region HA must be justified and used on the next cases:

1. Serve closest as possible to the user region due to justified latency restriction
2. Mission Critical Applications and Services

Mission Critical applications and services must belong to the next groups:

1. Human safety
2. Kitchen/Food functions
3. Power Systems
4. Self-Driving car/drone
5. Environment Security (fire-alarm, security cams, smoke sensors, ...)

> :warning: **WARNING!** See multi-cloud to clarify the difference between HA and DRP. Multi-region is recommendable as support for a DRP strategy.
