import random

word = input('Please, enter your word: ')
for letter in word:
    print(letter)

print('Length of your word is ', len(word))

print('is your word contains letter \'y\'? ', 'y' in word)
for i in range(10, 100, 13):
    print(i, end=" ")

for i in range(0, len(word)):
    ra = random.randint(0, len(word) - 1)
    print('letter ' + str(i) + ' = ' + word[ra])

print('now we are going to remove all vowels from your text.')
text = input('Please, enter your new text now: ')
VOWELS = 'eyuioa'
message = ""
for letter in text:
    if letter.lower() not in VOWELS:
        message += letter
        print('here is new string: ', message)

print("Finally, your text looks like this")
print(message[2:len(message)-1])
