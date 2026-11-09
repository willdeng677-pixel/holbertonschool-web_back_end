#!/usr/bin/env python3
"""Basic asynchronous generator."""

import asyncio
import random


async def async_generator():
    """Asynchronously generate 10 random numbers."""
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
