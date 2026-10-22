---
description: Review changes, commit them, and rebase onto origin/main
---

Review the current project changes before committing.

1. Run `git status` and `git diff` (and `git diff --cached` if anything is already staged). Check for unintended files, secrets, leftover debug code, and incomplete edits. If the changes look wrong, stop and report the problem instead of committing.
2. If there is nothing to commit, stop and report that.
3. If no commit message was provided, stop and ask for one.
4. Stage the project changes with `git add .`.
5. Commit the staged changes with `git commit -m "$ARGUMENTS"`.
6. Run `git pull --rebase origin main`.
7. If the rebase fails or has conflicts, stop and report them rather than resolving conflicts automatically.

Report the commit hash and the result of the rebase.
