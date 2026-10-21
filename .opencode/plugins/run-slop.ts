import { spawn } from "node:child_process"

import { Plugin } from "@opencode/plugin"

interface RunSlopResult {
  stdout: string
  stderr: string
  exitCode: number | null
}

function runSloperator(file: string, cwd: string, signal?: AbortSignal): Promise<RunSlopResult> {
  return new Promise((resolve, reject) => {
    const child = spawn("uv", ["run", "--no-active", "sloperator.py", file], {
      cwd,
      signal,
    })

    let stdout = ""
    let stderr = ""

    child.stdout.setEncoding("utf8")
    child.stdout.on("data", (chunk: string) => {
      stdout += chunk
    })

    child.stderr.setEncoding("utf8")
    child.stderr.on("data", (chunk: string) => {
      stderr += chunk
    })

    child.on("error", reject)
    child.on("close", (exitCode) => resolve({ stdout, stderr, exitCode }))
  })
}

export default Plugin.define({
  id: "sloperator.run-slop",
  setup: async (ctx) => {
    await ctx.tool.transform((tools) => {
      tools.add({
        name: "run_slop",
        description:
          "Run a SlopLang program with Sloperator and return stdout, stderr, and the exit code as JSON.",
        input: {
          type: "object",
          properties: {
            path: {
              type: "string",
              description:
                "Path to the .slop file, relative to the project root or absolute.",
            },
          },
          required: ["path"],
          additionalProperties: false,
        },
        options: { codemode: false },
        execute: async (input, context) => {
          const { path } = input as { path: string }
          const result = await runSloperator(path, ctx.location.directory, context.signal)
          return { content: JSON.stringify(result, null, 2) }
        },
      })
    })
  },
})
