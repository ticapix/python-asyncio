#!/usr/bin/env python3.5
import asyncio
from tools import debug, pause
from concurrent.futures import CancelledError

counter = 0
loop = None

@debug()
async def compute01(future):
    global counter
    counter += 1
    if not future.cancelled():
        future.set_result('Future is done! (count={})'.format(counter))

@debug()
def got_result(future):
    global loop
    print(future.result())
    loop.stop()

@pause()
def sample01():
    """- sample with a callback
- use of a global
- loop.stop() vs loop.close()"""
    global loop
    loop = asyncio.get_event_loop()
    future = asyncio.Future()
    asyncio.ensure_future(compute01(future))
    future.add_done_callback(got_result)
    loop.run_forever()

@debug()
async def compute02(future):
    future.cancel()

@pause()
def sample02():
    """- sample with run_until_complete
- future cancellation with try/except"""
    global loop
    future = asyncio.Future()
    asyncio.ensure_future(compute02(future))
    try:
        loop.run_until_complete(future)
        print(future.result())
    except CancelledError as e:
        print('future cancelled', e)
    loop.close()

sample01()
sample02()
