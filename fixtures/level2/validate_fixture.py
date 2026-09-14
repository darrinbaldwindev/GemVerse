#!/usr/bin/env python3
from pathlib import Path
import hashlib
import json
import tempfile
import shutil

ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / "gemverse-worker-acceptance.txt"
INITIAL = """mission=agentos-level2
project=gemverse
state=INITIAL
counter=0
note=non-production-fixture
"""
TARGET = """mission=agentos-level2
project=gemverse
state=VERIFIED_EDIT
counter=1
note=non-production-fixture
"""


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def stable_correlation(mission: str, project: str, preimage_hash: str, target_hash: str) -> str:
    material = "|".join([mission, project, preimage_hash, target_hash])
    return hashlib.sha256(material.encode("utf-8")).hexdigest()[:24]


def mutate(text: str) -> str:
    if text == TARGET:
        return TARGET
    if text != INITIAL:
        raise ValueError("unexpected pre-image")
    return text.replace("state=INITIAL\ncounter=0", "state=VERIFIED_EDIT\ncounter=1")


def validate_complete_state(text: str) -> None:
    if text not in (INITIAL, TARGET):
        raise AssertionError("partial/mixed/truncated fixture state")


def canonical_prepared_record() -> dict:
    mission = "agentos-level2"
    project = "gemverse"
    preimage_hash = sha256_text(INITIAL)
    target_hash = sha256_text(TARGET)
    return {
        "mission": mission,
        "project": project,
        "preimage_sha256": preimage_hash,
        "target_sha256": target_hash,
        "correlation_id": stable_correlation(mission, project, preimage_hash, target_hash),
    }


def validate_prepared_record(record: dict) -> None:
    expected = canonical_prepared_record()
    extra = sorted(set(record) - set(expected))
    missing = sorted(set(expected) - set(record))
    if extra:
        raise AssertionError(f"unrecognised prepared metadata fields: {extra}")
    if missing:
        raise AssertionError(f"missing prepared metadata fields: {missing}")
    if record != expected:
        raise AssertionError("prepared record identity/correlation mismatch")


def recovery_evidence(action: str, record: dict) -> dict:
    return {
        "fixture": True,
        "mission": record["mission"],
        "project": record["project"],
        "correlation_id": record["correlation_id"],
        "preimage_sha256": record["preimage_sha256"],
        "target_sha256": record["target_sha256"],
        "action": action,
    }


def recover(current_text: str, prepared_text: str, record: dict) -> dict:
    try:
        validate_complete_state(current_text)
    except AssertionError as exc:
        raise AssertionError("RECOVERY_DENIED_CURRENT_STATE_INVALID") from exc
    try:
        validate_complete_state(prepared_text)
    except AssertionError as exc:
        raise AssertionError("RECOVERY_DENIED_PREPARED_STATE_INVALID") from exc
    try:
        validate_prepared_record(record)
    except AssertionError as exc:
        raise AssertionError(f"RECOVERY_DENIED_PREPARED_IDENTITY: {exc}") from exc
    if sha256_text(prepared_text) != record["target_sha256"] or prepared_text != TARGET:
        raise AssertionError("RECOVERY_DENIED_PREPARED_PAYLOAD_MISMATCH")
    if current_text == TARGET:
        action = "ALREADY_COMPLETE"
    elif current_text == INITIAL:
        action = "PROMOTE_PREPARED"
    else:
        raise AssertionError("RECOVERY_DENIED_UNRECOVERABLE_STATE")
    return {
        "chosen_state": "TARGET",
        "action": action,
        "correlation_id": record["correlation_id"],
        "evidence": recovery_evidence(action, record),
    }


def recover_candidates(current_text: str, candidates: list[dict]) -> dict:
    if len(candidates) != 1:
        raise AssertionError("RECOVERY_DENIED_CANDIDATE_AMBIGUITY")
    candidate = candidates[0]
    return recover(current_text, candidate["payload"], candidate["record"])


def assert_rejected(text: str, label: str) -> None:
    try:
        validate_complete_state(text)
    except AssertionError:
        return
    raise AssertionError(f"{label} was accepted")


def assert_mutation_rejected(text: str, label: str) -> None:
    try:
        mutate(text)
    except ValueError:
        return
    raise AssertionError(f"{label} was accepted as an authorised pre-image")


def assert_prepared_rejected(record: dict, label: str) -> None:
    try:
        validate_prepared_record(record)
    except AssertionError:
        return
    raise AssertionError(f"{label} prepared record was accepted")


def main() -> None:
    repository_before = SOURCE.read_text(encoding="utf-8")
    assert repository_before == INITIAL, "repository fixture no longer matches canonical initial state"

    first = mutate(repository_before)
    assert first == TARGET
    assert mutate(first) == TARGET, "replay is not idempotent"

    near_misses = {
        "truncated": "mission=agentos-level2\nproject=gemverse\nstate=VERIFIED",
        "wrong-project": INITIAL.replace("project=gemverse", "project=other"),
        "counter-skipped": TARGET.replace("counter=1", "counter=2"),
        "mixed-state": INITIAL.replace("state=INITIAL", "state=VERIFIED_EDIT"),
    }
    for label, text in near_misses.items():
        assert_rejected(text, label)
        assert_mutation_rejected(text, label)

    canonical_prepared = canonical_prepared_record()
    validate_prepared_record(canonical_prepared)
    prepared_near_misses = {
        "prepared-wrong-project": {**canonical_prepared, "project": "other"},
        "prepared-stale-preimage": {**canonical_prepared, "preimage_sha256": sha256_text(TARGET)},
        "prepared-wrong-target": {**canonical_prepared, "target_sha256": sha256_text(INITIAL)},
        "prepared-wrong-mission": {**canonical_prepared, "mission": "other"},
        "prepared-wrong-correlation": {**canonical_prepared, "correlation_id": "other"},
        "prepared-extra-field": {**canonical_prepared, "unexpected": "value"},
        "prepared-missing-project": {k: v for k, v in canonical_prepared.items() if k != "project"},
    }
    for label, record in prepared_near_misses.items():
        assert_prepared_rejected(record, label)

    with tempfile.TemporaryDirectory() as tmp:
        work = Path(tmp) / SOURCE.name
        shutil.copy2(SOURCE, work)
        original = work.read_text(encoding="utf-8")
        prepared = work.with_suffix(work.suffix + ".prepared")
        prepared.write_text(TARGET, encoding="utf-8")
        candidate = {"payload": prepared.read_text(encoding="utf-8"), "record": canonical_prepared}

        decision = recover_candidates(original, [candidate])
        repeated = recover_candidates(original, [candidate])
        assert json.dumps(decision, sort_keys=True) == json.dumps(repeated, sort_keys=True), "recovery decision is not byte-stable"
        assert decision["action"] == "PROMOTE_PREPARED"
        assert decision["evidence"]["fixture"] is True
        assert decision["evidence"]["action"] == "PROMOTE_PREPARED"

        duplicate = recover_candidates(TARGET, [candidate])
        assert duplicate["action"] == "ALREADY_COMPLETE"
        assert duplicate["evidence"]["action"] == "ALREADY_COMPLETE"
        assert duplicate["correlation_id"] == decision["correlation_id"]

        try:
            recover("mission=agentos-level2\nproject=other\nstate=INITIAL\ncounter=0\nnote=non-production-fixture\n", TARGET, canonical_prepared)
        except AssertionError as exc:
            assert "RECOVERY_DENIED_CURRENT_STATE_INVALID" in str(exc)
        else:
            raise AssertionError("prepared/current identity disagreement was accepted")

        try:
            recover(INITIAL, INITIAL, canonical_prepared)
        except AssertionError as exc:
            assert "RECOVERY_DENIED_PREPARED_PAYLOAD_MISMATCH" in str(exc)
        else:
            raise AssertionError("metadata-correct but payload-mismatched artifact was accepted")

        competing = [candidate, {"payload": TARGET, "record": {**canonical_prepared, "correlation_id": "competing"}}]
        try:
            recover_candidates(INITIAL, competing)
        except AssertionError as exc:
            assert "RECOVERY_DENIED_CANDIDATE_AMBIGUITY" in str(exc)
        else:
            raise AssertionError("competing prepared artifacts were silently selected")

    assert SOURCE.read_text(encoding="utf-8") == repository_before, "synthetic recovery tests changed canonical fixture"
    print("PASS: GemVerse recovery is deterministic, evidence-bearing, identity-bound, fail-closed, and leaves canonical fixture unchanged")


if __name__ == "__main__":
    main()
