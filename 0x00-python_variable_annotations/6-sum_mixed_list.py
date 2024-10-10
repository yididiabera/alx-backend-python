#!/usr/bin/env python3
'''A module for summing up a mixed list'''
from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    '''Returns the float sum of a list of mixed elements'''
    return float(sum(mxd_lst))
