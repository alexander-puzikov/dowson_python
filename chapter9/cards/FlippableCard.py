from  chapter9 import *


class UnprintableCard(Card):
    def __init__(self, rank, suit, isUp=True):
        super(UnprintableCard.self).__init__(rank, suit)
        self.is_up = isUp

    def __str__(self):
        if self.is_up:
            return super(UnprintableCard.self).__str__()
        else:
            return 'XX'
