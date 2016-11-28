from functools import wraps
from asyncio import iscoroutinefunction

def debug(p=True):
    def decorator(func):
        @wraps(func)
        async def async_wrapper(*args, **kwargs):
            print('-> {:.42}'.format(str(func)))
            res = await func(*args, **kwargs)
            print('<- {:.40} (={:.40})'.format(str(func), str(res)))
            return res
        @wraps(func)
        def wrapper(*args, **kwargs):
            print('-> {:.42}'.format(str(func)))
            res = func(*args, **kwargs)
            print('<- {:.40} (={:.40})'.format(str(func), str(res)))
            return res
        return async_wrapper if iscoroutinefunction(func) else wrapper
    return decorator
