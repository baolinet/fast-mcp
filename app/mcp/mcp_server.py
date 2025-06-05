# server.py
from fastmcp import FastMCP

# Create an MCP server
mcp = FastMCP(name = "FastMCP 智能体平台")

# Add an addition tool
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

# Add a dynamic greeting resource
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"

@mcp.tool()
def mockey(name: str) -> str:
    """外号叫猴子的人"""
    return "猴子的本名叫孙悟空"
