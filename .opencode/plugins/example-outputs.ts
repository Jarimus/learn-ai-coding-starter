import { spawn } from "node:child_process"
import { readdir } from "node:fs/promises"
import { join } from "node:path"

import { Plugin } from "@opencode/plugin"

interface RunResult {
  stdout: string
  exitCode: number | null
}

interface ExampleOutput {
  name: string
  exitCode: number | null
  firstLine: string
}

function runExample(file: string, cwd: string, signal?: AbortSignal): Promise<RunResult> {
  return new Promise((resolve, reject) => {
    const child = spawn("uv", ["run", "--no-active", "sloperator.py", file], { cwd, signal })

    let stdout = ""

    child.stdout.setEncoding("utf8")
    child.stdout.on("data", (chunk: string) => {
      stdout += chunk
    })
    child.stderr.resume()

    child.on("error", reject)
    child.on("close", (exitCode) => resolve({ stdout, exitCode }))
  })
}

export default Plugin.define({
  id: "sloperator.example-outputs",
  setup: async (ctx) => {
    await ctx.tool.transform((tools) => {
      tools.add({
        name: "example_outputs",
        description:
          "Run every examples/*.slop program and return an examples array with each filename, exit code, and first output line as JSON.",
        input: {
          type: "object",
          properties: {},
          required: [],
          additionalProperties: false,
        },
        options: { codemode: false },
        execute: async (_input, context) => {
          const directory = join(ctx.location.directory, "examples")
          const entries = await readdir(directory, { withFileTypes: true })
          const names = entries
            .filter((entry) => entry.isFile() && entry.name.endsWith(".slop"))
            .map((entry) => entry.name)
            .sort()

          const examples: ExampleOutput[] = []
          for (const name of names) {
            const result = await runExample(
              join(directory, name),
              ctx.location.directory,
              context.signal,
            )
            examples.push({
              name,
              exitCode: result.exitCode,
              firstLine: result.stdout.split("\n", 1)[0] ?? "",
            })
          }

          return { content: JSON.stringify({ examples }, null, 2) }
        },
      })
    })
  },
})
