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


def validate_prepared_record(record: dict) -> None:
    expected = {
        "mission": "agentos-level2",
        "project": "gemverse",
        "preimage_sha256": sha256_text(INITIAL),
        "target_sha256": sha256_text(TARGET),
    }
    if record != expected:
        raise AssertionError("prepared record identity/correlation mismatch")


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
    current = SOURCE.read_text(encoding="utf-8")
    assert current == INITIAL, "repository fixture no longer matches canonical initial state"

    first = mutate(current)
    assert first == TARGET, "authorised mutation does not produce exact target"
    assert first.count("state=VERIFIED_EDIT") == 1
    assert first.count("counter=1") == 1

    replay = mutate(first)
    assert replay == TARGET, "replay is not idempotent"

    near_misses = {
        "truncated": "mission=agentos-level2\nproject=gemverse\nstate=VERIFIED",
        "wrong-project": INITIAL.replace("project=gemverse", "project=other"),
        "counter-skipped": TARGET.replace("counter=1", "counter=2"),
        "mixed-state": INITIAL.replace("state=INITIAL", "state=VERIFIED_EDIT"),
    }
    for label, text in near_misses.items():
        assert_rejected(text, label)
        assert_mutation_rejected(text, label)

    canonical_prepared = {
        "mission": "agentos-level2",
        "project": "gemverse",
        "preimage_sha256": sha256_text(INITIAL),
        "target_sha256": sha256_text(TARGET),
    }
    validate_prepared_record(canonical_prepared)

    prepared_near_misses = {
        "prepared-wrong-project": {**canonical_prepared, "project": "other"},
        "prepared-stale-preimage": {**canonical_prepared, "preimage_sha256": sha256_text(TARGET)},
        "prepared-wrong-target": {**canonical_prepared, "target_sha256": sha256_text(INITIAL)},
        "prepared-wrong-mission": {**canonical_prepared, "mission": "other"},
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
        validate_complete_state(work.read_text(encoding="utf-8"))
        validate_complete_state(prepared.read_text(encoding="utf-8"))
        validate_prepared_record(json.loads(prepared_meta.read_text(encoding="utf-8")))

        for label, text in near_misses.items():
            bad = work.with_suffix(work.suffix + f".{label}")
            bad.write_text(text, encoding="utf-8")
            assert_rejected(bad.read_text(encoding="utf-8"), label)

        # Stale replay evidence may not be rebound to the current authorised pre-image.
        stale_meta = {**canonical_prepared, "preimage_sha256": sha256_text(TARGET)}
        stale_path = work.with_suffix(work.suffix + ".stale-prepared.json")
        stale_path.write_text(json.dumps(stale_meta, sort_keys=True), encoding="utf-8")
        assert_prepared_rejected(json.loads(stale_path.read_text(encoding="utf-8")), "stale-replay")

    print("PASS: GemVerse Level 2 fixture contract rejects state and prepared-record identity/correlation near-misses")


if __name__ == "__main__":
    main()
