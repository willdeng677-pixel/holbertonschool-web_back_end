#!/usr/bin/env python3

import asyncio

async_comprehension = __import__(
    '6-async_comprehension'
).async_comprehension


async def main():
    print(await async_comprehension())


if __name__ == "__main__":
    asyncio.run(main())
