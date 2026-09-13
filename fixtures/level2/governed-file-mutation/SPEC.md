# Governed file-mutation Level 2 fixture

Purpose: deterministic, non-production acceptance workload for AgentOS Level 2. This fixture does not alter GemVerse canon, engine source, production configuration, credentials, live data, monetization, analytics, release settings, or deployment state.

## Approved root

`fixtures/level2/governed-file-mutation/`

The worker must reject any target outside this root. The only authorized mutation target for this fixture is `baseline.txt`.

## Exact pre-image

```text
fixture_version=1
status=READY_FOR_LEVEL2_TEST
mutation_token=ORIGINAL
```

UTF-8 bytes: 71
SHA-256: `957541b23ab71d3f88ed6780611113f91a98fa24dbdd8a5e80c21482fcb3bc3f`

## Exact mutation

Replace exactly one line:

`mutation_token=ORIGINAL`

with:

`mutation_token=MUTATED_ONCE`

No other byte or file may change.

## Exact post-image

```text
fixture_version=1
status=READY_FOR_LEVEL2_TEST
mutation_token=MUTATED_ONCE
```

UTF-8 bytes: 75
SHA-256: `7cc11ed2039455eba91dada24f3a889bcaad97230917e94fa702869dbfaca7ce`

## Verification contract

A candidate run is acceptable only when all of the following are evidenced:

1. Record exact repository, ref, and commit before mutation.
2. Verify the approved root and exact target path before writing.
3. Verify the pre-image byte count and SHA-256 before mutation; fail closed on mismatch.
4. Apply only the specified single-line replacement.
5. Verify the post-image byte count and SHA-256 after mutation.
6. Capture repository diff proving no other file changed.
7. Record exact task/mission/worker/result correlation in the canonical AgentOS receipts/log path.
8. Re-run the identical task against the post-image and prove idempotent success with no second semantic mutation.
9. Exercise interrupted-write recovery using a disposable copy or governed test harness; the durable target must end at either the exact pre-image or exact post-image, never a partial image.
10. Prove no file outside the approved fixture root changed.
11. Retain execution and verification receipts for independent Green + PRS assessment.

## Replay/idempotency expectation

If `baseline.txt` already matches the exact post-image, the mutation must be treated as already satisfied. A replay must not append, duplicate, reformat, or otherwise alter the file.

If the file matches neither the exact pre-image nor exact post-image, fail closed and require operator review; do not attempt a heuristic repair.

## Recovery expectation

An interrupted or failed mutation must not leave a partial/truncated durable image. Recovery must establish one of two byte-exact states only:

- pre-image SHA-256 `957541b23ab71d3f88ed6780611113f91a98fa24dbdd8a5e80c21482fcb3bc3f`; or
- post-image SHA-256 `7cc11ed2039455eba91dada24f3a889bcaad97230917e94fa702869dbfaca7ce`.

Any third state is a failed recovery and must not be reported as complete.

## Non-production boundary

This fixture grants no authority to mutate any other GemVerse path and no authority to change canon, Construct 3/source artifacts, product behavior, release configuration, credentials, external systems, or production data. It is a deterministic acceptance workload only.
