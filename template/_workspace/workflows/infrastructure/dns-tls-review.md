# Workflow: DNS / TLS Review

Use for DNS records, certificate changes, TLS settings, ingress/edge routing, load balancer listeners, domain cutovers, and hostname ownership.

## Required context

- affected domains/hostnames and environments
- current and proposed DNS/TLS/routing config
- TTLs, certificate lifecycle, and ownership notes
- rollback/cutover plan when relevant

## Process

1. Identify affected hostnames, records, certificate names, environments, and traffic path.
2. Review TTLs, propagation/cutover timing, certificate validity/renewal, SAN coverage, and issuer/ACME automation.
3. Check TLS policy, redirect behavior, SNI, listener/rule priority, ingress routing, and backend health dependencies.
4. Review blast radius: shared domains, wildcard certs, public exposure, cross-region/CDN/load balancer behavior.
5. Define validation: DNS lookup, cert inspection, config render/diff, dry run, health check, or canary/cutover checks.
6. Define rollback: previous record/cert/listener/rule, TTL timing, cache implications, and owner approval.

## Stop gates

Ask before changing public DNS, certificates, load balancer/listener rules, ingress routing, production traffic, or security policy.

## Result

Return:

- DNS/TLS/routing change summary
- blast radius and timing risks
- validation plan/results
- rollback/cutover notes
- blocking issues/questions
