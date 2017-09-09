class Critter(object):
    legs = 4

    def __init__(self, name, hunger=0, bordom=0):
        self.__name = name
        self.__hunger = hunger
        self.__boredom = bordom

    def __pass_time(self):
        self.__boredom += 1
        self.__hunger += 1

    @property
    def mood(self):
        mood = self.__boredom + self.__hunger
        if mood < 5:
            return 'Excellent'
        elif mood < 10:
            return 'Normal'
        elif mood < 15:
            return 'Bad'
        else:
            return 'Worst mood ever'

    def __str__(self):
        return "My name is " + self.__name + " and i'm currently at " + self.mood + " mood"

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, newName):
        self.__name = newName

    @staticmethod
    def increaseLegs():
        Critter.legs += 1

    def play(self, play_time=1):
        print("Yehooo")
        self.__boredom -= play_time
        if self.__boredom < 0:
            self.__boredom = 0
        self.__pass_time()

    def eat(self, eat_amount=1):
        print('Murr, thanks!')
        self.__hunger -= eat_amount
        if self.__hunger < 0:
            self.__hunger = 0
        self.__pass_time()

    def talk(self):
        print(self.__str__())
        self.__pass_time()

    def hidden__str__(self):
        return str(self.__boredom) + ' ' + str(self.__hunger)

def main():
    name = raw_input("How will you call your critter!? ")
    crit1 = Critter(name, 1, 2)
    print(crit1)

    choice = None
    while choice != '0':
        print("""
        My critter:
        0 - Quit
        1 - Find out how does your critter feeling
        2 - To feed the critter
        3 - Play with critter!
        """)
        choice = raw_input("Your choice is: ")
        if choice == '0':
            print('Goodbye!')
        elif choice == '1':
            crit1.talk()
        elif choice == '2':
            feed_amount = int(raw_input("How much want to eat: "))
            crit1.eat(feed_amount)
        elif choice == '3':
            play_time = int(raw_input("How much want to eat: "))
            crit1.play(play_time)
        elif choice == '12321':
            print crit1.hidden__str__()
        else:
            print('Sorry there is no such choice in this menu')