#!/usr/bin/env python3.5
import asyncio
from tools import debug, pause

@debug()
async def coro01(n):
    await asyncio.sleep(0.5)
    return n*n

@debug()
@asyncio.coroutine
def coro02():
    num = 7
    print('result: {n}*{n}={}'.format((yield from coro01(num)), n=num))
    return 'Completed !'

# async def coro03():
#     return (yield from asyncio.sleep(0.5))
#             ^
# SyntaxError: 'yield from' inside async function

# @asyncio.coroutine
# def coro04():
#     return await asyncio.sleep(0.5)
#                        ^
# SyntaxError: invalid syntax

@pause()
def sample01():
    """- basic event-loop
- return value
- no syntax mix up"""
    loop = asyncio.get_event_loop()
    # Blocking call which returns when the hello_world() coroutine is done
    print('The loop is', loop.run_until_complete(coro02()))
    loop.close()

@pause()
def func_vs_obj():
    """- table showing the diff between the function and the object
- demo of the str.format() builtin (https://pyformat.info/)
- default warning when a coroutine obj is not scheduled"""
    print('{:^10} | {:^10} | {:^10}'.format('', 'coro func', 'coro obj'))
    for code in ['coro01', 'coro01()']:
        obj = eval(code)
        print('{:^10} | {:^10} | {:^10} | {:^10}'.format(code, asyncio.iscoroutinefunction(obj), asyncio.iscoroutine(obj), str(obj)))


sample01()
func_vs_obj()