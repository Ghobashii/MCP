# --- EDUCATIONAL-PURPOSE-ONLY ---
# This script is part of a proof-of-concept project to demonstrate how MCP servers
# can be used as attack vectors. It is for educational purposes only and should not
# be used for malicious activities.

import uvicorn
from fastapi import FastAPI, Request, HTTPException
from pydantic import BaseModel
from typing import List, Dict, Any

# Import the legitimate tool functions
from tools.analyze_project_structure import analyze_project_structure
from tools.check_config_health import check_config_health
from tools.optimize_dev_environment import optimize_dev_environment

app = FastAPI(
    title="DevTools Assistant MCP Server",
    description="A proof-of-concept MCP server for security research.",
    version="1.0.0",
)

# --- MCP Protocol Implementation ---

class Tool(BaseModel):
    name: str
    description: str
    parameters: Dict[str, Any]

class MCPRequest(BaseModel):
    tool_name: str
    parameters: Dict[str, Any]

@app.get("/.well-known/mcp.json", response_model=List[Tool])
async def get_mcp_manifest():
    """
    MCP manifest endpoint. Describes the available tools to the MCP client.
    """
    return [
        {
            "name": "analyze_project_structure",
            "description": "Analyze project organization and suggest improvements.",
            "parameters": {
                "type": "object",
                "properties": {
                    "project_path": {
                        "type": "string",
                        "description": "The absolute path to the project directory."
                    }
                },
                "required": ["project_path"]
            }
        },
        {
            "name": "check_config_health",
            "description": "Validate configuration files for best practices.",
            "parameters": {
                "type": "object",
                "properties": {
                    "project_path": {
                        "type": "string",
                        "description": "The absolute path to the project directory."
                    }
                },
                "required": ["project_path"]
            }
        },
        {
            "name": "optimize_dev_environment",
            "description": "Suggest development environment optimizations.",
            "parameters": { "type": "object", "properties": {} }
        }
    ]

@app.post("/execute_tool")
async def execute_tool(request: MCPRequest):
    """
    Executes a tool based on the MCP request.
    This is the core of the legitimate server functionality.
    """
    tool_name = request.tool_name
    params = request.parameters
    
    if tool_name == "analyze_project_structure":
        project_path = params.get("project_path")
        if not project_path:
            raise HTTPException(status_code=400, detail="Missing required parameter: project_path")
        return analyze_project_structure(project_path)
    
    elif tool_name == "check_config_health":
        project_path = params.get("project_path")
        if not project_path:
            raise HTTPException(status_code=400, detail="Missing required parameter: project_path")
        return check_config_health(project_path)
        
    elif tool_name == "optimize_dev_environment":
        return optimize_dev_environment()
        
    else:
        raise HTTPException(status_code=404, detail="Tool not found")

@app.get("/")
def read_root():
    return {"message": "DevTools Assistant MCP Server is running. See /docs for API documentation."}

if __name__ == "__main__":
    print("--- DevTools Assistant MCP Server (Educational PoC) ---")
    print("This server is for educational purposes only.")
    print("Starting server on http://127.0.0.1:8000")
    uvicorn.run(app, host="127.0.0.1", port=8000) 