#!/usr/bin/env python3
'''A module for returning the square of a float associated with a string'''
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    '''Returns the string provided along with the square of the float'''
    return (k, v**2)
