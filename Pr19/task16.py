import asyncio

async def worker(n):
    await asyncio.sleep(n)
    print(f"Worker {n} finished")

async def main():
    await asyncio.gather(
        worker(1),
        worker(2),
        worker(3)
    )

asyncio.run(main())
