"""This is cq00"""

__author__ = "730827794"


def mimic(message: str) -> str:
    """This function will just take input and repeat it back"""
    return message


def main() -> None:
    """This is only going to print the result of calling mimic"""
    print(mimic(message=input("What is your message?")))


if __name__ == "__main__":
    main()
