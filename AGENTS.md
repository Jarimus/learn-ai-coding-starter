# AGENTS.md

Sloperator is a Python 3.13 tree-walking interpreter for SlopLang. The runtime is stdlib-only.

## Project layout

- `sloperator.py` — CLI entrypoint (`--check` parses without executing)
- `sloperator/lexer/`, `sloperator/parser/`, `sloperator/evaluator/` — source text to tokens, tokens to AST, AST evaluation
- `sloperator/runner.py` — runs source through all three stages
- `examples/` — `.slop` programs, each also exercised by `tests/test_examples.py`
- `tests/` — pytest suite
- `playground/server.py` — local web editor at <http://localhost:8080>
- `docs/spec.md` — the language specification

## Validation

Run all four before considering a change done:

```bash
uv run pytest              # tests
uv run ruff format --check # formatting
uv run ruff check          # linting
uv run ty check            # type checking
```

After making any code change, run `uv run ruff format` to apply formatting before running the checks above.

For comparison tests, run the focused file with `uv run pytest tests/test_comparisons.py -q`.

## When to add regression tests

Add a test whenever behavior could silently change:

- **Bug fix:** reproduce the bug first, then keep the test that fails without the fix. Name it in `tests/test_*_regression.py` and note the original symptom in the docstring.
- **Language change:** when adding or altering syntax, update the lexer, parser/AST, and evaluator, with matching tests at each layer.
- **Error behavior:** assert the exact stderr (`SlopLang <kind> error at line N: message`), exit code, and any stdout produced before the error. Wording and line numbers are part of the contract.
- **Runnable example:** add it to `examples/` only if it is meant to stay correct; `tests/test_examples.py` automatically runs every example and requires non-empty stdout.

Most tests call `run_source()`, which returns `RunResult(stdout, stderr, exit_code)` rather than raising language errors.

## Language behavior

`docs/spec.md` is the source of truth for SlopLang syntax, values, scoping, and control flow. Check it rather than inferring behavior from the implementation.
