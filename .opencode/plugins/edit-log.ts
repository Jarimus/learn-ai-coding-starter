import { appendFile, mkdir } from "node:fs/promises"
import { join } from "node:path"

import { Plugin } from "@opencode/plugin"

const LOGGED_TOOLS = new Set(["edit", "write", "patch"])
const LOG_DIRECTORY = "logs"
const LOG_FILE = "plugin-tools.log"

export default Plugin.define({
  id: "sloperator.edit-log",
  setup: async (ctx) => {
    await ctx.tool.hook("execute.after", async (event) => {
      if (event.status !== "completed" || !LOGGED_TOOLS.has(event.tool)) return

      const directory = join(ctx.location.directory, LOG_DIRECTORY)
      const line = `${JSON.stringify({ tool: event.tool, status: event.status })}\n`

      await mkdir(directory, { recursive: true })
      await appendFile(join(directory, LOG_FILE), line, "utf8")
    })
  },
})
