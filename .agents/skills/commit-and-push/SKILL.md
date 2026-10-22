---
name: commit-and-push
description: Commit all changes and push them to repo
---

## Checklist

1. First stage all unstaged changes with 'git add .'.
2. If there are no changes in the work tree, stop here and inform the user.
3. The user should have provided a commit comment for the skill. Commit with 'git commit -m "<user's comment>"'.
4. If the user did not provide a comment, ask for it.
5. After commiting, push the changes with 'git push'.

##

1. With any unexpected behaviour, stop and undo the process. Inform the user of the unexpected behaviour.
