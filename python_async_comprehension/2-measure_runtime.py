#!/usr/bin/env python3
"""Measure the runtime of four async comprehensions running in parallel."""
import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Run async_comprehension four times in parallel and return the runtime.

    The four runs wait at the same time, so the total is about 10 seconds
    (one run) and not 40.
    """
    start = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    return time.perf_counter() - start
