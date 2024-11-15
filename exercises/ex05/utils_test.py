"""This is the test of utils.py"""

__author__ = "730827794"

from exercises.ex05.utils import only_evens, sub, add_at_index
import pytest


def test_only_evens1() -> None:
    """This is test for edge case"""
    assert only_evens([]) == []


def test_only_evens2() -> None:
    """This is test for the return value"""
    assert only_evens([1, 2, 3, 4, 5]) == [2, 4]


def test_only_evens3() -> None:
    """This checks if it changes inputs"""
    original_list = [1, 2, 3, 4, 5]
    result = only_evens(original_list)
    assert result == [2, 4]
    assert original_list == [1, 2, 3, 4, 5]


def test_sub1() -> None:
    """This is test for edge case"""
    assert sub([], 0, 1) == []


def test_sub2() -> None:
    """This is test for the return value"""
    assert sub([1, 2, 3, 4, 5], 1, 4) == [2, 3, 4]


def test_sub3() -> None:
    """This checks if it changes inputs"""
    original_list = [1, 2, 3, 4, 5]
    result = sub(original_list, a=2, b=3)
    assert result == []
    assert original_list == [1, 2, 3, 4, 5]


def test_add_at_index1() -> None:
    """This is test for edge case"""
    with pytest.raises(IndexError):
        add_at_index([1, 2, 3], 5, 5)


def test_add_at_index2() -> None:
    """This is test for the return value"""
    original_list = [1, 3, 4]
    add_at_index(original_list, 2, 1)
    assert original_list == [1, 2, 3, 4]


def test_add_at_index3() -> None:
    """This checks if it changes inputs"""
    original_list = [1, 2, 3]
    add_at_index(original_list, element=4, index=3)
    assert original_list == [1, 2, 3, 4]
