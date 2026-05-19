import asyncio

async def hello():
    await asyncio.sleep(1)
    print("Hello after 1 second")

asyncio.run(hello())
