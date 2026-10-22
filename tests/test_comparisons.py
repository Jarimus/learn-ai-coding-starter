from sloperator.runner import run_source


def test_comparison_binds_tighter_than_equality():
    """Regression: `1 < 2 == ✅` must parse as `(1 < 2) == ✅`.

    Equality binds looser than comparison, so the ordered comparison is
    evaluated first and then compared to the boolean.
    """
    result = run_source("hallucinate(1 < 2 == ✅)✨")

    assert result.stderr == ""
    assert result.exit_code == 0
    assert result.stdout == "✅\n"
