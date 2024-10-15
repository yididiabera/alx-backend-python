#!/usr/bin/env python3
'''A module for measuring runtime of an asynchronous operation'''
import asyncio
import time


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    '''Measures the runtime of asynchronous operations'''
    coroutines = [async_comprehension() for _ in range(4)]
    start = time.perf_counter()
    await asyncio.gather(*coroutines)
    end = time.perf_counter()
    return end - start
