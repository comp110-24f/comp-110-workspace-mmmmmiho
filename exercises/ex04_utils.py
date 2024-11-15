"""This is exericise for list"""

__author__ = "730827794"


def all(list_1: list[int], i: int) -> bool:
    j: int = 0
    boolean: bool = True
    if len(list_1) == 0:
        return False
    while j < len(list_1):
        if list_1[j] == i:
            j += 1
        else:
            return False
    return boolean
    print(boolean)


def max(list_2: list[int]) -> int:
    current_max: int = 0
    i: int = 0
    if len(list_2) == 0:
        raise ValueError("max() arg is an empty List")
    else:
        current_max = list_2[0]
        while i < len(list_2):
            if list_2[i] > current_max:
                current_max = list_2[i]
            i += 1
        return current_max
        print(current_max)


def is_equal(list_3: list[int], list_4: list[int]) -> bool:
    i: int = 0
    boolean: bool = True
    if len(list_3) != len(list_4):
        boolean = False
    else:
        while i < len(list_3):
            if list_3[i] == list_4[i]:
                i += 1
            else:
                return False
    print(boolean)
    return boolean


def extend(list_5: list[int], list_6: list[int]) -> None:
    i: int = 0
    while i < len(list_6):
        list_5.append(list_6[i])
        i += 1
    print(list_5)
