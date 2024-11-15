"""Summing the elements of a list using different loops"""

__author__ = "730827794"


def w_sum(vals: list[float]) -> float:
    i: int = 0
    sum: float = 0.0
    if len(vals) == 0:
        return 0.0
    else:
        while i < len(vals):
            sum += vals[i]
            i += 1
        return sum


def f_sum(vals: list[float]) -> float:
    sum: float = 0.0
    for i in vals:
        sum += i
    return sum


def f_range_sum(vals: list[float]) -> float:
    sum: float = 0.0
    for i in range(0, len(vals)):
        sum += vals[i]
    return sum
