"""EX02 - Chardle - A cute step toward Wordle."""

__author__ = "730827794"


def main() -> None:
    contains_char(word=input_word(), letter=input_letter())


def input_word() -> str:
    word = str(input("Enter a 5-character word: "))
    if len(word) != 5:
        print("Error: Word must contain 5 characters.")
        exit()
    else:  # if len(word)==5, nothing is shown
        return word


def input_letter() -> str:
    letter = str(input("Enter a single character: "))
    if len(letter) != 1:
        print("Error: Character must be a single character.")
        exit()
    else:
        return letter


def contains_char(word: str, letter: str) -> None:
    count: int = 0  # count is a variable which counts how many times the letter appear
    print("Searching for " + letter + " in " + word)
    if word[0] == letter:
        print(letter + " found at index 0")
        count = count + 1
    if word[1] == letter:
        print(letter + " found at index 1")
        count = count + 1
    if word[2] == letter:
        print(letter + " found at index 2")
        count = count + 1
    if word[3] == letter:
        print(letter + " found at index 3")
        count = count + 1
    if word[4] == letter:
        print(letter + " found at index 4")
        count = count + 1

    if count != 0:
        print(str(count) + " instances of " + letter + " found in " + word)
    else:
        print("No instances of " + letter + " found in " + word)


if __name__ == "__main__":
    main()
