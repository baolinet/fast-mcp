from app.mcp.mcp_server import mcp
from app.core.config import settings

if __name__ == "__main__":
    mcp.run(
        transport="sse",
        host="0.0.0.0",
        port=settings.PORT
    )