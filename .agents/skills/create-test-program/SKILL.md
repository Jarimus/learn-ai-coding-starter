---
name: create-test-program
description: Add a runnable SlopLang example program in examples/ and an exact-output test in tests/test_example_outputs.py for a given language feature. Use when asked to demonstrate, document, or test SlopLang syntax or semantics with an example program.
---

# Create Test Program

Given a language feature, add a focused example program and a test that pins its exact stdout.

## 1. Read the spec

Read `docs/spec.md` and find the section that defines the feature. Use only syntax, values, and behavior documented there. Do not infer behavior from the implementation, and do not demonstrate the spec's non-goals.

## 2. Write the example

Create `examples/<feature>.slop`:

- Name it with lowercase kebab-case, for example `examples/logical-short-circuit.slop`.
- Keep it minimal and deterministic: exercise the feature in as few statements as possible.
- Start with a short `—` comment that says what the program demonstrates.
- Use smart quotes `“ ”`, em dash comments `—`, and the `✨` terminator after declarations, assignments, `ship`, and expression statements.
- Make it run cleanly: exit code `0`, empty stderr, and non-empty stdout. `tests/test_examples.py` enforces these rules for every file in `examples/`.

## 3. Capture the exact output

Run the program and copy stdout byte-for-byte, including spaces, emoji, and the trailing newline:

```bash
uv run sloperator.py examples/<feature>.slop
```

## 4. Add the exact-output test

Edit `tests/test_example_outputs.py`. If it does not exist, create it with this structure and include the new entry in `EXPECTED_OUTPUTS`:

```python
"""Exact expected stdout for programs in examples/."""

from pathlib import Path

import pytest

from sloperator.runner import run_source

EXAMPLES = Path(__file__).resolve().parent.parent / "examples"

EXPECTED_OUTPUTS = {
    "logical-short-circuit": "❌\n✅\n",
}


@pytest.mark.parametrize("stem, expected", sorted(EXPECTED_OUTPUTS.items()))
def test_example_output(stem: str, expected: str):
    result = run_source((EXAMPLES / f"{stem}.slop").read_text(encoding="utf-8"))

    assert result.stderr == ""
    assert result.exit_code == 0
    assert result.stdout == expected
```

When the file already exists, add exactly one entry to `EXPECTED_OUTPUTS` and leave the other entries alone unless their examples changed:

```python
EXPECTED_OUTPUTS = {
    "existing-example": "unchanged output\n",
    "new-feature": "exact output\n",
}
```

Write expected stdout as an explicit string literal, using `\n` for line breaks. Do not build it with `dedent`, `join`, or by running the interpreter from the test; the exact bytes should be readable in the test file.

## 5. Verify

Run the focused tests:

```bash
uv run pytest tests/test_example_outputs.py tests/test_examples.py -q
```

Then run the project's `validate` skill (pytest, `ruff format --check`, `ruff check`, `ty check`) before reporting the change.
