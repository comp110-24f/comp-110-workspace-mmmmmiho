"""This is cq03 to practice while loop"""

__author__ = "730827794"


def num_instances(phrase: str, search_char: str) -> int:
    count: int = 0
    i: int = 0
    while i < len(phrase):
        if phrase[i] == search_char:
            count += 1
        i += 1
    return count


print(num_instances(phrase="HelloHeLloHEllo", search_char="e"))
