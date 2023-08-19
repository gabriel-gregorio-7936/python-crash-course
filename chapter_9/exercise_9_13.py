from random import randint

class Dice:
    """An attempt to model a dice"""
    
    def __init__(self):
        """Initialize our dice"""
    
    def roll_dice(self, sides=6):
        """An attempt to model a dice roll"""
        side = randint(1, sides)
        print(f"{side}")


my_dice = Dice()
my_dice.roll_dice(20)