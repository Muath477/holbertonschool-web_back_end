#!/usr/bin/env python3
"""Run several wait_random tasks at the same time."""
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Spawn task_wait_random n times and return the delays in ascending order.

    as_completed yields the tasks in the order they finish, so the delays come
    back already sorted.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    return [await finished for finished in asyncio.as_completed(tasks)]
