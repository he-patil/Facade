from pytest import mark
from Card import Card

class Deck():
    def __init__(self, cards):
        self.cards = cards

    @staticmethod
    def createDeck():
        cards = []
        for j in range (4):
            for i in range(1,11):
                card = Card(i)
                cards.append(card)
            for i in range(3):
                card = Card(10)
                cards.append(card)
        return Deck(cards)