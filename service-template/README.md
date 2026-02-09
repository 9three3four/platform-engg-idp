# Config Aware Service

This service exists to validate platform capabilities.

## What This Service Demonstrates
- Environment-aware configuration
- Externalized config via ConfigMaps
- Safe rollouts through GitOps
- Git-based rollback on failure

## Intentional Failure Mode
Setting FEATURE_FLAG=break will:
- Cause health check failures
- Trigger rollback scenarios
- Validate platform recovery workflows

## Ownership Model
- Application code: developer-owned
- Configuration & rollout: platform-owned
