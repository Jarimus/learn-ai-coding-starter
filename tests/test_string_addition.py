import pytest

from sloperator.runner import run_source


@pytest.mark.parametrize(
    ("expression", "expected"),
    [
        ("“” + “slop”", "slop"),
        ("“slop” + “”", "slop"),
        ("“café” + “✨”", "café✨"),
    ],
)
def test_string_addition(expression: str, expected: str):
    result = run_source(f"hallucinate({expression})✨")

    assert result.stdout == f"{expected}\n"
    assert result.stderr == ""
    assert result.exit_code == 0


def test_string_addition_produces_a_string():
    result = run_source("hallucinate((“” + “slop”) == “slop”)✨")

    assert result.stdout == "✅\n"
    assert result.stderr == ""
    assert result.exit_code == 0
