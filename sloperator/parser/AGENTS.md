# Parser Conventions

- **Use one method per grammar rule.** Mirror the productions in `docs/spec.md` (for example `logic_or`, `comparison`, `term`, `factor`, `unary`, `call`, `primary`), and delegate sub-rules to their own methods instead of inlining their parsing.
- **Make syntax errors describe what token was found.** Raise through `self.error()` or `self.expect()` so diagnostics include the offending token's lexeme (`..., found '<lexeme>'`) or note end of file, and carry the correct source line.
