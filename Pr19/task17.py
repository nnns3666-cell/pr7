import asyncio

async def delayed_task(delay):
    await asyncio.sleep(delay)
    print(f"Finished after {delay} sec")

async def main():
    tasks = [delayed_task(i) for i in [3, 1, 5, 2, 4]]
    await asyncio.gather(*tasks)

asyncio.run(main())
