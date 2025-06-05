import pytest
# 根据你的实际包名导入 Client
from fastmcp.client import Client

@pytest.mark.asyncio
async def test_mcp():
    async with Client("http://127.0.0.1:8081/sse") as mcp_client:
        tools = await mcp_client.list_tools()
        print(f"test1 Available tools: {tools}")
        result = await mcp_client.call_tool("add", {"a": 5, "b": 3})
        print(f"Result: {result[0].text}")
        # 测试 greeting 资源
        greeting = await mcp_client.read_resource(f"greeting://猴子")
        print(f"Greeting: {greeting}")
        assert "猴子" in greeting[0].text

@pytest.mark.asyncio
async def test_mcp2():
    async with Client("http://127.0.0.1:8081/sse") as mcp_client:
        tools = await mcp_client.list_tools()
        print(f"test2 Available tools: {tools}")