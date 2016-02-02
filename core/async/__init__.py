import asyncio
import random
import time

total = 0


async def io(x, y):
    global total
    s = time.time()
    await asyncio.sleep(random.random())
    print(x + y)
    print(time.time() - s)
    total += (time.time() - s)


@asyncio.coroutine
def io_deco(x, y):
    global total
    s = time.time()
    yield from asyncio.sleep(random.random())
    print(x + y)
    print(time.time() - s)
    total += (time.time() - s)


loop = asyncio.get_event_loop()
tasks = [
    asyncio.ensure_future(io(1, 2)),
    asyncio.ensure_future(io(2, 3)),
    asyncio.ensure_future(io_deco(2, 4))
]
try:
    loop.run_until_complete(asyncio.wait(tasks))
    print(total)
finally:
    loop.close()
