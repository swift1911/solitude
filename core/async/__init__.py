import asyncio


async def io(x, y):
    await asyncio.sleep(2)
    print(x + y)


@asyncio.coroutine
def io_deco(x, y):
    yield from asyncio.sleep(2)
    print(x + y)


loop = asyncio.get_event_loop()
tasks = [
    asyncio.ensure_future(io(1, 2)),
    asyncio.ensure_future(io(2, 3)),
    asyncio.ensure_future(io_deco(2, 4))

]
try:
    loop.run_until_complete(asyncio.wait(tasks))

finally:
    loop.close()