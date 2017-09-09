import random
from chapter8 import critter


class Farm(object):
    def __init__(self, critters_count=0):
        self.__critters = []
        for i in range(critters_count):
            name = raw_input('Give name for your critter #' + str(i) + ' ')
            self.__critters.append(critter.Critter(name, random.randint(0, 4), random.randint(0, 4)))

    def play(self, play_time=1):
        for crit in self.__critters:
            crit.play(play_time)

    def eat(self, food_amount=1):
        for crit in self.__critters:
            crit.eat(food_amount)

    def talk(self):
        for crit in self.__critters:
            crit.talk()


def main():
    critter_count = int(raw_input('How much critters we will have in farm: '))
    farm = Farm(critter_count)
    choice = None
    while choice != '0':
        choice = raw_input("Your choice is: ")
        if choice == '0':
            print('Goodbye!')
        elif choice == '1':
            farm.talk()
        elif choice == '2':
            feed_amount = int(raw_input("How much want to eat: "))
            farm.eat(feed_amount)
        elif choice == '3':
            play_time = int(raw_input("How much want to eat: "))
            farm.play(play_time)
        else:
            print('Sorry there is no such choice in this menu')


main()
input('Press enter to quit')
