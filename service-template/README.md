# Service Template

This template defines the standard way services are built and deployed
on the platform.

## What this provides
- Preconfigured CI pipeline
- Kubernetes manifests
- GitOps-compatible deployment
- Production-safe defaults

## How to create a new service?
1. Click "Use this template" in GitHub
2. Rename the repository
3. Push code to `main`
4. Platform handles the rest

## What devs do not need to know?
- Kubernetes internals
- Argo CD configuration
- Environment promotion mechanics

## Supported environments
- dev
- staging
- prod
