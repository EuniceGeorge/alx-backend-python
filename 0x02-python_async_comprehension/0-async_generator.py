#!/usr/bin/env python3
"""async_generator"""


import asyncio
import random


async def async_generator():
    """async_generator"""

    for _ in range(10):
        await asyncio.sleep(1)
        yield random.randint(0, 10)