from enum import Enum, auto

class Suit(Enum):
    HEARTS = auto()
    DIAMONDS = auto()
    CLUBS = auto()
    SPADES = auto()

    def __str__(self):
        return self.name.capitalize()

class Rank(Enum):
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13
    ACE = 14

    def __str__(self):
        if self.value <= 10:
            return str(self.value)
        else:
            return self.name.capitalize()

class Card:
    def __init__(self, rank, suit):
        if isinstance(rank, Rank) and isinstance(suit, Suit):
            self.rank = rank
            self.suit = suit
        else:
            raise TypeError("Invalid type for rank or suit")

    def __repr__(self):
        return f"{self.rank} of {self.suit}"

    def compare(self, other):
        # Compare two cards based on their rank
        if self.rank.value > other.rank.value:
            return 1
        elif self.rank.value < other.rank.value:
            return -1
        else:
            return 0
    
