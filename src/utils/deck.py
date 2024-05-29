from random import shuffle
from .card import Card, Suit, Rank

class Deck:
    def __init__(self):
        self.cards = [Card(rank, suit) for suit in Suit for rank in Rank]
        shuffle(self.cards)

    def draw(self, count=1):
        if len(self.cards) < count:
            raise ValueError("Not enough cards in the deck to draw the requested number.")
        return [self.cards.pop() for _ in range(count)]

    def __repr__(self):
        return f"Deck({len(self.cards)} cards remaining)"
