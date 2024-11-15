"""  """

__author__ = "730827794"


def find_and_remove_max(list1: list[int]) -> int:
    i: int = 0
    j: int = 0
    if len(list1) == 0:
        return -1
    else:
        max: int = list1[0]
        while i < len(list1):
            if max <= list1[i]:
                max = list1[i]
            i += 1

        while j < len(list1):
            if max == list1[j]:
                list1.pop(j)
            else:
                j += 1
        return max
