#!/usr/bin/env python3.5
from tools import debug, timeme, pause, burn_cpu
import time
import asyncio
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor, wait, as_completed
import subprocess


@debug()
def compute(y):
	# http://stackoverflow.com/questions/92928/time-sleep-sleeps-thread-or-process?answertab=votes#tab-top
	# time.sleep(0.1)
	burn_cpu(0.2)
	return pow(2, y)


@pause()
@timeme()
def pool01():
	"""sample of ThreadPoolExecutor
- unordered execution with executor.submit()
- dispatch among workers
- future.result()
- demo of a synch point with wait() (partial join with [:3])
- GIL"""
	with ThreadPoolExecutor(max_workers=3) as executor:
		futures = [executor.submit(compute, i) for i in range(6)]
		wait(futures[:3])
		print([(f.done(), f.result()) for f in futures])

@pause()
@timeme()
def pool02():
	"""sample of ThreadPoolExecutor
- unordered execution with executor.submit()
- dispatch among workers
- future.result()
- ordered iterator with as_completed()
- GIL"""
	with ThreadPoolExecutor(max_workers=3) as executor:
		futures = [executor.submit(compute, i) for i in range(6)]
		ans = []
		for future in as_completed(futures):
			ans.append(future.result())
		print(ans)

@pause()
@timeme()
def pool03():
	"""sample of ThreadPoolExecutor
- unordered execution with executor.map()
- dispatch among workers
- map return value: iterator vs Future for error handling
- GIL"""
	with ThreadPoolExecutor(max_workers=3) as executor:
		futures = executor.map(compute, range(6))
		print([f for f in futures])

@pause()
@timeme()
def pool10():
	"""sample of ThreadPoolExecutor
- ordered execution with map()
"""
	with ThreadPoolExecutor(max_workers=3) as executor:
		futures = map(compute, range(6))
		print([f for f in futures])

@pause()
@timeme()
def pool20():
	"""sample of ProcessPoolExecutor
- unordered execution with executor.map()
- dispatch among process
- map return value: iterator vs Future for error handling
- no GIL"""
	with ProcessPoolExecutor(max_workers=3) as executor:
		futures = executor.map(compute, range(6), chunksize=2)
		print([f for f in futures])


pool01()
pool02()
pool03()
pool10()
pool20()
