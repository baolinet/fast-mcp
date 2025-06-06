from app.mcp_server import main_mcp
from app.core.config import settings

if __name__ == "__main__":
    main_mcp.run(
        transport="sse",
        host="0.0.0.0",
        port=settings.PORT
    )
     # This runs the server, defaulting to STDIO transport
    # mcp.run()
    # To use a different transport, e.g., HTTP:
    # mcp.run(transport="streamable-http", host="127.0.0.1", port=9000)
