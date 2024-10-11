#!/usr/bin/env python3
"""Type_annotated function"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """str_kv"""
    squared = v ** 2
    return (k, int(squared) if isinstance(v, int) else squared)
