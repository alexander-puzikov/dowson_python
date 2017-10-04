from cards import games
import random

print('Welcome to simple game')
again = None
while again != 'n':
    players = []
    # recent commits
    num = games.ask_number('How much players? (2-5', 2, 5)
    for i in range(num):
        name = raw_input('what is name of playes #' + str(i) + ': ')
        players.append(games.Player(name, random.randrange(100)))

    print('here is the game resuilt - ')
    for p in players:
        print(p)
    again = games.ask_yes_no('Again?')
input('press enter to quit')
