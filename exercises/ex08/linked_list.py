"""Exporing the linked list in a class."""

from __future__ import annotations

__author__ = "730827794"


class Node:
    """This is a Node class."""

    value: int
    next: Node | None

    def __init__(self, val: int, next: Node | None):
        """This is a constructor."""
        self.value = val
        self.next = next

    def __str__(self) -> str:
        """Represent a linked list as a str."""
        rest: str
        if self.next is None:  # Base case
            rest = "None"
        else:
            rest = str(self.next)
        return f"{self.value} -> {rest}"


two: Node = Node(2, None)
one: Node = Node(1, two)
print(one)


def last(head: Node) -> int:
    """Return the last value in the a non-emp."""
    if head.next is None:  # Base case
        return head.value
    else:
        return last(head.next)


def value_at(head: Node | None, index: int) -> int:
    """This returns the value at the index in the Linked List."""
    if head is None:
        raise IndexError("Index is out of bounds on the list.")

    else:
        current_Node: Node = head

        if index < 0:
            raise IndexError("Index is out of bounds on the list.")

        if index == 0:  # Base case
            return current_Node.value

        else:
            return value_at(current_Node.next, index - 1)


def max(head: Node | None) -> int:
    """This returns the maximum value in the linked list."""
    if head is None:
        raise ValueError("Cannot call max with None")

    else:
        if head.next is None:  # base case
            return head.value

        else:
            if head.value > max(head.next):
                return head.value

            else:
                return max(head.next)


def linkify(items: list[int]) -> Node | None:
    """This converts list to linked list."""
    if len(items) == 0:
        return None

    else:
        return Node(items[0], linkify(items[1:]))


def scale(head: Node | None, factor: int) -> Node | None:
    """This multiples the linked list by factor."""
    if head is None:
        return None

    else:
        return Node((head.value) * factor, scale(head.next, factor))
