import pytest

from sloperator.errors import LexicalError
from sloperator.lexer import tokenize


def test_unexpected_character_falls_through_with_correct_line():
    """Regression: the catch-all branch in scan_token had no test.

    Unknown characters must raise a generic "unexpected character" error and
    report the line they appear on, not the line where the scanner started.
    """
    with pytest.raises(LexicalError) as info:
        tokenize("x = 1✨\n@ nope")

    assert info.value.line == 2
    assert info.value.message == "unexpected character '@'"
    assert str(info.value) == "SlopLang lexical error at line 2: unexpected character '@'"
