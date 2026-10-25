"""Tripo3D integration: text/image to 3D model.

Runs two ways:
  python tripo3d_tool.py serve                 # MCP server (used by Claude via .mcp.json)
  python tripo3d_tool.py text "a cute cat"     # command line
  python tripo3d_tool.py image cat.png
  python tripo3d_tool.py task <task_id>
  python tripo3d_tool.py balance

Needs the TRIPO_API_KEY environment variable (get a key at platform.tripo3d.ai).
"""

import argparse
import asyncio
import os

from tripo3d import TaskStatus, TripoClient, TripoPollTimeoutError

OUTPUT_DIR = os.environ.get("TRIPO_OUTPUT_DIR", "tripo_output")
# How long a generate call waits before handing back the task id to check later.
WAIT_SECONDS = 300


async def finish(client, task_id, timeout=WAIT_SECONDS):
    """Wait for a task, download its files, and describe the result."""
    try:
        task = await client.wait_for_task(task_id, timeout=timeout)
    except TripoPollTimeoutError:
        return f"Task {task_id} is still running. Check it later with the task id."

    if task.status != TaskStatus.SUCCESS:
        return f"Task {task_id} ended with status {task.status.value}: {task.error_msg or 'no details'}"

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    files = await client.download_task_models(task, OUTPUT_DIR)
    lines = [f"Task {task_id} finished."]
    for kind, path in files.items():
        if path:
            lines.append(f"  {kind}: {path}")
    return "\n".join(lines)


async def text_to_3d(prompt, negative_prompt=None):
    async with TripoClient() as client:
        task_id = await client.text_to_model(prompt=prompt, negative_prompt=negative_prompt)
        return await finish(client, task_id)


async def image_to_3d(image_path):
    async with TripoClient() as client:
        task_id = await client.image_to_model(image=image_path)
        return await finish(client, task_id)


async def check_task(task_id):
    async with TripoClient() as client:
        task = await client.get_task(task_id)
        if task.status in (TaskStatus.QUEUED, TaskStatus.RUNNING):
            return f"Task {task_id} is {task.status.value} ({task.progress}%)."
        return await finish(client, task_id, timeout=10)


async def balance():
    async with TripoClient() as client:
        b = await client.get_balance()
        return f"Balance: {b.balance} credits ({b.frozen} frozen)"


def serve():
    from mcp.server.mcpserver import MCPServer

    server = MCPServer("tripo3d", instructions="Generate 3D models (GLB) with Tripo3D.")

    @server.tool()
    async def tripo_text_to_3d(prompt: str, negative_prompt: str | None = None) -> str:
        """Generate a 3D model from a text prompt and download it. Spends Tripo credits."""
        return await text_to_3d(prompt, negative_prompt)

    @server.tool()
    async def tripo_image_to_3d(image_path: str) -> str:
        """Generate a 3D model from a local image file and download it. Spends Tripo credits."""
        return await image_to_3d(image_path)

    @server.tool()
    async def tripo_check_task(task_id: str) -> str:
        """Check a Tripo task and download its model once it has finished."""
        return await check_task(task_id)

    @server.tool()
    async def tripo_balance() -> str:
        """Show the remaining Tripo credit balance."""
        return await balance()

    server.run("stdio")


def main():
    parser = argparse.ArgumentParser(description="Tripo3D text/image to 3D")
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("serve", help="run as an MCP server")
    text = sub.add_parser("text", help="text prompt to 3D model")
    text.add_argument("prompt")
    text.add_argument("--negative", default=None)
    image = sub.add_parser("image", help="image file to 3D model")
    image.add_argument("path")
    task = sub.add_parser("task", help="check or download a task")
    task.add_argument("task_id")
    sub.add_parser("balance", help="show credit balance")
    args = parser.parse_args()

    if args.command == "serve":
        serve()
    elif args.command == "text":
        print(asyncio.run(text_to_3d(args.prompt, args.negative)))
    elif args.command == "image":
        print(asyncio.run(image_to_3d(args.path)))
    elif args.command == "task":
        print(asyncio.run(check_task(args.task_id)))
    else:
        print(asyncio.run(balance()))


if __name__ == "__main__":
    main()
