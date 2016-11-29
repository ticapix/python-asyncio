#!/usr/bin/env python3.5
import asyncio


# https://www.python.org/dev/peps/pep-0492/#asynchronous-context-managers-and-async-with

class Test(object):
    async def __aenter__(self):
        print("enter")

    async def __aexit__(self, *args):
        print("exit")

    def __await__(self):
        return self.__aenter__().__await__()

async def run():
    async with Test():
        print("hello")
    await Test()

loop = asyncio.get_event_loop()
loop.run_until_complete(run())
loop.close()
