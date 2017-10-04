import random


class Card(object):
    RANKS = ['A', '2', '3', '4', '5', '6', '7', '8', '9','10', 'J', 'Q', 'K']
    SUITS = ['CLUBS', 'DIAMONDS', 'SPADES', 'HEARDS']

    def __init__(self, rank, suit):
        self.__rank = rank
        self.__suit = suit

    def __str__(self):
        return '[' + self.__rank + ' ' + self.__suit + ']'


class Hand(object):
    def __init__(self):
        self.__cards = []

    def getCards(self):
        return self.__cards

    def setCards(self, cards):
        self.__cards = cards

    def __str__(self):
        result = ""
        if not self.__cards:
            result = 'Empty!'
        else:
            for card in self.__cards:
                result += str(card) + ' '
        return result

    def clear(self):
        self.__cards = []

    def add(self, card):
        self.__cards.append(card)

    def give(self, card, otherHand):
        self.__cards.remove(card)
        otherHand.__cards.append(card)


class Deck(Hand):
    def populate(self):
        cards = []
        for rank in Card.RANKS:
            for suit in Card.SUITS:
                cards.append(Card(rank, suit))
        self.setCards(cards)

    def shuffle(self):
        import random
        random.shuffle(self.getCards())

    def deal(self, hands, per_hands=1):
        for round in range(per_hands):
            for hand in hands:
                if self.getCards():
                    top_card = self.getCards()[0]
                    self.give(top_card, hand)
                else:
                    print('No more cards')

