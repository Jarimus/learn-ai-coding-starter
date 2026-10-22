# Sloperator

A tree-walking interpreter for [SlopLang](docs/spec.md), written in Python.

## Usage

```bash
uv run sloperator.py path/to/program.slop
uv run sloperator.py --check path/to/program.slop
```

Pass `--check` to tokenize and parse without executing; it exits `0` when valid and `1` with the diagnostic otherwise.

## Validation

```bash
uv run pytest              # tests
uv run ruff format --check # formatting
uv run ruff check          # linting
uv run ty check            # type checking
```

## Language

SlopLang programs use the `.slop` extension. See [docs/spec.md](docs/spec.md) for the full language specification, including syntax, values, scoping, and control flow.

## Layout

| Path                    | What it is                                             |
| ----------------------- | ------------------------------------------------------ |
| `sloperator.py`         | Command-line entrypoint                                |
| `sloperator/lexer/`     | Source text to tokens                                  |
| `sloperator/parser/`    | Tokens to AST (`ast.py` holds the node definitions)    |
| `sloperator/evaluator/` | Walks the AST: values, environments, the interpreter   |
| `sloperator/runner.py`  | Runs source through all three stages                   |
| `docs/spec.md`          | The language specification                             |
| `examples/`             | Example programs                                       |
| `tests/`                | Pytest suite                                           |
| `playground/`           | A tiny web server and editor page for running programs |

## Playground

```bash
uv run playground/server.py
```

Then open <http://localhost:8080>.
