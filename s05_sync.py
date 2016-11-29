#!/usr/bin/env python3.5
import asyncio
from tools import debug, pause

lock = asyncio.Lock()

data = [None, None]

@debug()
async def set_data(k, v):
	global data
	await asyncio.sleep(v)
	with await lock:
		data[0] = k
		await asyncio.sleep(0.6)
		data[1] = v
	print(data)
	return v

@pause()
def sample01():
	"""- how to spwan multiple future in parallel
- how to use the lock"""
	tasks = [
    	asyncio.ensure_future(set_data('a', 1.5)),
    	asyncio.ensure_future(set_data('b', 1)),
    	asyncio.ensure_future(set_data('c', 0.5))]
	loop.run_until_complete(asyncio.gather(*tasks))


@debug()
async def set_data2(k, v):
	global data
	await asyncio.sleep(v)
	data[0] = k
	await asyncio.sleep(0.6)
	data[1] = v
	print(data)
	return v

@pause()
def sample02():
	"""- how to spwan multiple future in parallel
- no lock effect"""
	tasks = [
    	asyncio.ensure_future(set_data2('a', 1.5)),
    	asyncio.ensure_future(set_data2('b', 1)),
    	asyncio.ensure_future(set_data2('c', 0.5))]
	loop.run_until_complete(asyncio.gather(*tasks))

loop = asyncio.get_event_loop()
sample02()
sample01()
loop.close()
