from random import randint


class Die():
    """Class to store die attributes and methods"""
    def __init__(self, num_sides = 6):
        """Assume standard 6 sides"""
        self.num_sides = 6
    
    def roll(self):
        """Return random value between 1 and # sides"""
        return randint(1, self.num_sides)