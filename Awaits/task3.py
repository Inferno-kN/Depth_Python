import asyncio

async def coro1(task1, delay):
    await asyncio.sleep(delay)
    print(task1)

async def coro2(task2, delay):
    await asyncio.sleep(delay)
    print(task2)

async def coro3(task3, delay):
    await asyncio.sleep(delay)
    print(task3)

async def start():
    await asyncio.gather(coro1('Задача 1', 1), coro2('Задача 2', 2), coro3('Задача 3', 3))

asyncio.run(start())