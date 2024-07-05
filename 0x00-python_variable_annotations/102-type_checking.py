#!/usr/bin/env python3
"""
This module provides a function to zoom into a tuple by repeating its elements.
"""

from typing import Tuple, Any


def zoom_array(lst: Tuple[Any, ...], factor: int = 2) -> Tuple[Any, ...]:
    """
    Zooms into a tuple by repeating its elements.
    """

    if not isinstance(factor, int):
        raise ValueError(f"factor should be an integer, got {type(factor).__name__}")

    zoomed_in: Tuple[Any, ...] = tuple(
        item for item in lst
        for i in range(factor)
    )
    return zoomed_in
