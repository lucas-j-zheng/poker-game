
class PokerGame:
    def __init__(self, players):
        self.players = players
        self.current_players = players
        self.dealer_position = 0

    def get_next_player(self, current_position):
        return (current_position + 1) % len(self.current_players)
    
    def play_round(self):
        current_position = self.get_next_player(self.dealer_position)
