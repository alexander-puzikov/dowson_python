import random

print('Welcome to "guess the number" game!')
print('I think about natural number from 1 to 100...')
print('Try to guess this number using minimum of tries. Remember, you have only 5 attempts!')
the_number = random.randint(1, 100)
tries = 1
guess = int(input('Your guess is: '))
while guess != the_number and tries <= 5:
    if guess > the_number:
        print('Lower...')
    else:
        print('Higher...')
    guess = int(input('Your guess is: '))
    tries += 1
if tries <= 5:
    print('Congratulations, you did really guess the number ', the_number, '!')
    print('The number of your tries is ', tries)
else:
    print('You are fucking looser, a cunt, who cannot guess the number ', the_number, '!')