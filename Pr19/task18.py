import asyncio

async def read_file(name):
    print(f"Reading {name}...")
    await asyncio.sleep(2)
    print(f"{name} read complete")

async def main():
    await asyncio.gather(
        read_file("file1.txt"),
        read_file("file2.txt")
    )

asyncio.run(main())
