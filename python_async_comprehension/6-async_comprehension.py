#!/usr/bin/env python3
"""Async comprehension module."""

async_generator = __import__('5-basic_async_generator').async_generator


async def async_comprehension():
    """Collect 10 random numbers using async comprehension."""
    return [number async for number in async_generator()]
