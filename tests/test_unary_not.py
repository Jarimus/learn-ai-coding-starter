import pytest

from sloperator.runner import run_source


@pytest.mark.parametrize(
    ("expression", "expected"),
    [
        ("!✅", "❌"),
        ("!❌", "✅"),
        ("!!✅", "✅"),
        ("!!!✅", "❌"),
        ("!❌ == ✅", "✅"),
        ("!(✅ && ❌)", "✅"),
    ],
)
def test_unary_not_negates_booleans(expression: str, expected: str):
    result = run_source(f"hallucinate({expression})✨")

    assert result.stderr == ""
    assert result.stdout == f"{expected}\n"


def test_unary_not_rejects_non_booleans():
    result = run_source("hallucinate(!1)✨")

    assert result.exit_code == 1
    assert result.stdout == ""
    assert result.stderr == (
        "SlopLang runtime error at line 1: operand of unary '!' must be a boolean, got number\n"
    )
