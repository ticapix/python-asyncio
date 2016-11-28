from functools import wraps, partial
from asyncio import iscoroutinefunction
import timeit

def debug():
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

def timeme():
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            ans = timeit.timeit(partial(func, *args, **kwargs), number=1)
            print('{:.42} tooks {:.2f} sec'.format(str(func), ans))
        return wrapper
    return decorator

def _burn_cpu():
    c = 0
    for i in range(10**4):
        c += 1

_unit_sec = timeit.timeit(_burn_cpu, number=5)/5

@timeme()
def burn_cpu(duration_sec):
    counter = duration_sec / _unit_sec
    while counter > 0:
        _burn_cpu()
        counter -= 1

def pause():
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(func.__doc__)
            input('\n{:>80}\n'.format('Press <ENTER> to continue'))
            ans = func(*args, **kwargs)
            input('\n{:>80}\n'.format('Press <ENTER> to continue'))
            return ans
        return wrapper
    return decorator
