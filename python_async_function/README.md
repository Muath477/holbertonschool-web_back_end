# Python - Async Function

Basics of asynchronous programming with `asyncio`: coroutines, running them concurrently, measuring the runtime and
creating tasks.

## Files

| File | Description |
| --- | --- |
| `0-basic_async_syntax.py` | `wait_random(max_delay)`: waits a random delay and returns it. |
| `1-concurrent_coroutines.py` | `wait_n(n, max_delay)`: runs `wait_random` n times and returns the delays in ascending order, without `sort()`. |
| `2-measure_runtime.py` | `measure_time(n, max_delay)`: total runtime of `wait_n` divided by n. |
| `3-tasks.py` | `task_wait_random(max_delay)`: returns an `asyncio.Task`. |
| `4-tasks.py` | `task_wait_n(n, max_delay)`: like `wait_n`, built on `task_wait_random`. |

## Requirements

- Python 3.9, files start with `#!/usr/bin/env python3`
- Code style checked with `pycodestyle`
- Every function is documented and type-annotated
