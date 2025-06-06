import time
import logging
from functools import wraps
# 设置日志
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def mcp_interceptor(func):
    """
    FastMCP 工具函数拦截器
    """
    @wraps(func)
    async def wrapper(a: int = None, b: int = None, name: str = None):
        # 前置处理
        print("请求开始")
        logger.info(f"参数: a={a}, b={b}, name={name}")

        try:
            # 根据参数调用原函数
            if a is not None and b is not None:
                result = await func(a=a, b=b)
            elif name is not None:
                result = await func(name=name)
            else:
                result = await func()
                
            # 后置处理
            print("请求成功")
            return result
        except Exception as e:
            # 异常处理
            print(f"请求失败: {e}")
            raise
            
    return wrapper