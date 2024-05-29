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
    STRAIGHTFLUSH = 7
    

    def __str__(self):
        return self.name.capitalize()
    
class HandEval:
    def __init__(self):
        pass
    
    @staticmethod
    def handScore(hand, board):
        
        if HandEval.isStraightFlush(hand, board) != None:
            hScore, kickers, output = HandEval.isStraightFlush(hand, board)
            return [HandRank.STRAIGHTFLUSH, hScore, kickers,output]
        elif HandEval.isQuads(hand, board) != None:
            hScore, kickers,output = HandEval.isQuads(hand, board)
            return [HandRank.QUADS, hScore, kickers,output]
        elif HandEval.isFlush(hand, board) != None:
            hScore, kickers,output = HandEval.isFlush(hand, board)
            return [HandRank.FLUSH, hScore, kickers,output]
        elif HandEval.isStraight(hand, board) != None:
            hScore, kickers,output = HandEval.isStraight(hand, board)
            return [HandRank.STRAIGHT, hScore, kickers,output]
        elif HandEval.isTrips(hand, board) != None:
            hScore, kickers,output = HandEval.isTrips(hand, board)
            return [HandRank.SET, hScore, kickers,output]
        elif HandEval.isTwoPair(hand, board) != None:
            hScore, kickers,output = HandEval.isTwoPair(hand, board)
            return [HandRank.TWOPAIR, hScore, kickers,output]
        elif HandEval.isPair(hand, board) != None:
            hScore, kickers,output = HandEval.isPair(hand, board)
            return [HandRank.PAIR, hScore, kickers,output]
        else:
            hScore, kickers,output = HandEval.isHighCard(hand, board)
            return [HandRank.HIGHCARD, hScore, kickers,output]





        
    @staticmethod
    def isStraightFlush(hand, board):
        suits = {Suit.HEARTS: [], Suit.DIAMONDS: [], Suit.SPADES: [], Suit.CLUBS: []}
        for i in hand + board:
            if i.rank not in suits[i.suit]:
                suits[i.suit].append(i.rank)
        
        for suit, ranks in suits.items():
            if len(ranks) < 5:
                return False
            ranks = sorted(ranks, reverse = True)
            for i in range(len(ranks) - 4):  
                if ranks[i + 4] == ranks[i] - 4: 
                    return (ranks[i], [], str(ranks[i]) + " Straight Flush")
                

        return None
    
    @staticmethod
    def isQuads(hand, board):
        ranks = [card.rank for card in hand + board]
        counter = Counter(ranks)
        sortedRanks = sorted(ranks, reverse=True)
        for i in counter.keys():
            if counter[i] == 4:
                for j in sortedRanks:
                    if j != i:
                        return(i, [j], "4 " + str(i) + "'s")
        return None
    @staticmethod
    def isFullHouse(hand, board):

        ranks = [card.rank for card in hand + board]
        counter = Counter(ranks)
        trips = []
        pairs = []
        for item, count in counter.items():
            if count >= 3:
                trips.append(item)
            if count >= 2:
                pairs.append(item)

        trips = sorted(trips, reverse=True)
        pairs = sorted(pairs, reverse=True)
        for i in trips:
            for j in pairs:
                if i != j:
                    return (15 * i + j, [], str(i) + "'s full of " + str(j) + "'s")
        return None



    
    @staticmethod
    def isStraight(hand,board):
        ranks = []
        for i in hand + board:
            if i.rank not in ranks:
                ranks.append(i.rank)
        ranks = sorted(ranks, reverse = True)
        for i in range(len(ranks) -4):
            if ranks[i+4] == ranks[i] - 4:
                return (ranks[i], [], str(ranks[i]) + " high straight")
        return None

    @staticmethod
    def isFlush(hand,board):
        suits = {Suit.HEARTS: [], Suit.DIAMONDS: [], Suit.SPADES: [], Suit.CLUBS: []}
        for i in hand + board:
            suits[i.suit].append(i.rank)
        for i in suits.values():
            if len(i) >= 5:
                sorts = sorted(i, reverse = True)
                return (sorts[len(i)-5:len(i)], [], str(sorts[len(i)-5:len(i)]) + " high flush")
            
        return None
    
    @staticmethod
    def isTrips(hand, board):
        ranks = [card.rank for card in hand + board]
        counter = Counter(ranks)
        sortedRanks = sorted(ranks, reverse=True)
        trips = []
        for i in counter.keys():
            if counter[i] == 3:
                trips.append(i)
        if len(trips) > 0:
            trips = sorted(trips, reverse=True)
            kickers = []
            for j in sortedRanks:
                if j != trips[0]:
                    kickers.append(j)
                    if(len(kickers) == 2):
                        return(trips[0], [kickers[0], kickers[1]], "3 of a kind")
        else:
            return None

    @staticmethod
    def isTwoPair(hand, board):
        ranks = [card.rank for card in hand + board]
        counter = Counter(ranks)
        sortedRanks = sorted(ranks, reverse=True)
        pairs = []
        for i in counter.keys():
            if counter[i] == 2:
                pairs.append(i)
        if len(pairs) > 1:
            pairs = sorted(pairs, reverse=True)
            for rank in ranks:
                if rank != pairs[0] and rank != pairs[1]:
                    return (2**pairs[1] + 2** pairs[0],[rank], "two pair " + str(pairs[0]) +" and " + str(pairs[1]) )
        else:
            return None
    @staticmethod

    def isPair(hand, board):
        ranks = [card.rank for card in hand + board]
        counter = Counter(ranks)
        pairs = []
        kickers = []
        for i in counter.keys():
            if counter[i] == 2:
                pairs.append(i)
        if len(pairs) > 0:
            pairs = sorted(pairs, reverse=True)
            sortedRanks = sorted(ranks, reverse=True)
            for j in sortedRanks:
                if j != pairs[0]:
                    kickers.append(j)
                    if len(kickers) == 3:
                        return (pairs[0], kickers, "Pair of " + str(pairs[0]))
        else:
            return None
    
    @staticmethod
    def isHighCard(hand, board):
        ranks = [card.rank for card in hand + board]
        sortedRanks = sorted(ranks, reverse=True)
        highCard = sortedRanks[0]
        kickers = []
        for j in sortedRanks:
            if j != highCard:
                kickers.append(j)
                if len(kickers) == 4:
                    return (highCard, kickers, str(highCard) + " High")


    @staticmethod
    def handCompare(hands, board):
        evaluated_hands = [HandEval.handScore(hand, board) for hand in hands]
        # Determine the highest rank
        highest_rank = max(hand[0].value for hand in evaluated_hands)
        
        # Filter hands that have the highest rank
        highest_rank_hands = [hand for hand in evaluated_hands if hand[0].value == highest_rank]
        
        # If only one hand, it's the winner
        if len(highest_rank_hands) == 1:
            return highest_rank_hands[0]
        
        # Compare kickers if more than one hand has the highest rank
        best_hands = HandEval.compareKickers(highest_rank_hands)
        return best_hands
    
    @staticmethod
    def compareKickers(highest_rank_hands):
        # Assuming kickers are stored in the second index of the hand evaluation tuple
        # Continue comparing while there are multiple hands with the same rank
        current_best = highest_rank_hands
        kicker_index = 0
        
        while len(current_best) > 1 and kicker_index < len(current_best[0][2]):
            max_kicker = max(hand[2][kicker_index] for hand in current_best)
            current_best = [hand for hand in current_best if hand[2][kicker_index] == max_kicker]
            kicker_index += 1
            
        return current_best
        



