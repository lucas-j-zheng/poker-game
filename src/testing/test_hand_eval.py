import sys
import os

sys.path.append(os.getcwd())
#sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.utils import hand, card, deck, hand_eval, exceptions

class Testing:
    @staticmethod
    def test_straight_flush():
        card1 = card.Card.cardFromString('AS')
        print(card1)
        assert card1.rank == card.Rank.ACE
        assert card1.suit == card.Suit.SPADES

        hand1s = card.Card.cardsFromStrings(['AS', 'KS'])
        board1s = card.Card.cardsFromStrings(['QS', 'JS', 'TS', '3H', '5H'])
        
        hand1 = hand.Hand("joe",hand1s, board1s)
        hand_eval.HandEval.setHandScore(hand1)
        assert hand1.score == hand_eval.HandRank.STRAIGHTFLUSH
        print(hand1.cardsInPlay)
        print(hand1.score)
        print(hand1.scoreRank)

    @staticmethod
    def test_quads():
        hand1s = card.Card.cardsFromStrings(['AS', 'AD'])
        board1s = card.Card.cardsFromStrings(['QS', 'JS', 'TS', 'AH', 'AC'])
        hand1 = hand.Hand("joe",hand1s, board1s)
        hand_eval.HandEval.setHandScore(hand1)
        assert hand1.score == hand_eval.HandRank.QUADS

    @staticmethod
    def test_full_house():
        hand1s = card.Card.cardsFromStrings(['AS', 'AD'])
        board1s = card.Card.cardsFromStrings(['QS', 'JS', 'TS', 'AH', 'QC'])
        hand1 = hand.Hand("joe",hand1s, board1s)
        hand_eval.HandEval.setHandScore(hand1)
        assert hand1.score == hand_eval.HandRank.FULLHOUSE

    @staticmethod
    def test_flush():
        hand1s = card.Card.cardsFromStrings(['AS', '2S'])
        board1s = card.Card.cardsFromStrings(['3S', '5S', 'TS', 'AH', 'QC'])
        hand1 = hand.Hand("joe",hand1s, board1s)
        hand_eval.HandEval.setHandScore(hand1)
        assert hand1.score == hand_eval.HandRank.FLUSH

        hand1s = card.Card.cardsFromStrings(['AS', '2S'])
        board1s = card.Card.cardsFromStrings(['3S', '5S', 'TS', 'QS', 'QC'])
        hand1 = hand.Hand("joe",hand1s, board1s)
        hand_eval.HandEval.setHandScore(hand1)
        assert hand1.score == hand_eval.HandRank.FLUSH

    @staticmethod
    def test_straight():
        hand1s = card.Card.cardsFromStrings(['3S', '2C'])
        board1s = card.Card.cardsFromStrings(['4S', '5D', '6H', 'KH', 'QC'])
        hand1 = hand.Hand("joe",hand1s, board1s)
        hand_eval.HandEval.setHandScore(hand1)
        assert hand1.score == hand_eval.HandRank.STRAIGHT

        hand1s = card.Card.cardsFromStrings(['AS', '2S'])
        board1s = card.Card.cardsFromStrings(['3S', '4D', '5D', 'QC', 'KC'])
        hand1 = hand.Hand("joe",hand1s, board1s)
        hand_eval.HandEval.setHandScore(hand1)
        assert hand1.score == hand_eval.HandRank.STRAIGHT

    @staticmethod
    def test_set():
        hand1s = card.Card.cardsFromStrings(['3S', '2C'])
        board1s = card.Card.cardsFromStrings(['3D', '3H', '6H', 'KH', 'QC'])
        hand1 = hand.Hand("joe",hand1s, board1s)
        hand_eval.HandEval.setHandScore(hand1)
        assert hand1.score == hand_eval.HandRank.SET

    @staticmethod
    def test_twoPair():
        hand1s = card.Card.cardsFromStrings(['3S', '2C'])
        board1s = card.Card.cardsFromStrings(['3D', '3H', '6H', 'KH', 'QC'])
        hand1 = hand.Hand("joe",hand1s, board1s)
        hand_eval.HandEval.setHandScore(hand1)
        assert hand1.score == hand_eval.HandRank.SET
    @staticmethod
    def test_pair():
        hand1s = card.Card.cardsFromStrings(['3S', '2C'])
        board1s = card.Card.cardsFromStrings(['3D', '4H', '6H', 'KH', 'QC'])
        hand1 = hand.Hand("joe",hand1s, board1s)
        hand_eval.HandEval.setHandScore(hand1)
        assert hand1.score == hand_eval.HandRank.PAIR  

    @staticmethod
    def test_hand_compare_straight_flush():
        hand1s = card.Card.cardsFromStrings(['AS', 'KS'])
        board1s = card.Card.cardsFromStrings(['QS', 'JS', 'TS', '3H', '5H'])
        hand1 = hand.Hand("joe",hand1s, board1s)
        hand_eval.HandEval.setHandScore(hand1)
        hand2s = card.Card.cardsFromStrings(['QS', 'JS'])
        board2s = card.Card.cardsFromStrings(['TS', '9H', '8H', '3H', '5H'])
        hand2 = hand.Hand("joe",hand2s, board2s)
        hand_eval.HandEval.setHandScore(hand2)
        assert hand1.score > hand2.score

    