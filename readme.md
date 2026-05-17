# MCP Server — Random Number Generator

This is a simple MCP server built with FastMCP. Give it a number `n` and it gives back an array of `n` random numbers. That's it!

---

## Setting up in VS Code (GitHub Copilot)

To use this server as a tool inside GitHub Copilot chat, you need a `.vscode/mcp.json` file in your project. Create it with this content:

```json
{
  "servers": {
    "mcp-server": {
      "type": "stdio",
      "command": "C:\\Users\\<your-username>\\.local\\bin\\uv.exe",
      "args": [
        "--directory",
        "c:\\projects\\mcp_server",
        "run",
        "fastmcp",
        "run",
        "c:\\projects\\mcp_server\\main.py:server"
      ]
    }
  }
}
```

Replace `<your-username>` with your Windows username. Once VS Code detects this file, it'll ask you to start the server. After that, the `generate_random_numbers` tool shows up in Copilot agent mode.

---

## Setting up in Claude Desktop

Add this to your `claude_desktop_config.json` under `mcpServers`:

```json
"mcp-server": {
  "command": "C:\\Users\\<your-username>\\.local\\bin\\uv.exe",
  "args": [
    "--directory",
    "c:\\projects\\mcp_server",
    "run",
    "fastmcp",
    "run",
    "c:\\projects\\mcp_server\\main.py:server"
  ]
}
```

Restart Claude Desktop after saving.

---

## Install & Run

pip install uv

python -m venv .venv
.venv/Scripts/activate
pip install -r requirements.txt

to run the server
python main.py


to test the server workin insoection
```
uv run fastmcp dev inspector main.py:server
```