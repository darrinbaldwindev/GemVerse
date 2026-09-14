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
    return {
        "mission": "agentos-level2",
        "project": "gemverse",
        "preimage_sha256": sha256_text(INITIAL),
        "target_sha256": sha256_text(TARGET),
    }


def validate_prepared_record(record: dict) -> None:
    if record != canonical_prepared_record():
        raise AssertionError("prepared record identity/correlation mismatch")


def recover(current_text: str, prepared_text: str, record: dict) -> dict:
    validate_complete_state(current_text)
    validate_complete_state(prepared_text)
    validate_prepared_record(record)
    if prepared_text != TARGET:
        raise AssertionError("prepared payload is not canonical target")
    if current_text == TARGET:
        return {"chosen_state": "TARGET", "action": "ALREADY_COMPLETE"}
    if current_text == INITIAL:
        return {"chosen_state": "TARGET", "action": "PROMOTE_PREPARED"}
    raise AssertionError("unrecoverable state")


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
    assert first == TARGET, "authorised mutation does not produce exact target"
    assert first.count("state=VERIFIED_EDIT") == 1
    assert first.count("counter=1") == 1
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
        "prepared-missing-project": {k: v for k, v in canonical_prepared.items() if k != "project"},
        "prepared-missing-mission": {k: v for k, v in canonical_prepared.items() if k != "mission"},
    }
    for label, record in prepared_near_misses.items():
        assert_prepared_rejected(record, label)

    with tempfile.TemporaryDirectory() as tmp:
        work = Path(tmp) / SOURCE.name
        shutil.copy2(SOURCE, work)
        original = work.read_text(encoding="utf-8")
        assert original == INITIAL

        prepared = work.with_suffix(work.suffix + ".prepared")
        prepared.write_text(TARGET, encoding="utf-8")
        prepared_meta = work.with_suffix(work.suffix + ".prepared.json")
        prepared_meta.write_text(json.dumps(canonical_prepared, sort_keys=True), encoding="utf-8")

        decision = recover(original, prepared.read_text(encoding="utf-8"), json.loads(prepared_meta.read_text(encoding="utf-8")))
        assert decision == {"chosen_state": "TARGET", "action": "PROMOTE_PREPARED"}

        duplicate = recover(TARGET, prepared.read_text(encoding="utf-8"), json.loads(prepared_meta.read_text(encoding="utf-8")))
        assert duplicate == {"chosen_state": "TARGET", "action": "ALREADY_COMPLETE"}

        for label, text in near_misses.items():
            bad = work.with_suffix(work.suffix + f".{label}")
            bad.write_text(text, encoding="utf-8")
            assert_rejected(bad.read_text(encoding="utf-8"), label)

        stale_meta = {**canonical_prepared, "preimage_sha256": sha256_text(TARGET)}
        stale_path = work.with_suffix(work.suffix + ".stale-prepared.json")
        stale_path.write_text(json.dumps(stale_meta, sort_keys=True), encoding="utf-8")
        assert_prepared_rejected(json.loads(stale_path.read_text(encoding="utf-8")), "stale-replay")

    assert SOURCE.read_text(encoding="utf-8") == repository_before, "synthetic recovery tests changed canonical fixture"
    print("PASS: GemVerse Level 2 fixture recovery is deterministic, idempotent, identity-bound, and leaves canonical fixture unchanged")


if __name__ == "__main__":
    main()
