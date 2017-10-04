from  chapter9 import *


class UnprintableCard(Card):
    def __str__(self):
        return "can't print me"
