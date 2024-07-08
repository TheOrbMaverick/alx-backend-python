#!/usr/bin/env python3
"""
This module contains the task_wait_random function.
"""
import asyncio
from importlib import import_module

wait_random = import_module('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Takes an integer max_delay and returns an asyncio.Task.

    Args:
        max_delay (int): The maximum number of seconds to wait.

    Returns:
        asyncio.Task: A task that waits for a random delay.
    """
    return asyncio.create_task(wait_random(max_delay))
