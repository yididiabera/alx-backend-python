#!/usr/bin/env python3
'''A module for getting a function that multiplies a float by a multiplier'''
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''Returns a multiplier function'''
    def multiply(n: float) -> float:
        '''Multiply function'''
        return n * multiplier
    return multiply
