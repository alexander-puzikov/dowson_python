class Player(object):
    def blast(self, enemy):
        print('Players blasts into an enemy ')
        enemy.die()

class Alien(object):

    def die(self):
        print('Goodbye cruel world!')


print('Alien massacre!')
hero = Player()
invader = Alien()

hero.blast(invader)