import functools
from functools import wraps

def retry(max_retries=3) :
    """
    装饰器，用于重试函数最多 max_retries 次。
    如果函数在重试中成功，则返回其结果。
    如果在所有重试后失败，则返回所有异常的列表。
    """

    def decorator_retry(func) :
        @functools.wraps(func)
        def wrapper_retry(*args , **kwargs) :
            exceptions = []  # 存储所有异常
            for attempt in range(max_retries + 1) :
                try :
                    result = func(*args , **kwargs)
                    return result
                except Exception as e :
                    exceptions.append(e)
                    if attempt == max_retries :
                        return exceptions

        return wrapper_retry

    return decorator_retry

import time
from functools import wraps

def wait(func, wait_time=0.1):
    """
    装饰器：在方法开始和结束时分别等待指定的时间（默认0.02秒）
    :param func: 被装饰的函数
    :param wait_time: 等待时间，默认 0.02 秒
    :return: 被装饰的函数
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        time.sleep(wait_time)  # 等待开始
        result = func(*args, **kwargs)
        time.sleep(wait_time)  # 等待结束
        return result
    return wrapper

def wait_all_methods(cls):
    """
    类装饰器：为类中的所有方法添加等待装饰器
    :param cls: 需要装饰的类
    :return: 装饰后的类
    """
    # 遍历类的所有属性
    for attr_name, attr_value in cls.__dict__.items():
        # 仅装饰方法，不装饰其他属性
        if callable(attr_value):
            # 将 `wait` 装饰器应用于类中的每个方法
            decorated_method = wait(attr_value)
            setattr(cls, attr_name, decorated_method)
    return cls

