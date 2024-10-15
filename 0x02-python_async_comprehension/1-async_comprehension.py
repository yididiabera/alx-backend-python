#!/usr/bin/env python3
'''A module for creating a comprehension for generated async values'''
from typing import List


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    '''Returns 10 random numbers generated asynchronously'''
    return [i async for i in async_generator()]
