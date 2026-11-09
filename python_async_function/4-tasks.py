#!/usr/bin/env python3
"""Tasks."""

import asyncio

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> list[float]:
    """Spawn task_wait_random n times and return delays in ascending order."""
    tasks = []

    for _ in range(n):
        tasks.append(task_wait_random(max_delay))

    delays = []

    for task in asyncio.as_completed(tasks):
        delays.append(await task)

    return delays
