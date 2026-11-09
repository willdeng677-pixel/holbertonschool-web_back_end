#!/usr/bin/env python3

import asyncio

async_generator = __import__('5-basic_async_generator').async_generator


async def main():
    async for number in async_generator():
        print(number)


asyncio.run(main())
