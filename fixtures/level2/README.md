# GemVerse Level 2 governed worker fixture

Canonical mission: `darrinbaldwindev/Overseer#49`
Parent coordination: GemVerse issue #5

## Purpose

Provide a deterministic, non-production acceptance workload for the AgentOS Level 2 governed Windows worker.

## Approved fixture root

Only `fixtures/level2/` is in scope for this workload.

## Starting file

`fixtures/level2/gemverse-worker-acceptance.txt`

Expected initial content:

```text
mission=agentos-level2
project=gemverse
state=INITIAL
counter=0
note=non-production-fixture
```

## Exact authorised mutation

Change only these two lines:

```diff
-state=INITIAL
-counter=0
+state=VERIFIED_EDIT
+counter=1
```

Expected target content:

```text
mission=agentos-level2
project=gemverse
state=VERIFIED_EDIT
counter=1
note=non-production-fixture
```

## Verification requirements

A Level 2 acceptance run must capture and correlate:

1. exact repository/ref/head before mutation;
2. exact task, mission, worker, and result identifiers;
3. approved-root decision for `fixtures/level2/`;
4. exact pre-image content or hash;
5. the mutation receipt;
6. exact post-image content or hash;
7. repository diff proving only the two authorised lines changed;
8. test/verification result;
9. proof that no file outside `fixtures/level2/` changed;
10. downstream Green + PRS assessment before completion is claimed.

## Replay/idempotency rule

Re-running the same authorised task against the target state must make no second semantic mutation. `counter` must remain `1`; duplicate lines or repeated increments are a failure.

## Recovery rule

For an injected interruption during mutation, the file must be recoverable to either the complete initial state or the complete target state. Partial, truncated, mixed, or duplicate state is a failure. Recovery must produce durable evidence correlated to the same mission/task lineage.

## Concurrency rule

If two workers/tasks contend for this fixture, unsafe last-writer-wins behavior is not acceptable. The existing AgentOS concurrency/authority mechanism must prevent or explicitly serialize/conflict the mutation, with evidence.

## Hard boundary

This fixture does not authorize changes to GemVerse canon, executable Arena source, production configuration, deployment, credentials, live data, analytics, monetization, release settings, or any file outside `fixtures/level2/`.

This fixture is an acceptance workload only. It does not itself prove AgentOS Level 2 capability.
