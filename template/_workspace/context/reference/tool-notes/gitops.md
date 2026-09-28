# GitOps Notes

Applies to Argo CD, Flux, and similar controllers that reconcile a cluster from Git.

- The Git repository is the desired state. Change it through commits and pull requests, not by editing live resources.
- Identify the controller, the app-of-apps or root object, the project or tenant boundary, and the target cluster and namespace before adding anything.
- Keep one application per service and environment, or one generator (`ApplicationSet`, Kustomization) that produces them. Name them predictably.
- Pin the source revision per environment: a branch for development, a tag or commit for production, or a promotion flow that moves an explicit version.
- Choose the sync policy deliberately. Automated sync with prune and self-heal suits development; production usually needs manual sync or an approval gate.
- Declare sync ordering (waves, dependencies) for CRDs, namespaces, and secrets that workloads need first.
- Adding, syncing, pruning, or deleting an application in a shared or production cluster is approval-gated. Merging to the tracked branch counts as a deployment when auto-sync is on.
