class Person(object):
    name = "The guy has no name"

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name


per = Person()

print(per.getName())