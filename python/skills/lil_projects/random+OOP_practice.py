import random

class Dice:
    def roll(self):
        first = random.randint(0,9)
        second = random.randint(0,9)
        return(first,second)            # Returning 2+ values in a function automatically makes the return output a tuple
    
dice = Dice()
print(dice.roll())
    

