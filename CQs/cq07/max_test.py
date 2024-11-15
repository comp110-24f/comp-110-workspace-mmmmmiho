"""This is the test of find_max.py"""

__author__ = "730827794"

from CQs.cq07.find_max import find_and_remove_max


def test_find_max1() -> None:
    """This tests if it returns expected value"""
    assert find_and_remove_max([1, 2, 3, 4, 5, 4, 3, 2, 1]) == 5


def test_find_max2() -> None:
    """This tests if it mutates the input in the expected way"""
    a: list[int] = [1, 2, 3, 4, 1, 2, 3, 4]
    find_and_remove_max(a)
    assert a == [1, 2, 3, 1, 2, 3]


def test_find_max3() -> None:
    """This test for edge case"""
    assert find_and_remove_max([]) == -1
