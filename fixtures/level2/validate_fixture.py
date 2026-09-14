#!/usr/bin/env python3
from pathlib import Path
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


def mutate(text: str) -> str:
    if text == TARGET:
        return TARGET
    if text != INITIAL:
        raise ValueError("unexpected pre-image")
    return text.replace("state=INITIAL\ncounter=0", "state=VERIFIED_EDIT\ncounter=1")


def validate_complete_state(text: str) -> None:
    if text not in (INITIAL, TARGET):
        raise AssertionError("partial/mixed/truncated fixture state")


def main() -> None:
    current = SOURCE.read_text(encoding="utf-8")
    assert current == INITIAL, "repository fixture no longer matches canonical initial state"

    first = mutate(current)
    assert first == TARGET, "authorised mutation does not produce exact target"
    assert first.count("state=VERIFIED_EDIT") == 1
    assert first.count("counter=1") == 1

    replay = mutate(first)
    assert replay == TARGET, "replay is not idempotent"

    with tempfile.TemporaryDirectory() as tmp:
        work = Path(tmp) / SOURCE.name
        shutil.copy2(SOURCE, work)
        original = work.read_text(encoding="utf-8")
        assert original == INITIAL

        # Simulate a crash-safe prepared write: recovery may retain the original or
        # promote the complete target, but must never accept a partial state.
        prepared = work.with_suffix(work.suffix + ".prepared")
        prepared.write_text(TARGET, encoding="utf-8")
        validate_complete_state(work.read_text(encoding="utf-8"))
        validate_complete_state(prepared.read_text(encoding="utf-8"))

        # A truncated candidate must be rejected rather than promoted.
        bad = work.with_suffix(work.suffix + ".partial")
        bad.write_text("mission=agentos-level2\nproject=gemverse\nstate=VERIFIED", encoding="utf-8")
        try:
            validate_complete_state(bad.read_text(encoding="utf-8"))
        except AssertionError:
            pass
        else:
            raise AssertionError("partial candidate was accepted")

    print("PASS: GemVerse Level 2 fixture contract is deterministic, idempotent, and partial-state rejecting")


if __name__ == "__main__":
    main()
