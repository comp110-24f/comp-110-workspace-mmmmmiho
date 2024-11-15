"""This is EX05"""

__author__ = "730827794"


def only_evens(original_list: list[int]) -> list[int]:
    even_list: list[int] = []
    for i in range(0, len(original_list)):
        if original_list[i] % 2 == 0:
            even_list.append(original_list[i])

    return even_list


def sub(original_list: list[int], a: int, b: int) -> list[int]:
    new_list: list[int] = []
    if (len(original_list) == 0) or (a >= len(original_list)) or (b == 0):
        return new_list

    if a < 0:
        a = 0
    if b > len(original_list):
        b = len(original_list)

    i: int = a

    while a <= i and i < b:
        new_list.append(original_list[i])
        i += 1

    return new_list


def add_at_index(original_list: list[int], element: int, index: int) -> None:
    if index < 0 or index > len(original_list):
        raise IndexError("Index is out of bounds for the input list")

    original_list.append(0)
    for i in range(len(original_list) - 1, index, -1):
        original_list[i] = original_list[i - 1]
    original_list[index] = element
