"""This makes get_coords function"""

__author__ = "730827794"


def get_coords(xs: str, ys: str) -> None:
    i: int = 0
    while i < len(xs):
        j: int = 0
        while j < len(ys):
            print((xs[i], ys[j]))
            j += 1
        i += 1


print(get_coords("hi", "bye"))
