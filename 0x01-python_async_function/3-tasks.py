#!/usr/bin/env python3
'''A module for a function that returns a task'''
import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    '''Returns a task from a coroutine'''
    task = asyncio.create_task(wait_random(max_delay))
    return task
