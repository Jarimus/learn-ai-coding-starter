from sloperator.runner import run_source


def test_call_as_argument_to_another_call():
    source = """clanker add(left, right) {
    ship left + right✨
}
hallucinate(add(1, 2))✨"""

    result = run_source(source)

    assert result.stderr == ""
    assert result.exit_code == 0
    assert result.stdout == "3\n"
