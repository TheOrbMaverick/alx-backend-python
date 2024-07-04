#!/usr/bin/env python3
"""
This module provides a function to zoom into a list by repeating its elements.
"""

from typing import List, Tuple

def zoom_array(lst: Tuple[int, ...], factor: int = 2) -> List[int]:
    """
    Zooms into a tuple by repeating its elements.

    Args:
        lst (Tuple[int, ...]): A tuple of integers to zoom into.
        factor (int, optional): The number of times to repeat each element. Defaults to 2.
    """
    zoomed_in: List[int] = [item for item in lst for i in range(factor)]
    return zoomed_in