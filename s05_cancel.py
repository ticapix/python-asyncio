!/usr/bin/env python3.5
import asyncio
from tools import debug

counter = 0

@debug()
async def compute(future):
    global counter
    counter += 1
    future.set_result('Future is done! (count={})'.format(counter))

@debug()
def got_result(future):
    print(future.result())
    loop.stop()

loop = asyncio.get_event_loop()
future = asyncio.Future()
asyncio.ensure_future(compute(future))
future.add_done_callback(got_result)
loop.run_forever()

future = asyncio.Future()
asyncio.ensure_future(compute(future))
loop.run_until_complete(future)
print(future.result())
loop.close()
