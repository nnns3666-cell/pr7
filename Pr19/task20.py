import asyncio
import random

async def worker(name, queue):
    while True:
        task = await queue.get()

        print(f"{name} started {task}")
        await asyncio.sleep(random.randint(1, 3))
        print(f"{name} finished {task}")

        queue.task_done()

async def main():
    queue = asyncio.Queue()

    for i in range(10):
        await queue.put(f"Task-{i+1}")

    workers = [
        asyncio.create_task(worker("Worker-1", queue)),
        asyncio.create_task(worker("Worker-2", queue)),
        asyncio.create_task(worker("Worker-3", queue))
    ]

    await queue.join()

    for w in workers:
        w.cancel()

asyncio.run(main())
