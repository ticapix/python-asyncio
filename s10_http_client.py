#!/usr/bin/env python3.5
import aiohttp
import asyncio
import async_timeout

async def fetch(session, url):
    with async_timeout.timeout(10):
        async with session.get(url) as response:
            return await response.text()

async def main(loop):
    async with aiohttp.ClientSession(loop=loop) as session:
        htmls = [await fetch(session, 'http://localhost:8080/A'),
        await fetch(session, 'http://localhost:8080/B')]
        print(htmls)
        tasks = [asyncio.ensure_future(fetch(session, 'http://localhost:8080/{}'.format(name)), loop=loop) for name in 'PYTHON']
        tasks += [loop.create_task(fetch(session, 'http://localhost:8080/{}'.format(name))) for name in 'FOREEVER']
        htmls = await asyncio.gather(*tasks)
        print(htmls)

#        print('{}\n{:.512}'.format(len(html), html))

loop = asyncio.get_event_loop()
loop.run_until_complete(main(loop))
