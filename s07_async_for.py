#!/usr/bin/env python3.5
import asyncio
from tools import debug, pause, timeme

class AsyncIteratorWrapper:
    def __init__(self, obj):
        self._it = iter(obj)

    def __aiter__(self):
        return self

    @debug()
    async def __anext__(self):
        try:
            value = next(self._it)
        except StopIteration:
            raise StopAsyncIteration
        return value

async def sample01():
    async for letter in AsyncIteratorWrapper("ASYNC PYTHON"):
        print(letter)

loop = asyncio.get_event_loop()
loop.run_until_complete(sample01())
loop.close()
