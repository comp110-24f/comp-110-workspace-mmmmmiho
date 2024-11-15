"""File to define Bear class."""
__author__ = "730827794"


class Bear:
    """This is class Bear."""
    age: int
    hunger_score: int
    
    def __init__(self): 
        """This is the initialization."""
        self.age = 0
        self.hunger_score = 0
    
    def one_day(self) -> None:  
        """They become older and thier hunger become increase by one."""
        self.age += 1
        self.hunger_score -= 1 
        return None 
    
    def eat(self, num_fish: int) -> None: 
        """Bears eat fish."""
        self.hunger_score += num_fish 
        return None 