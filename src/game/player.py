from src.utils.hand import Hand

class Player:
    def __init__(self, name, is_human=True, chip_count=1000):
        self.name = name
        self.is_human = is_human
        self.chip_count = chip_count
        self.hand = Hand()  
        self.current_bet = 0
        self.folded = False

    def receive_cards(self, cards):
        """Add cards to the player's hand."""
        for card in cards:
            self.hand.add_card(card)

    def action(self, game_state):
        """Determine the player's action based on the game state and player type."""
        if not self.is_human:
            return self._computer_action(game_state)
        return self._human_action(game_state)

    def _human_action(self, game_state):
        """Prompt human player for their action."""
        print(f"{self.name}, it's your turn. Your hand: {self.hand}")
        print(f"Current bet: {game_state['current_bet']}, Your chips: {self.chip_count}")
        action = input("Choose your action (fold, call, raise): ").strip().lower()
        if action == "fold":
            self.folded = True
        elif action == "raise":
            raise_amount = int(input("Enter raise amount: "))
            self.chip_count -= raise_amount
            self.current_bet += raise_amount
            return 'raise', raise_amount
        elif action == "call":
            self.chip_count -= game_state['current_bet']
            self.current_bet = game_state['current_bet']
        return action

    def _computer_action(self, game_state):
        """Determine computer's action based on a simplistic strategy."""
        # This is a very simple strategy for demonstration purposes
        if game_state['current_bet'] > 0:
            if self.chip_count > game_state['current_bet']:
                self.chip_count -= game_state['current_bet']
                self.current_bet = game_state['current_bet']
                return 'call'
            else:
                self.folded = True
                return 'fold'
        return 'check'

    def reset_for_new_round(self):
        """Reset player's state for a new round."""
        self.hand = Hand()  # Re-initialize the hand for a new round
        self.current_bet = 0
        self.folded = False

    def __str__(self):
        return f"Player {self.name} - Chips: {self.chip_count} - Hand: {self.hand}"
