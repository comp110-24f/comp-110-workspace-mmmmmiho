"""This proguram help me plan a tea party. """

__author__: str = "730827794"


def main_planner(guests: int) -> None:
    """This bring all of the functions together and print output"""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(people=guests)))
    print("Treats: " + str(treats(people=guests)))
    print(
        "Cost: $"
        + str(
            cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests))
        )
    )
    # cost is sum of tea cost and treat cost


def tea_bags(people: int) -> int:
    """This counts the number of teabags needed"""
    return people * 2  # 2 tea bags needed for each person


def treats(people: int) -> int:
    """This compute the number of treats needed"""
    return int(tea_bags(people=people) * 1.5)  # 1.5 treats needed for each tea


def cost(tea_count: int, treat_count: int) -> float:
    """This compute the cost of the tea bags and the treats combined"""
    return tea_count * 0.50 + treat_count * 0.75  # cost is sum of tea cost & traet cost


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
