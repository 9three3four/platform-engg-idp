# Platform Engineering IDP (local-first)

## Overview
This repository demonstrates the design and implementation of a
GitOps-driven Internal Developer Platform (IDP) built with a local-first
approach.

The goal is to show how platform teams can enable consistent, safe, scalable app delivery without tightly coupling to any specific cloud provider. 

## Why this exists?
As teams scale, deployment workflows tend to drift, ownership sometimes gets blurred, and operational risk might increase. This repo gives a view on how a GitOps-driven Internal Developer Platform can address these problems using declarative delivery and clear platform boundaries.

## What this repo is about?
- Platform engineering mindset
- GitOps-based delivery using Argo CD
- Multi-environment deployment strategy
- Developer golden paths
- Operational thinking (failure & recovery)

## What this is not?
- A toy demo
- A cloud-specific implementation
- A production-ready SaaS

## Architecture
High-level architecture and design decisions are documented in:
- `architecture/`
- `docs/architecture.md`
- `decisions/`

## Demo
This platform is designed to run locally using Kubernetes (kind).
Short demo recordings and walkthroughs are referenced inside the docs.

## Future Extensions
- Cloud-backed clusters (EKS/GKE)
- Secrets management
- Observability
- AI / LLM workloads on top of the platform    