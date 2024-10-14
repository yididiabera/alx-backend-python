#!/usr/bin/env python3
'''Refactor code to use tasks'''
import asyncio
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    '''Returns the sorted waiting times of all calls'''
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    completed, _ = await asyncio.wait(tasks)
    delays = [task.result() for task in completed]
    ordered = []
    while delays:
        minimum = min(delays)
        ordered.append(minimum)
        delays.remove(minimum)
    return ordered
