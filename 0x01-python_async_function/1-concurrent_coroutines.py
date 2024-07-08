#!/usr/bin/env python3
"""
This module contains the wait_n coroutine.
"""
from typing import List
import asyncio
import importlib
# wait_random = __import__('0-basic_async_syntax').wait_random
wait_random = importlib.import_module('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawn wait_random n times with the specified max_delay and return the list
    of all the delays in ascending order.

    Args:
        n (int): The number of times to spawn wait_random.
        max_delay (int): The maximum number of seconds to wait.

    Returns:
        List[float]: List of all the delays in ascending order.
    """
    delays = await asyncio.gather(*(wait_random(max_delay) for _ in range(n)))
    return sorted(delays)
