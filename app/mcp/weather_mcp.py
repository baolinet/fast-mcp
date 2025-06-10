import uvicorn
from fastmcp import FastMCP
from fastapi import FastAPI, Response
from starlette.routing import Mount
from starlette.applications import Starlette
 
mcp = FastMCP("weather-sse")
api = FastAPI(
    version="1.0.0",
    title="测试服务",
    description="FastAPI 测试服务器"
)
 
@api.get("/")
async def index():
    return Response(content="welcome to index", media_type="text/plain")
 
@mcp.tool()
@api.get("/weather")
def get_weather(location: str="Beijing") -> str:
    """获取指定地点的天气预报。
    参数：
        location (str): 城市名，如 'Beijing'。
    返回：
        str: 天气信息。
    """
    # 模拟天气数据
    weather_info = {
        "temperature": 27,
        "condition": "晴",
        "humidity": 65,
        "wind": "东北风3-4级"
    }
    return f"{location}的天气：温度 {weather_info['temperature']}°C，{weather_info['condition']}，湿度{weather_info['humidity']}%，{weather_info['wind']}"
 
 
app = Starlette(
    routes=[
        Mount('/api', app=api),
        Mount('/', app=mcp.sse_app()),
    ]
)
 
if __name__ == '__main__':
    # mcp.run(transport="sse")
    # uvicorn server:app --host 0.0.0.0 --port 5000
    uvicorn.run("__main__:app",host="127.0.0.1",port=5000,reload=False);