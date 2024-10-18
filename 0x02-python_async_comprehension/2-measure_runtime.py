#!/usr/bin/env python3
"""use asycio.gather"""

import asyncio
import time
from typing import List

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Execute async_comprehension four times in parallel and
    measure total runtime.
    Returns:
        float: Total time taken for all four executions to complete"""
    start_time = time.time()
    await asyncio.gather(
            async_comprehension(),
            async_comprehension(),
            async_comprehension(),
            async_comprehension()
            )
    end_time = time.time()
    total_time = end_time - start_time
    return total_time
