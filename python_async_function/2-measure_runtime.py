#!/usr/bin/env python3
"""Measure the average runtime of wait_n per spawned coroutine."""
import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Return the total execution time of wait_n(n, max_delay) divided by n."""
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    elapsed = time.time() - start
    return elapsed / n
