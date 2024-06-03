from .card import Card, Suit,Rank
from collections import Counter
from enum import Enum, auto

class HandRank(Enum):
    HIGHCARD = 0
    PAIR = 1
    TWOPAIR = 2
    SET = 3
    STRAIGHT = 4
    FLUSH = 5
    QUADS = 6
    FULLHOUSE = 7
    STRAIGHTFLUSH = 8
    def __lt__(self, other):
        if not isinstance(other, HandRank):
            return NotImplemented
        return self.value < other.value

    def __le__(self, other):
        if not isinstance(other, HandRank):
            return NotImplemented
        return self.value <= other.value

    def __gt__(self, other):
        if not isinstance(other, HandRank):
            return NotImplemented
        return self.value > other.value

    def __ge__(self, other):
        if not isinstance(other, HandRank):
            return NotImplemented
        return self.value >= other.value

    def __eq__(self, other):
        if not isinstance(other, HandRank):
            return NotImplemented
        return self.value == other.value
    

    def __str__(self):
        return self.name.capitalize()
    
class HandEval:
    def __init__(self):
        pass
    
    @staticmethod
    def setHandScore(hand):
        board = hand.board

        if HandEval.isStraightFlush(hand.cards, board) != None:
            (hScore, cardsInPlay, kickers) = HandEval.isStraightFlush(hand.cards, board)
            handRank = HandRank.STRAIGHTFLUSH
        elif HandEval.isQuads(hand.cards, board) != None:
            hScore, cardsInPlay, kickers = HandEval.isQuads(hand.cards, board)
            handRank = HandRank.QUADS
        elif HandEval.isFullHouse(hand.cards, board) != None:
            hScore, cardsInPlay, kickers = HandEval.isFullHouse(hand.cards, board)
            handRank = HandRank.FULLHOUSE
        elif HandEval.isFlush(hand.cards, board) != None:
            hScore, cardsInPlay, kickers = HandEval.isFlush(hand.cards, board)
            handRank = HandRank.FLUSH
            
        elif HandEval.isStraight(hand.cards, board) != None:
            hScore, cardsInPlay, kickers = HandEval.isStraight(hand.cards, board)
            handRank = HandRank.STRAIGHT
        elif HandEval.isTrips(hand.cards, board) != None:
            hScore, cardsInPlay, kickers = HandEval.isTrips(hand.cards, board)
            handRank = HandRank.SET
        elif HandEval.isTwoPair(hand.cards, board) != None:
            hScore, cardsInPlay, kickers = HandEval.isTwoPair(hand.cards, board)
            handRank = HandRank.TWOPAIR
        elif HandEval.isPair(hand.cards, board) != None:
            hScore, cardsInPlay, kickers = HandEval.isPair(hand.cards, board)
            handRank = HandRank.PAIR
        else:
            hScore, cardsInPlay, kickers = HandEval.isHighCard(hand.cards, board)
            handRank = HandRank.HIGHCARD
        hand.score = handRank
        hand.scoreRank = hScore
        hand.cardsInPlay = cardsInPlay
        hand.kickers = kickers






        
    @staticmethod
    def isStraightFlush(hand, board):
        suits = {Suit.HEARTS: [], Suit.DIAMONDS: [], Suit.SPADES: [], Suit.CLUBS: []}
        total = hand + board
        for i in total:
            if i.rank not in suits[i.suit]:
                suits[i.suit].append(i)
        
        for suit, cards in suits.items():
            if len(cards) >= 5:
                sortedCards = sorted(hand+board, key=lambda x: x.rank, reverse=True)
                ranks = [card.rank for card in sortedCards]
                
                for i in range(len(ranks) - 4):  
                    if ranks[i + 4] == ranks[i].value - 4: 
                        return (ranks[i],sortedCards[i:i+5], [])
            
                

        return None
    
    @staticmethod
    def isQuads(hand, board):
        quadCounter = {}
        total = hand + board
        for i in total:
            if i.rank.value not in quadCounter.keys():
                quadCounter[i.rank.value] = [i]
            else:
                quadCounter[i.rank.value].append(i)
        
        
        for i in quadCounter.keys():
            if len(quadCounter[i]) == 4:
                new_list = sorted(hand+board, key=lambda x: x.rank, reverse=True)
                for j in new_list:
                    if j.rank != i:
                        return(i, quadCounter[i] + [j] , [j])
        return None
    @staticmethod
    def isFullHouse(hand, board):
        fhCounter = {}
        ranks = [card.rank for card in hand + board]
        for i in hand+board:
            if i.rank.value not in fhCounter.keys():
                fhCounter[i.rank.value] = [i]
            else:
                fhCounter[i.rank.value].append(i)
        trips = []
        pairs = []
        for item, values in fhCounter.items():
            if len(values) >= 3:
                trips.append(item)
            if len(values) >= 2:
                pairs.append(item)

        trips = sorted(trips, reverse=True)
        pairs = sorted(pairs, reverse=True)
        for i in trips:
            for j in pairs:
                if i != j:
                    return (15 * i + j, fhCounter[i] + fhCounter[j], [])
        return None



    
    @staticmethod
    def isStraight(hand,board):

        rankValues = []
        ranks = []
        for i in hand + board:
            if i.rank.value not in rankValues:
                ranks.append(i)
                rankValues.append(i.rank)
        ranks = sorted(ranks,key=lambda x: x.rank, reverse=True)
        for i in range(len(ranks) -4):
            if ranks[i+4].rank == ranks[i].rank.value - 4:
                print("return 1")
                return (ranks[i].rank.value, ranks[i:i+5], [])
            
        if ranks[len(ranks)-4].rank == ranks[len(ranks)-1].rank.value+3:
            if ranks[len(ranks)-1].rank == Rank.TWO and ranks[0].rank == Rank.ACE:
                print("reutn 2")
                return (ranks[len(ranks)-4].rank.value,ranks[0:4] + [ranks[len(ranks)-1]], [])

        return None

    @staticmethod
    def isFlush(hand,board):
        suits = {Suit.HEARTS.value: [], Suit.DIAMONDS.value: [], Suit.SPADES.value: [], Suit.CLUBS.value: []}
        for i in hand + board:
            suits[i.suit.value].append(i)
        for keys, values in suits.items():
            if len(values) >= 5:
                ranks = sorted(values,key=lambda x: x.rank, reverse=True)
                return (ranks[0].rank.value, ranks[0:5], [])
            
        return None
    
    @staticmethod
    def isTrips(hand, board):

        tripsCounter = {}
        total = hand + board
        for i in total:
            if i.rank.value not in tripsCounter.keys():
                tripsCounter[i.rank.value] = [i]
            else:
                tripsCounter[i.rank.value].append(i)
        
        kickers = []
        for i in tripsCounter.keys():
            if len(tripsCounter[i]) == 3:
                new_list = sorted(hand+board, key=lambda x: x.rank, reverse=True)
                for j in new_list:
                    if j.rank != i:
                        kickers.append(j)
                        if len(kickers) == 2:
                            return(i, tripsCounter[i] + kickers, kickers)
        return None

    @staticmethod
    def isTwoPair(hand, board):
        #this method returns 2** of the value of the higher pair plus 2**
        #of the value of the lower pair
        # and the 5 cards that make up the two pairs and the kciker
        # and then the kicker
        pairs = []
        ranks = [card.rank.value for card in hand + board]
        counter = Counter(ranks)
        for i in counter.keys():
            if counter[i] == 2:
                pairs.append(i)
        if len(pairs) >= 2:
            pairs = sorted(pairs, reverse=True)
            kickers = []
            for i in hand + board:
                if i.rank != pairs[0] and i.rank != pairs[1]:
                    kickers.append(i)
                    if len(kickers) == 1:
                        return (15**pairs[0] + pairs[1], [card for card in hand + board if card.rank == pairs[0] or card.rank == pairs[1]] + kickers, kickers)
        
        return None
        
        
        
    @staticmethod
    def isPair(hand, board):
        pairs = []
        ranks = [card.rank.value for card in hand + board]
        counter = Counter(ranks)
        for i in counter.keys():
            if counter[i] == 2:
                pairs.append(i)
        if len(pairs) >= 1:
            pairs = sorted(pairs, reverse=True)
            kickers = []
            for i in hand + board:
                if i.rank != pairs[0]:
                    kickers.append(i)
                    if len(kickers) == 3:
                        return (pairs[0], [card for card in hand + board if card.rank == pairs[0]] + kickers, kickers)
        
        return None
        
    @staticmethod
    def isHighCard(hand, board):
        ranks = sorted([card.rank for card in hand + board], reverse=True)
        return (ranks[0].value, [ranks[0]], ranks[1:])
        


    @staticmethod
    def handCompare(hands, board):
        evaluated_hands = [HandEval.handScore(hand, board) for hand in hands]
        # Determine the highest rank
        highest_rank = max(hand[0].value for hand in evaluated_hands)
        
        # Filter hands that have the highest rank
        highest_rank_hands = [hand for hand in evaluated_hands if hand[0].value == highest_rank]
        
        # If only one hand, it's the winner
        if len(highest_rank_hands) == 1:
            return [highest_rank_hands[0]]

        highest_score = max(hand[1] for hand in highest_rank_hands)
        highest_score_hands = [hand for hand in highest_score_hands if hand[1] == highest_score]
        if len(highest_score_hands) == 1:
            return [highest_score_hands[0]]
        
        
        
        # Compare kickers if more than one hand has the highest rank
        best_hands = HandEval.compareKickers(highest_rank_hands)
        return best_hands
    
    @staticmethod
    # List of cards is the input
    # return index of highest card
    def compareKickers(highest_rank_hands):
        # Sort hands by highest card
        for i in range(len(highest_rank_hands[0].kickers)):
            maxKicker = max([hand.kickers[i] for hand in highest_rank_hands])
            highest_rank_hands = sorted(highest_rank_hands, key=lambda x: x.kickers[i], reverse=True)
            for j in range(len(highest_rank_hands)):
                if highest_rank_hands[j].kickers[i] != maxKicker:
                    highest_rank_hands = highest_rank_hands[0:j]
                    break
            if len(highest_rank_hands) == 1:
                return highest_rank_hands
                
        
        return highest_rank_hands
            
    
        

        



