import random



class Card(object):
    RANKS = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'J', 'Q', 'K']
    SUITS = ['CLUBS', 'DIAMONDS', 'SPADES', 'HEARDS']

    def __init__(self, rank, suit):
        self.__rank = rank
        self.__suit = suit

    def __str__(self):
        return '[' + self.__rank + ' ' + self.__suit + ']'


class Hand(object):
    def __init__(self):
        self.__cards = []

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


card1 = Card(random.choice(Card.RANKS), random.choice(Card.SUITS))
card2 = Card(random.choice(Card.RANKS), random.choice(Card.SUITS))
card3 = Card(random.choice(Card.RANKS), random.choice(Card.SUITS))
card4 = Card(random.choice(Card.RANKS), random.choice(Card.SUITS))
card5 = Card(random.choice(Card.RANKS), random.choice(Card.SUITS))
myHand = Hand()
print(myHand)
myHand.add(card1)
myHand.add(card2)
myHand.add(card3)
myHand.add(card4)
myHand.add(card5)
print(myHand)
yourHand = Hand()
myHand.give(card2,yourHand)
print(myHand)
print(yourHand)
