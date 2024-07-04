#!/usr/bin/env python3
"""
This module provides a function to create a multiplier function.
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a function that multiplies a float by the given multiplier.
    """

    def multiplier_function(value: float) -> float:
        return value * multiplier

    return multiplier_function
