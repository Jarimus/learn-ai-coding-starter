---
description: Start the Sloperator playground server on a chosen port
---

Review the current TCP listeners:

!`lsof -nP -iTCP -sTCP:LISTEN`

Use `$ARGUMENTS` as the port. If it is empty, use `8080`. If it is 'stop', 'halt' or something similar, instead stop any running playground servers.

Before starting the server:

1. Validate that the port is a number between 1 and 65535. If it is not, stop and report the error.
2. Check the listener output above and run `pgrep -af "[p]layground/server.py"` to look for an existing Sloperator playground server. If a server is already running, or the chosen port is already in use, stop and report the existing process and port. Do not start a second server.

If the port is free and no Sloperator server is running, start `uv run playground/server.py PORT` in the background, replacing `PORT` with the chosen numeric port. Leave it running after the command returns, and report the playground URL.
