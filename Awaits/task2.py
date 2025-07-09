import asyncio

async def delayed_print(text, delay):
    await asyncio.sleep(delay)
    print(text)


async def run():
    task1 = asyncio.create_task(delayed_print("Привет", 1))
    task2 = asyncio.create_task(delayed_print("я Паша", 2))

    await task1
    await task2

asyncio.run(run())