"""Exact expected stdout for programs in examples/."""

from pathlib import Path

import pytest

from sloperator.runner import run_source

EXAMPLES = Path(__file__).resolve().parent.parent / "examples"

EXPECTED_OUTPUTS = {
    "equality": "✅\n❌\n❌\n",
    "short-circuit": "❌\n✅\n",
}


@pytest.mark.parametrize("stem, expected", sorted(EXPECTED_OUTPUTS.items()))
def test_example_output(stem: str, expected: str):
    result = run_source((EXAMPLES / f"{stem}.slop").read_text(encoding="utf-8"))

    assert result.stderr == ""
    assert result.exit_code == 0
    assert result.stdout == expected
