#!/usr/bin/env python3

import asyncio

async_generator = __import__('5-basic_async_generator').async_generator


async def main():
    print([i async for i in async_generator()])


if __name__ == "__main__":
    asyncio.run(main())
