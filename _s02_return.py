#!/usr/bin/env python3.5
import asyncio
from tools import debug

@debug()
async def coro_add(n):
    return n+n


@debug()
async def coro_mult(n):
    return n*n


async def compute(num):
	print('{n}+{n}={}, {n}*{n}={}'.format(
		await coro_add(num),
		await coro_mult(num),
		n=num))
	return 42

loop = asyncio.get_event_loop()
loop.run_until_complete(compute(7))
loop.close()
