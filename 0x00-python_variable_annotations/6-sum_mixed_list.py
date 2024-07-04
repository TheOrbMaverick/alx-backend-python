#!/usr/bin/env python3
"""
This module provides a function to sum a list of integers
and floating-point numbers.
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Sums a list of integers and floating-point numbers.
    """
    return sum(mxd_lst)
