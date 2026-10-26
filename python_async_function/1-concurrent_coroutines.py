#!/usr/bin/env python3
"""Run several wait_random coroutines at the same time."""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Spawn wait_random n times and return the delays in ascending order.

    as_completed yields the coroutines in the order they finish, which is the
    order of their delays, so no sorting is needed.
    """
    coroutines = [wait_random(max_delay) for _ in range(n)]
    return [await finished for finished in asyncio.as_completed(coroutines)]
