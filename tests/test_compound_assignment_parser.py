"""Parser tests for the += compound assignment operator."""

from sloperator.lexer import TokenType, tokenize
from sloperator.parser import parse
from sloperator.parser.ast import Assign, Binary, Block, CompoundAssign


def tokens(source: str):
    return tokenize(source)


def parse_source(source: str):
    return parse(tokenize(source))


def test_plus_equal_is_a_single_token():
    scanned = tokens("n += 1✨")

    assert [token.type for token in scanned] == [
        TokenType.IDENTIFIER,
        TokenType.PLUS_EQUAL,
        TokenType.NUMBER,
        TokenType.SPARKLES,
        TokenType.EOF,
    ]
    assert scanned[1].lexeme == "+="


def test_plus_without_equal_is_still_addition():
    scanned = tokens("n + 1✨")

    assert scanned[1].type is TokenType.PLUS
    assert scanned[1].lexeme == "+"


def test_compound_assignment_is_a_statement():
    (statement,) = parse_source("n += 3 * 4✨")

    assert isinstance(statement, CompoundAssign)
    assert statement.name.lexeme == "n"
    assert statement.operator.type is TokenType.PLUS_EQUAL
    assert isinstance(statement.value, Binary)
    assert statement.value.operator.type is TokenType.STAR


def test_plain_assignment_is_still_an_assign():
    (statement,) = parse_source("n = 1✨")

    assert isinstance(statement, Assign)
    assert statement.operator.type is TokenType.EQUAL


def test_compound_assignment_parses_inside_a_block():
    (block,) = parse_source("{ n += 1✨ }")

    assert isinstance(block, Block)
    assert isinstance(block.statements[0], CompoundAssign)
