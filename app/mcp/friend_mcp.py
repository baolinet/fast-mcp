from fastmcp import FastMCP

# Create a basic server instance
friend_mcp = FastMCP(name="我的朋友")

# Add an addition tool
@friend_mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

# Add a dynamic greeting resource
@friend_mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"

@friend_mcp.tool()
def mockey(name: str) -> str:
    """外号叫猴子的人"""
    return "猴子的本名叫孙悟空"


# @friend_mcp.tool
# def multiply(a: float, b: float) -> float:
#     """Multiplies two numbers together."""
#     return a * b

# @friend_mcp.resource("data://config")
# def get_config() -> dict:
#     """Provides the application configuration."""
#     return {"theme": "dark", "version": "1.0"}

# @friend_mcp.resource("users://{user_id}/profile")
# def get_user_profile(user_id: int) -> dict:
#     """Retrieves a user's profile by ID."""
#     # The {user_id} in the URI is extracted and passed to this function
#     return {"id": user_id, "name": f"User {user_id}", "status": "active"}

# @friend_mcp.prompt
# def analyze_data(data_points: list[float]) -> str:
#     """Creates a prompt asking for analysis of numerical data."""
#     formatted_data = ", ".join(str(point) for point in data_points)
#     return f"Please analyze these data points: {formatted_data}"