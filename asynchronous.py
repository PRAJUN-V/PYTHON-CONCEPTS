import asyncio

async def say_hello(delay):
    await asyncio.sleep(delay)
    print("Hello, world!")

async def main():
    print("Starting...")
    await asyncio.gather(
        say_hello(1),
        say_hello(2),
        say_hello(10)
    )
    print("Finished!")

asyncio.run(main())
