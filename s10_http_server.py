#!/usr/bin/env python3.5
import asyncio
from aiohttp import web
from tools import debug

@debug()
async def handle(request):
    name = request.match_info.get('name', "Anonymous")
    text = "Hello, " + name
    await SomeFakeDBOperation()
    return web.Response(text=text)


async def SomeFakeDBOperation():
	await asyncio.sleep(1)


app = web.Application()
app.router.add_get('/', handle)
app.router.add_get('/{name}', handle)

web.run_app(app, port=8080)
