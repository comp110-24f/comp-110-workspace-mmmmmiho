"""Exporing the linked list in a class"""

from __future__ import Node #I don't know what is next to import

class Node:
    value: int
    next: Node | None

    def __init__(self, val: int, next: Node | None):
        self.value = val
        self.next = next

    def __str__(self)->str:
        rest: str
        if self.next is None: #Base case
            rest = "None"
        else:
            rest = str(self.next)
        return f"{self.value} -> {rest}"

two: Node = Node(2, None)
one: Node = Node(1, two)

print(one)

def last(head: Node)-> int:
    """"Return the last value in the a non-emp"""
    if head.next is None: #Base case
        return head.value
    else:
        return last(head.next)
    
