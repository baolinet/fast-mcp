from fastmcp import FastMCP
from app.mcp.friend_mcp import friend_mcp

# Create a basic server instance
main_mcp = FastMCP(name="MyAssistantServer")

# You can also add instructions for how to interact with the server
mcp_with_instructions = FastMCP(
    name="HelpfulAssistant",
    instructions="""
        This server provides data analysis tools.
        Call get_average() to analyze numerical data.
    """,
)

main_mcp.mount("friend", friend_mcp)
