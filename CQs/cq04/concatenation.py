"""This makes concat function"""

__author__ = "730827794"


def concat(w1: str, w2: str) -> str:
    word: str = w1 + w2
    return word


if __name__ == "__main__":
    word1: str = "happy"
    word2: str = "tuesday"
    print(concat(word1, word2))
