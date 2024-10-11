#!/usr/bin/env python3
"""Multiplier"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """callable function"""
    def mul(x: float) -> float:
        return x * multiplier
    return mul    
