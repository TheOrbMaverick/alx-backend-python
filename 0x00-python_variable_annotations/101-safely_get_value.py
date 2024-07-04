#!/usr/bin/env python3
"""
This module provides a function to safely get a value from a
dictionary with a default.
"""

from typing import Mapping, Any, TypeVar, Union

# Define a TypeVar for the default value
T = TypeVar('T')


def safely_get_value(
    dct: Mapping[Any, Any],
    key: Any,
    default: Union[T, None] = None
) -> Union[Any, T]:
    """
    Safely returns the value for a given key from a
    dictionary or a default value if the key is not present.
    """

    if key in dct:
        return dct[key]
    else:
        return default
