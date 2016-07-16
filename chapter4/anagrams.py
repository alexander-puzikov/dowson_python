import random

WORDS = ('penis', 'chick', 'dick', 'harder','library', 'mozart', 'stiffler', 'bold', 'python', 'monty')

word = random.choice(WORDS)
correct = word
jumble = ""
while word:
    index = random.randrange(0, len(word))
    jumble += word[index]
    word = word[:index] + word[index + 1:]

print('Your anagram is ', jumble)
tries = 1
answer = input('Please enter correct word: ')
while answer != correct:
    tries += 1
    answer = input('Try again: ')

print("Congratulations, this is indeed word " + correct)