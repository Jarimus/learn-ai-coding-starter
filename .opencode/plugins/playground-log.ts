import { appendFile, mkdir } from "node:fs/promises"
import { join } from "node:path"

import { Plugin } from "@opencode/plugin"

const PLAYGROUND_SERVER = "playground/server.py"
const LOG_DIRECTORY = "logs"
const LOG_FILE = "plugin-playground.log"
const LOG_MESSAGE = "playground shell request\n"

export default Plugin.define({
  id: "sloperator.playground-log",
  setup: async (ctx) => {
    await ctx.shell.hook("create.before", async (event) => {
      if (!event.command.includes(PLAYGROUND_SERVER)) return

      const directory = join(ctx.location.directory, LOG_DIRECTORY)
      await mkdir(directory, { recursive: true })
      await appendFile(join(directory, LOG_FILE), LOG_MESSAGE, "utf8")
    })
  },
})
