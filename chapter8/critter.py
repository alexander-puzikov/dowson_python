class Critter(object):
    legs = 4

    def __init__(self, name, hunger=0, bordom=0):
        self.__name = name
        self.__hunger = hunger
        self.__bordom = bordom

    def passTime(self):
        self.__bordom += 1
        self.__hunger += 1

    @property
    def mood(self):
        mood = self.__bordom + self.__hunger
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


crit1 = Critter("bobik", 1, 2)
crit2 = Critter("Tusik", 4, 1)

print(crit1)
print(crit2)
