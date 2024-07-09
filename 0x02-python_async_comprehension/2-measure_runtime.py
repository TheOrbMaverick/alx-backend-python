#!/usr/bin/env python3
"""
This module contains the measure_runtime coroutine.
"""
import asyncio
import time
async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime() -> float:
    """
    Execute async_comprehension four times in parallel using asyncio.gather.
    Measure the total runtime and return it.

    Returns:
        float: The total runtime.
    """
    start_time = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end_time = time.time()
    return end_time - start_time
