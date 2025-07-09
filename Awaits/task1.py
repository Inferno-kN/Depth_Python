import asyncio

class MyClass:
    def run(self):
        asyncio.run(self.say_hello())


    async def say_hello(self):
        await asyncio.sleep(1)
        print("Привет")


if __name__ == '__main__':
    m = MyClass()
    m.run()