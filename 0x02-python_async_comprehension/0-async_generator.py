#!/usr/bin/env python3
"""async_generator"""


import asyncio
import random
from typing import List


async def async_generator() -> List[float]:
    """async_generator"""

    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
