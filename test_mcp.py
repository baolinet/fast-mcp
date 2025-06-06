import asyncio
from fastmcp import Client
from app.mcp_server import main_mcp 

# Example transports (more details in Transports page)
sse_url = "http://localhost:8081/sse"       # SSE server URL

# Client automatically infers the transport type
client_sse = Client(sse_url)

print(client_sse.transport)

async def main():
    # Connection is established here
    async with client_sse:
        print(f"Client connected: {client_sse.is_connected()}")

        # Make MCP calls within the context
        tools = await client_sse.list_tools()
        print(f"Available tools: {tools}")

        resources = await client_sse.list_resources()
        print(f"Available resources: {resources}")

        templates = await client_sse.list_resource_templates()
        print(f"Available resource templates: {templates}")

        result = await client_sse.call_tool("friend_mockey", {"name": "猴子"})
        print(f"Tool result: {result}")

    # Connection is closed automatically here
    print(f"Client connected: {client_sse.is_connected()}")


if __name__ == "__main__":
    asyncio.run(main())