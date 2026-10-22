"""Regression tests for identifiers containing digits.

Original symptom: `slop score2 = 40✨` reported
"SlopLang syntax error at line 1: expected '=' after variable name, an
initializer is required, found '2'" because the scanner stopped an identifier at
the first digit. The specification allows `[A-Za-z_][A-Za-z0-9_]*`.
"""

from sloperator.lexer import TokenType, tokenize
from sloperator.runner import run_source


def test_digits_are_part_of_an_identifier():
    tokens = tokenize("score2✨")

    assert [token.type for token in tokens] == [
        TokenType.IDENTIFIER,
        TokenType.SPARKLES,
        TokenType.EOF,
    ]
    assert tokens[0].lexeme == "score2"


def test_variable_names_may_contain_digits():
    result = run_source("slop score2 = 40✨\nscore2 = score2 + 2✨\nhallucinate(score2)✨\n")

    assert (result.stdout, result.stderr, result.exit_code) == ("42\n", "", 0)


def test_function_and_parameter_names_may_contain_digits():
    source = "clanker add2(x1) {\n  ship x1 + 2✨\n}\nhallucinate(add2(40))✨\n"

    result = run_source(source)

    assert (result.stdout, result.stderr, result.exit_code) == ("42\n", "", 0)


def test_identifiers_cannot_start_with_a_digit():
    result = run_source("slop 1x = 1✨\n")

    assert result.stdout == ""
    assert result.exit_code == 1
    assert result.stderr == (
        "SlopLang syntax error at line 1: expected a variable name after 'slop', found '1'\n"
    )
