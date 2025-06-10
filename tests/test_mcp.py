import asyncio
import pytest
# 根据你的实际包名导入 Client
from fastmcp.client import Client


async def main():
    # 测试 mcp 客户端的功能
    async with Client("http://127.0.0.1:8081/sse") as mcp_client:
        tools = await mcp_client.list_tools()
        print(f"Available tools: {tools}")
        result = await mcp_client.call_tool("friend_add", {"a": 5, "b": 3})
        print(f"Result: {result[0].text}")

if __name__ == "__main__":
    asyncio.run(main())