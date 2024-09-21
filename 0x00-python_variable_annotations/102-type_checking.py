#!/usr/bin/env python3
"""
This module provides a function to zoom into a tuple by repeating its elements.
"""

from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
    Zooms into a tuple by repeating its elements.
    """

    if not isinstance(factor, int):
        raise ValueError(
            f"factor should be an integer, got {type(factor).__name__}"
            )

    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in
