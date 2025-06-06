from functools import wraps
import time
import logging
from typing import Any, Callable, TypeVar, cast, Optional

# 设置日志
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# 类型变量定义
F = TypeVar('F', bound=Callable[..., Any])

def mcp_interceptor(
    func: Optional[F] = None,
    *,
    log_args: bool = True,
    log_result: bool = True,
    log_time: bool = True
) -> Callable[[F], F]:
    """
    FastMCP 工具函数拦截器装饰器
    
    Args:
        func: 被装饰的函数
        log_args: 是否记录参数
        log_result: 是否记录结果
        log_time: 是否记录执行时间
    """
    def decorator(func: F) -> F:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            # 记录开始时间
            start_time = time.time()
            
            # 记录请求信息
            logger.info(f"开始执行 {func.__name__}")
            if log_args:
                logger.info(f"参数: args={args}, kwargs={kwargs}")
            
            try:
                # 执行原函数
                result = func(*args, **kwargs)
                
                # 记录执行时间
                if log_time:
                    execution_time = time.time() - start_time
                    logger.info(f"执行时间: {execution_time:.2f}秒")
                
                # 记录结果
                if log_result:
                    logger.info(f"执行结果: {result}")
                
                logger.info(f"成功完成 {func.__name__}")
                return result
                
            except Exception as e:
                # 记录异常
                logger.error(f"执行 {func.__name__} 时发生错误: {str(e)}")
                raise
                
        return cast(F, wrapper)
    
    if func is None:
        return decorator
    return decorator(func) 