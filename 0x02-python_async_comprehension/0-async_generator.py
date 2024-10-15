#!/usr/bin/env python3
'''A module for an async coroutine that yields 10 random numbers'''
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    '''Yields 10 random floats'''
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
