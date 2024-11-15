"""File to define Fish class."""
__author__ = "730827794"


class Fish:
    """This is Class Fish."""

    age: int
    
    def __init__(self): 
        """This is the initialization."""
        self.age = 0
        return None
    
    def one_day(self) -> None: 
        """They grow by one day."""
        self.age += 1
        return None