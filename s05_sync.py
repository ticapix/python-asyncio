#!/usr/bin/env python3.5
import asyncio
from tools import debug, pause, timeme

data = [None, None]

@debug()
async def set_data(k, v):
	global data
	await asyncio.sleep(v)
	data[0] = k
	await asyncio.sleep(0.6)
	data[1] = v
	print(data)
	return v

@pause()
@timeme()
def sample01():
	"""- how to spwan multiple future in parallel
- no lock effect"""
	tasks = [
    	asyncio.ensure_future(set_data('a', 1.5)),
    	asyncio.ensure_future(set_data('b', 1)),
    	asyncio.ensure_future(set_data('c', 0.5))]
	loop.run_until_complete(asyncio.gather(*tasks))

#######################

lock = asyncio.Lock()

@debug()
async def set_data_lock(k, v):
	global data
	await asyncio.sleep(v)
	async with lock:
#	with await lock:
		data[0] = k
		await asyncio.sleep(0.6)
		data[1] = v
	print(data)
	return v

@pause()
@timeme()
def sample02():
	"""- how to spwan multiple future in parallel
- how to use the lock"""
	tasks = [
    	asyncio.ensure_future(set_data_lock('a', 1.5)),
    	asyncio.ensure_future(set_data_lock('b', 1)),
    	asyncio.ensure_future(set_data_lock('c', 0.5))]
	loop.run_until_complete(asyncio.gather(*tasks))


loop = asyncio.get_event_loop()
sample01()
sample02()
loop.close()
