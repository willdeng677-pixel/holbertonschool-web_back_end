#!/usr/bin/env python3
"""Concurrent coroutines."""

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> list[float]:
    """Spawn wait_random n times and return delays in ascending order."""
    delays = []

    for _ in range(n):
        delays.append(asyncio.create_task(wait_random(max_delay)))

    results = []

    for task in asyncio.as_completed(delays):
        results.append(await task)

    return results
