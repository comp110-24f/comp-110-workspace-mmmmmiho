"""This is cq02"""

__author__ = "730827794"


def guess_a_number() -> None:
    secret: int = 7
    x = int(input("Guess a number."))
    print("Your guess was " + str(x) + ".")
    if x == secret:
        print("You got it!")
    elif x < secret:
        print("Your guess was too low! The secret number is " + str(secret) + ".")
    else:
        print("Your guess was too high! The secret number is " + str(secret) + ".")

    return None


if __name__ == "__main__":
    guess_a_number()