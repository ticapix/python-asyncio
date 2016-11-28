#!/usr/bin/env python3.5
from tools import debug, timeme
import time
import asyncio
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor, wait

@debug()
def compute(y):
	time.sleep(0.1)
	return pow(2, y)


@timeme()
def pool01():
	"""ThreadPoolExecutor: order of execution is not determined"""
	with ThreadPoolExecutor(max_workers=3) as executor:
		futures = [executor.submit(compute, i) for i in range(6)]
		wait(futures[:3])
		print([(f.done(), f.result()) for f in futures])

@timeme()
def pool02():
	"""ThreadPoolExecutor: order of execution is not determined"""
	with ThreadPoolExecutor(max_workers=3) as executor:
		futures = executor.map(compute, range(6))
		print([f for f in futures])

@timeme()
def pool03():
	"""ThreadPoolExecutor: order of execution is not determined"""
	with ThreadPoolExecutor(max_workers=3) as executor:
		futures = executor.map(compute, range(6))
		print([f for f in futures])

@timeme()
def pool10():
	"""ThreadPoolExecutor:order of execution is sequential"""
	with ThreadPoolExecutor(max_workers=3) as executor:
		futures = map(compute, range(6))
		print([f for f in futures])

@debug()
def compute_slow(y):
	time.sleep(.5)
	return pow(2, y)

@timeme()
def pool20():
	"""ProcessPoolExecutor: order of execution is not determined"""
	with ProcessPoolExecutor(max_workers=6) as executor:
		futures = executor.map(compute_slow, range(6), chunksize=3)
		print([f for f in futures])


pool01()
pool02()
pool03()
pool10()
pool20()
