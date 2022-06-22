from game.director import Director


class director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        Deck(List[Deck]): A list of Deck instances.
        is_playing (boolean): Whether or not the game is being played.
        score (int): The score for one round of play.
        total_score (int): The score for the entire game.
    """

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        self.deck = []
        self.guess_card =" "
        self.is_playing = True
        self.score = 300
        self.total_score = 300

        for i in range(13):
            card = card()
            self.guess_card.append(card)

    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        while self.is_playing:
            self.get_inputs()
            self.guess_card()
            self.do_updates()
            self.do_outputs()

    def get_inputs(self):
        """Ask the user if they want to Shuffle the Deck of cards.

        Args:
            self (Director): An instance of Director.
        """
        shuffle_deck = input("Shuffle the deck of cards? [y/n] ")
        
        self.is_playing = (shuffle_deck == "y")
        

    def guess_card(self):
        """Asks the user to guess_card
        
        Args
        self(Director): An instance of Director.
        """
        guess_card = input("Guess the card: [y/n]")
        self.is_playing = (guess_card == "y")

    def do_updates(self):
        """Updates the player's score.

        Args:
            self (Director): An instance of Director.
        """
        if not self.is_playing:
            return 

        for i in range(len(self.deck)):
            card = self.deck[i]
            card.shuffle()
            self.score += card.points 
        self.total_score += self.score

    def do_outputs(self):
        """Displays the card and the score. Also asks the player if they want to shuffle_deck again. 

        Args:
            self (Director): An instance of Director.
        """
        if not self.is_playing:
            return
        
        values = ""
        for i in range(len(self.dice)):
            card = self.card[i]
            values += f"{card.value} "

        print(f"You shuffled: {values}")
        print(f"Your score is: {self.total_score}\n")
        self.is_playing == (self.score > 0)