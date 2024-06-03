from .card import Card
from .hand_eval import HandRank

class Hand:
    def __init__(self, player, cards = [], board = []):
        self.player = player
        self.cards = cards
        #score for what type of hand someone has
        self.score = None
        #score for specifically where that hand ranks with other hands
        # i.e. higher pair vs lower pair
        self.scoreRank = None
        self.board = board
        #the 5 cards that matter for the player's hand
        self.cardsInPlay = []
        self.kickers = []

    def dealHand(self, card):
        if isinstance(card, Card):
            self.cards.append(card)
        else:
            raise ValueError("Only Card instances can be added to a hand")

    def evaluate_hand(self):
        # Placeholder for hand evaluation logic
        # This should interact with a hand evaluation system or utility
        pass

    def dealBoard(boardCards):
        board = board + boardCards


    def __str__(self):
        return ', '.join(str(card) for card in self.cards)
