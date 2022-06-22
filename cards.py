import random


class cards:
    """A small deck of cards with a different face .

    The responsibility of deck is to keep track of the side facing up and calculate the points for 
    it.
   
    Attributes:
        value (int): The number of spots on the side facing up.
    """

    def __init__(self, value, points, current_card):
        """Constructs a new instance Cards.

        Args:
            self (card): An instance of Die.
        """
        self.value = 0
        self.points = 0
        self.current_card = 1  

    def shuffle(self):
        """Generates a new random value and calculates the points for the current card.
        
        Args:
            self (card): An instance of card.
        """
        self.value = random.randint(1, 13)
        self.points = 300 if self.current_card == 1  else 100 if self.value == 1 else 0