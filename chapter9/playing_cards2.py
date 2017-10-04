from __future__ import print_function
from chapter9 import *

deck = Deck()
deck.populate()
print(deck)
print('\n')
print(deck)
vasya = Hand()
petya = Hand()
deck.deal([vasya, petya], 4)
print('Petya ' + petya.__str__(), end='\n')
print('Vasya ' + vasya.__str__())
print('left in deck ' + str(len(deck.getCards())))
