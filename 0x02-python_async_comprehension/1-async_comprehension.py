#!/usr/bin/env python3
"""Print random numbers"""


import asyncio
from typing import AsyncGenerator
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> AsyncGenerator[float, None]:
    """async_comprehension"""
    return [number async for number in async_generator()]
