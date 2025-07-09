import asyncio
import random


async def fetch_data(index):
    await asyncio.sleep(random.randint(1, 5))
    print(f"Данные {index} получены")

async def fetch_data1(index1):
    await asyncio.sleep(random.randint(1, 5))
    print(f"Данные {index1} получены")


async def fetch_data2(index2):
    await asyncio.sleep(random.randint(1, 5))
    print(f"Данные {index2} получены")


async def fetch_data3(index3):
    await asyncio.sleep(random.randint(1, 5))
    print(f"Данные {index3} получены")


async def fetch_data4(index4):
    await asyncio.sleep(random.randint(1, 5))
    print(f"Данные {index4} получены")



async def start():
    await asyncio.gather(fetch_data('1'), fetch_data1("2"), fetch_data2('3'), fetch_data3('4'), fetch_data4('5'))

asyncio.run(start())