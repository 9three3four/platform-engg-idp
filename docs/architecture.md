## Problem Statement
As engineering teams scale, deployments become inconsistent, slow, and risky.

## Goals
- Standardised deployment workflows
- Clear ownership boundaries
- Safe promotion across environments
- Easy rollback

## Non-Goals
- No cloud-specific optimisations
- No AI/ML workloads (yet)

## High-Level Architecture

## Design Principles
- Git as source of truth
- Declarative over imperative
- Platform over pipelines

## High-Level Architecture

The platform follows a GitOps-first model where Git is the single source
of truth for both infrastructure configuration and application delivery.

### Flow
1. Developers use a standardised service template
2. Code changes trigger CI pipelines via GitHub Actions
3. Container images are built and versioned
4. Deployment manifests are updated declaratively
5. Argo CD reconciles desired state into the cluster
6. Applications are promoted safely across environments
7. Rollbacks are handled via Git history

### Environments
- Dev
- Staging
- Prod

Each environment is isolated but follows the same delivery pattern.

## Why Local-First
The platform is intentionally designed to run locally to:
- Reduce setup friction
- Avoid cloud vendor lock-in
- Emphasise architecture over infrastructure
- Enable easy demonstration and portability
