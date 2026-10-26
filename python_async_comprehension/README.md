# Python - Async Comprehension

Asynchronous generators, asynchronous comprehensions and type annotations for generators.

## Files

| File | Description |
| --- | --- |
| `0-async_generator.py` | `async_generator()`: yields 10 random numbers between 0 and 10, waiting 1 second before each. |
| `1-async_comprehension.py` | `async_comprehension()`: collects the 10 numbers with an async comprehension. |
| `2-measure_runtime.py` | `measure_runtime()`: runs `async_comprehension` four times with `asyncio.gather` and returns the runtime (about 10 seconds). |

## Requirements

- Ubuntu 20.04 LTS, Python 3.8, files start with `#!/usr/bin/env python3`
- Code style checked with `pycodestyle`
- Every module and function is documented, and every function and coroutine is type-annotated
