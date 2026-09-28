# Kubernetes Workload Triage Workflow

## Required context

- `_workspace/context/reference/kubernetes-principles.md`
- `_workspace/context/reference/tool-notes/kubernetes.md`
- `_workspace/context/reference/incident-and-oncall-principles.md`

## Process

1. Identify cluster, namespace, workload, environment, and the symptom: CrashLoopBackOff, OOMKilled, Pending, failing probes, image pull errors, or restarts.
2. Collect read-only evidence: pod status and events, recent logs, resource requests against usage, probe configuration, node conditions, and recent changes to image, configuration, or secrets.
3. Rank likely causes, with the evidence for each.
4. Propose the smallest fix and how to verify it. Restarting, scaling, editing, or deleting resources is approval-gated. If users are affected, switch to the incident-response pipeline.

## Result

Produce a triage note with the symptom, evidence, ranked causes, proposed fix, verification, and open questions.
