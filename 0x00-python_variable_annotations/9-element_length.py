#!/usr/bin/env python3
"""
This module provides a function to return a list of tuples with string lengths.
"""

from typing import List, Tuple


def element_length(lst: List[str]) -> List[Tuple[str, int]]:
    """
    Returns a list of tuples where each tuple contains a string and its length.
    """

    return [(i, len(i)) for i in lst]
