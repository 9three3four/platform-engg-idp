## Platform Bootstrap Flow

This platform uses a controlled bootstrap process:

1. Create a local k8s cluster (kind)
2. Install ArgoCD manually (one-time)
3. Apply the ArgoCD bootstrap Application
4. From this point onwards, ArgoCD manages itself and all workloads.

This approach avoids circular dependencies during initial cluster bring-up
while ensuring Git becomes the long-term source of truth.