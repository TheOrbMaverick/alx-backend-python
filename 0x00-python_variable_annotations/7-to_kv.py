#!/usr/bin/env python3
"""
This module provides a function to create a tuple with a
string and the square of a number.
"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Returns a tuple where the first element is the string k
    and the second element is the square of v.
    """
    return (k, float(v ** 2))
