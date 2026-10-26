#!/usr/bin/env python3
"""Collect values from an asynchronous generator with a comprehension."""
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Return the 10 random numbers produced by async_generator."""
    return [number async for number in async_generator()]
