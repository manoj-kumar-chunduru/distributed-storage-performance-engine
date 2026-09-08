# ADR 0001: Modular Storage Engine

## Status
Accepted

## Decision
Use explicit interfaces and a coordinator to separate routing, caching, persistence, and replication.

## Consequences
The system is easier to test and evolve, at the cost of additional abstraction and wiring.
