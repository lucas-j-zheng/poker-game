from .card import Card
from hand_eval import HandRank

class Hand:
    def __init__(self, player):
        self.cards = []
        self.score = None
        self.board = []
        #the 5 cards that matter for the player's hand
        self.cardsInPlay = []
        self.kickers = []

    def add_card(self, card):
        if isinstance(card, Card):
            self.cards.append(card)
        else:
            raise ValueError("Only Card instances can be added to a hand")

    def evaluate_hand(self):
        # Placeholder for hand evaluation logic
        # This should interact with a hand evaluation system or utility
        pass

    def dealCards(boardCards):
        board = board + boardCards


    def __str__(self):
        return ', '.join(str(card) for card in self.cards)
