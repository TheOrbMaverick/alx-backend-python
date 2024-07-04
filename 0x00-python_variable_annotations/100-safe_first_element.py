#!/usr/bin/env python3
"""
This module provides a function to safely get the first element of a sequence.
"""

from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Safely returns the first element of a sequence or
    None if the sequence is empty.
    """
    if lst:
        return lst[0]
    else:
        return None
