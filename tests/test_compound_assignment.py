"""Regression tests for the += compound assignment operator."""

from sloperator.runner import run_source


def run(source: str) -> str:
    result = run_source(source)
    assert result.stderr == "", result.stderr
    assert result.exit_code == 0
    return result.stdout


def fails(source: str) -> str:
    result = run_source(source)
    assert result.stdout == ""
    assert result.exit_code == 1
    return result.stderr.rstrip("\n")


def test_compound_assignment_adds_numbers():
    source = """slop n = 2✨
n += 3 * 4✨
hallucinate(n)✨"""
    assert run(source) == "14\n"


def test_compound_assignment_concatenates_strings():
    source = """slop greeting = “hello”✨
greeting += “, slop”✨
hallucinate(greeting)✨"""
    assert run(source) == "hello, slop\n"


def test_compound_assignment_updates_the_nearest_variable():
    source = """slop n = 1✨
{
    slop n = 2✨
    n += 10✨
    hallucinate(n)✨
}
hallucinate(n)✨"""
    assert run(source) == "12\n1\n"


def test_compound_assignment_evaluates_the_right_hand_side_first():
    source = """clanker bump() {
    n = 10✨
    ship 5✨
}
slop n = 2✨
n += bump()✨
hallucinate(n)✨"""
    assert run(source) == "15\n"


def test_compound_assignment_rejects_undefined_names():
    assert (
        fails("missing += 1✨") == "SlopLang runtime error at line 1: undefined variable 'missing'"
    )


def test_compound_assignment_rejects_loadbearing_bindings():
    source = """loadbearing LIMIT = 100✨
LIMIT += 1✨"""
    assert fails(source) == "SlopLang runtime error at line 2: cannot assign to loadbearing 'LIMIT'"


def test_compound_assignment_rejects_incompatible_types():
    source = """slop n = 1✨
n += “x”✨"""
    assert fails(source) == (
        "SlopLang runtime error at line 2: operands of '+=' must both be numbers "
        "or both be strings, got number and string"
    )
