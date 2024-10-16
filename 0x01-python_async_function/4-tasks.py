#!/usr/bin/env python3
"""Test file for printing the correct output of the wait_n coroutine"""
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """wait_n"""
    task = [task_wait_random(max_delay) for _ in range(n)]
    result = await asyncio.gather(*task)
    return (result)
