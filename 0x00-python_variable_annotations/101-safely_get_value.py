#!/usr/bin/env python3
'''Use typevar to annotate python code'''
from typing import Mapping, Any, Union, TypeVar


T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any, default:
                     Union[T, None]) -> Union[Any, T]:
    '''Return a value or None'''
    if key in dct:
        return dct[key]
    else:
        return default
