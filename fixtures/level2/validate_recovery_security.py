#!/usr/bin/env python3
import copy

import validate_fixture as vf


def expect_rejected(result: dict, current_text: str, record: dict, reason: str) -> None:
    try:
        vf.validate_recovery_result(result, current_text, record)
    except AssertionError as exc:
        assert reason in str(exc), f"expected {reason}, got {exc}"
        return
    raise AssertionError(f"tampered recovery evidence accepted: {reason}")


def main() -> None:
    record = vf.canonical_prepared_record()
    result = vf.recover(vf.INITIAL, vf.TARGET, record)

    wrong_state = copy.deepcopy(result)
    wrong_state["chosen_state"] = "INITIAL"
    expect_rejected(wrong_state, vf.INITIAL, record, "RECOVERY_RESULT_STATE_MISMATCH")

    wrong_correlation = copy.deepcopy(result)
    wrong_correlation["correlation_id"] = "cross-task-correlation"
    expect_rejected(wrong_correlation, vf.INITIAL, record, "RECOVERY_RESULT_CORRELATION_MISMATCH")

    wrong_current_hash = copy.deepcopy(result)
    wrong_current_hash["evidence"]["current_state_sha256"] = vf.sha256_text(vf.TARGET)
    expect_rejected(wrong_current_hash, vf.INITIAL, record, "RECOVERY_RESULT_EVIDENCE_MISMATCH")

    extra_secret_shaped_evidence = copy.deepcopy(result)
    extra_secret_shaped_evidence["evidence"]["credential"] = "synthetic-do-not-persist"
    expect_rejected(extra_secret_shaped_evidence, vf.INITIAL, record, "RECOVERY_EVIDENCE_SCHEMA_MISMATCH")

    print("PASS: GemVerse recovery evidence rejects state, correlation, hash, and secret-shaped schema tampering")


if __name__ == "__main__":
    main()
