import pytest

from sloperator.runner import run_source


def run(source: str) -> str:
    result = run_source(source)
    assert result.stderr == "", result.stderr
    return result.stdout


@pytest.mark.parametrize(
    ("expression", "expected"),
    [
        ("2 + 3 * 4", "14"),
        ("2 * 3 + 4", "10"),
        ("2 + 3 * 4 - 5 * 6", "-16"),
    ],
)
def test_multiplication_binds_tighter_than_addition(expression: str, expected: str):
    assert run(f"hallucinate({expression})✨") == f"{expected}\n"
