---
name: create-and-validate
description: Create a runnable SlopLang example and exact-output test for a language feature, then run the project's full validation. Use when asked to add an example with tests and verify the repository end to end.
---

# Create and Validate

Given a language feature, run the two project skills in order. Do not repeat their instructions here; load each skill and follow it.

## Workflow

1. Load the `create-test-program` skill and follow it to read `docs/spec.md`, write the example in `examples/`, and add the exact-output test in `tests/test_example_outputs.py`.
2. Load the `validate` skill and follow it to run the tests, formatting check, linting, and type checking.

## Inputs

Treat the user's requested feature as the input to `create-test-program`. If no feature was requested, ask for one before starting.

## Report

Report the example and test files changed, the exact output that was pinned, and the result of each validation check. If either skill reports a failure, stop and report it rather than adding unrelated changes.
