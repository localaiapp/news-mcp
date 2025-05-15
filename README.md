# Fake News Detection

A tool for detecting fake news using MCP.



## MCP Configuration

Add this to your MCP's package.json:

```json
{
  "mcpServers": {
    "fakenews": {
      "command": "uvx",
      "args": [
        "--from",
        "git+https://github.com/localaiapp/news-mcp.git", "mcp-fakenews"
      ],
      "env": {}
    }
  }
}
``` 