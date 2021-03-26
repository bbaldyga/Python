from random import randint
class Die():
    """a class representing a single die"""

    def __init__(self, num_sides=6):
        """Assume a six-sided dice"""
        self.num_sides = num_sides
    
    def roll(self):
        """Return a random valuen between 1 and num of sides"""
        return randint(1,self.num_sides)