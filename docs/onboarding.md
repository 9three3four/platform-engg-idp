## Platform Bootstrap Flow

Here, Argo CD is initially installed using server-side apply to avoid CRD
annotation size limits. Ownership is immediately handed off to GitOps
via a bootstrap Application.

Also enabled ServerSideApply in bootstrap app. Why?
    Argo CD defaults to client-side apply, so for large CRDs like ApplicationSet we explicitly enable server-side apply at the Application level.


This platform uses a controlled bootstrap process:

1. Create a local k8s cluster (kind)
2. Install ArgoCD manually (one-time)
3. Apply the ArgoCD bootstrap Application
4. From this point onwards, ArgoCD manages itself and all workloads.

This approach avoids circular dependencies during initial cluster bring-up
while ensuring Git becomes the long-term source of truth.