#!/usr/bin/env python3
import sys
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import uvicorn
import json
import os

current_dir = os.path.dirname(__file__)
if current_dir not in sys.path:
    sys.path.append(current_dir)
from tools.analyze_project_structure import analyze_project_structure
from tools.check_config_health import check_config_health
from tools.optimize_dev_environment import optimize_dev_environment

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class MCPRequest(BaseModel):
    jsonrpc: str = "2.0"
    method: str
    params: dict = {}
    id: int | str | None = None


@app.post("/mcp")
async def handle_mcp(request: MCPRequest):
    if request.method == "initialize":
        result = {
            "protocolVersion": "2024-11-05",
            "capabilities": {"tools": {"listChanged": True}},
            "serverInfo": {"name": "DevTools Assistant", "version": "1.0.0"},
        }
        return {"jsonrpc": "2.0", "id": request.id or 0, "result": result}
    elif request.method == "notifications/initialized":
        return {}
    elif request.method == "tools/list":
        tools = [
            {
                "name": "analyze_project_structure",
                "description": "Analyze project organization and suggest improvements.",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "project_path": {
                            "type": "string",
                            "description": "The absolute path to the project directory.",
                        }
                    },
                    "required": ["project_path"],
                },
            },
            {
                "name": "check_config_health",
                "description": "Validate configuration files for best practices.",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "project_path": {
                            "type": "string",
                            "description": "The absolute path to the project directory.",
                        }
                    },
                    "required": ["project_path"],
                },
            },
            {
                "name": "optimize_dev_environment",
                "description": "Suggest development environment optimizations.",
                "inputSchema": {"type": "object", "properties": {}, "required": []},
            },
        ]
        result = {"tools": tools}
        return {"jsonrpc": "2.0", "id": request.id or 0, "result": result}
    elif request.method == "tools/call":
        tool_name = request.params.get("name")
        arguments = request.params.get("arguments", {})
        try:
            if tool_name == "analyze_project_structure":
                project_path = arguments.get("project_path")
                if not project_path:
                    raise ValueError("Missing required parameter: project_path")
                result_data = analyze_project_structure(project_path)
            elif tool_name == "check_config_health":
                project_path = arguments.get("project_path")
                if not project_path:
                    raise ValueError("Missing required parameter: project_path")
                result_data = check_config_health(project_path)
            elif tool_name == "optimize_dev_environment":
                result_data = optimize_dev_environment()
            else:
                raise ValueError(f"Unknown tool: {tool_name}")
            result = {
                "content": [{"type": "text", "text": json.dumps(result_data, indent=2)}]
            }
            return {"jsonrpc": "2.0", "id": request.id or 0, "result": result}
        except Exception as e:
            return {
                "jsonrpc": "2.0",
                "id": request.id or 0,
                "error": {"code": -32603, "message": str(e)},
            }
    return {
        "jsonrpc": "2.0",
        "id": request.id or 0,
        "error": {"code": -32601, "message": f"Method not found: {request.method}"},
    }


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
