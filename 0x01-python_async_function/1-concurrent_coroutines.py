#!/usr/bin/env python3
'''A module for calling multiple delays and returning them in a sorted list'''
import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    '''Returns the sorted waiting times of all calls'''
    coroutines = [wait_random(max_delay) for _ in range(n)]
    completed, _ = await asyncio.wait(coroutines)
    delays = [task.result() for task in completed]
    ordered = []
    while delays:
        minimum = min(delays)
        ordered.append(minimum)
        delays.remove(minimum)
    return ordered
