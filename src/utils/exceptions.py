class CardNotFoundException(Exception):
    """Exception raised when a card is not found in the deck."""
    def __init__(self, card, message="Card not found"):
        self.card = card
        self.message = message
        super().__init__(f"{message}: {card}")