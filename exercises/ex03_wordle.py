"""This is an ex03 for Wordle"""

__author__ = "730827794"


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    state: str = ""  # strings of color boxes
    i: int = 1
    j: bool = True  # we can use bool when the game is over
    while i <= 6 and j:  # we conside the case of i=6
        print(f"=== Turn {i}/6 ===")
        guess_word: str = input_guess(secret_word_len=len(secret))
        state = emojified(guess_word, secret)
        print(state)
        if state == "\U0001F7E9" * len(secret):  # we need len(secret) boxes
            print(f"You won in {i}/6 turns!")
            j = False
        else:
            i += 1
    if j:  # when user lost
        print("X/6 - Sorry, try again tomorrow!")


def input_guess(secret_word_len: int) -> str:
    guess_word = str(
        input(f"Enter a {str(secret_word_len)} character word: ")
    )  # when we use print(f-),we can use {} for variables
    while len(guess_word) != secret_word_len:
        guess_word = str(
            input(f"That wan't {str(secret_word_len)} charas! Try again: ")
        )
    print(guess_word)
    return guess_word


def contains_char(secret_word: str, char_guess: str) -> bool:
    """This tests if each index of the first parameter string matches the second parameter."""
    assert len(char_guess) == 1
    i: int = 0
    while i < len(secret_word):
        if secret_word[i] == char_guess:
            return True
        i += 1
    return False


def emojified(guess: str, secret: str) -> str:
    """Its purpose is to compare two strings of equal length"""
    assert len(guess) == len(secret)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    i: int = 0  # index
    answer: str = ""
    while i < len(guess):
        if secret[i] == guess[i]:  # we chack if it shoul be a green box
            answer += GREEN_BOX
        else:  # if it is not a green box
            if contains_char(secret_word=secret, char_guess=guess[i]):
                answer += YELLOW_BOX
            else:
                answer += WHITE_BOX
        i += 1
    return answer


if __name__ == "__main__":
    main(secret="codes")
