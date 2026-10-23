"""Regression tests for assignment through nested standalone blocks.

Original symptom: a bare block was parented to the global scope instead of the
enclosing scope, so an assignment inside it skipped a shadowing binding. The
program below printed "2" then "3" instead of "3" then "1".
"""

from sloperator.runner import run_source


def test_nested_block_assignment_updates_the_nearest_shadowing_binding():
    source = """slop score = 1✨
{
    slop score = 2✨
    {
        score = 3✨
    }
    hallucinate(score)✨
}
hallucinate(score)✨"""

    result = run_source(source)

    assert (result.stdout, result.stderr, result.exit_code) == ("3\n1\n", "", 0)
