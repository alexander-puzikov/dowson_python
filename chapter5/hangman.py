import random

HANGMAN = ('''
        -------^
        |/     |
        |      |
        |
        |
        |
        |
        |
        |
        _________
        ---------
        ''',
           '''
      -------^
      |/     |
      |      |
      |      O
      |
      |
      |
      |
      |
      _________
      ---------
      ''',
           '''
      -------^
      |/     |
      |      |
      |      O
      |     -+-
      |    / | \
      |
      |
      |
      _________
      ---------
      ''',
           '''
      -------^
      |/     |
      |      |
      |      O
      |     -+-
      |    / | \
      |      |
      |
      |
      _________
      ---------
      ''',
           '''
      -------^
      |/     |
      |      |
      |      O
      |     -+-
      |    / | \
      |      |
      |     /\
      |
      _________
      ---------
      ''',

           '''
      -------^
      |/     |
      |      |
      |      O
      |     -+-
      |    / | \
      |      |
      |     /\
      |    /  \
      _________
      ---------
      ''')
MAX_WRONG = len(HANGMAN) - 1

words = ('silly', 'rabbit', 'fly', 'like', 'eagle')
usedLetters = None
currentWord = random.choice(words)
guessed = '-' * len(currentWord)
wrongs = 0

while wrongs <= MAX_WRONG and guessed != currentWord:
    print(HANGMAN[wrongs])
    print('The word is ' + guessed)
    if usedLetters:
        print('Letters, you have picked: ' + usedLetters)
    print('You was wrong ' + str(wrongs) + ' times')
    nextLetter = None
    while nextLetter == None:
        nextLetter = input('Choose your next letter: ')
        if usedLetters and (len(nextLetter) > 2 or nextLetter in usedLetters):
            nextLetter = None
    newWord = ''
    if nextLetter in currentWord:
        for i in range(len(currentWord)):
            if currentWord[i] == nextLetter:
                newWord += nextLetter
            else:
                newWord += guessed[i]
        guessed = newWord
    else:
        wrongs += 1
if wrongs <= MAX_WRONG:
    print('Congratulations, this is indeed word ' + currentWord)