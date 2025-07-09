import asyncio

async def coro(task, delay):
    await asyncio.sleep(delay)
    print(f'Задача {task} решена!')

async def start():
    await asyncio.gather(coro(1, 1), coro(2, 2), coro(3, 3))

asyncio.run(start())