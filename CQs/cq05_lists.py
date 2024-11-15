"""Mutating functions."""

__author__ = "730827794"


def manual_append(a: list[int], b: int) -> None:
    a.append(b)


def double(c: list[int]) -> None:
    i: int = 0
    while i < len(c):
        c[i] = 2 * c[i]
        i += 1


list_1: list[int] = [1, 2, 3]
list_2: list[int] = list_1

double(list_2)
print(list_1)
print(list_2)
