from enum import Enum, auto
from .exceptions import CardNotFoundException

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
    def __lt__(self, other):
        if isinstance(other, Rank):
            return self.value < other.value
        elif isinstance(other, int):
            return self.value < other
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, Rank):
            return self.value <= other.value
        elif isinstance(other, int):
            return self.value <= other
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Rank):
            return self.value > other.value
        elif isinstance(other, int):
            return self.value > other
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, Rank):
            return self.value >= other.value
        elif isinstance(other, int):
            return self.value >= other
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, Rank):
            return self.value == other.value
        elif isinstance(other, int):
            return self.value == other
        return NotImplemented

class Card:
    card_ranks = {
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'T': 10,  # Typically, 'T' is used for Ten
    'J': 11,  # Jack
    'Q': 12,  # Queen
    'K': 13,  # King
    'A': 14   # Ace
    }
    card_suits = {
    'C': 1,  # Clubs
    'D': 2,  # Diamonds
    'H': 3,  # Hearts
    'S': 4   # Spades
    }
    
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
    
    @staticmethod
    def cardFromString(cardString):
        
        if len(cardString) != 2:
            raise CardNotFoundException()
        elif cardString[0] not in Card.card_ranks.keys() or cardString[1] not in Card.card_suits.keys():
            raise CardNotFoundException()
        else:
            return Card(Rank(Card.card_ranks[cardString[0]]), Suit(Card.card_suits[cardString[1]]))
        
    @staticmethod
    def cardsFromStrings(cardStringList):
        cardList = []
        for i in cardStringList:
            cardList.append(Card.cardFromString(i))
        return cardList

        
        