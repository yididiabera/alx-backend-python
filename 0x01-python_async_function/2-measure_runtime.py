#!/usr/bin/env python3
'''A module for measuring the execution time of another function'''
import time
import asyncio


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    '''Returns the runtime of a coroutine'''
    t = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    s = time.perf_counter()
    return s - t
