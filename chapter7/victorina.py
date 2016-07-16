import sys


def openFile(path):
    try:
        file = open(path, 'r+', encoding='UTF-8')
        return file
    except IOError as e:
        print('Could not open file due to error: \n', e, '\n Program will shut down immediately')
        input('Press enter to exit')
        sys.exit(-1)


def nextLine(file):
    line = file.readline()
    line = line.replace('/', '\n')
    return line


def nextBlock(file):
    category = nextLine(file)
    question = nextLine(file)
    answers = []
    for i in range(0, 4):
        answers.append(nextLine(file))
    correctAnswer = nextLine(file)
    whyIs = nextLine(file)
    return category, question, answers, correctAnswer, whyIs


def welcome(title):
    print("Hello, dear friend! Title of this game is " + title)


def main():
    score = 0
    fileName = 'resources/trivia.txt'
    file = open(fileName, 'r', encoding='UTF-8')
    title = nextLine(file)
    welcome(title)
    while True:
        category, question, answers, correctAnswer, explanation = nextBlock(file)
        if not category:
            break
        print('The category is ', category, ' end your question is...')
        print(question, end='')
        for i in range(0, len(answers)):
            print(i + 1, ' ', answers[i])
        answer = input('What is your choice: ')
        if int(answer) == int(correctAnswer):
            print('You are right! Indeed, ', end='')
            score += 1
        else:
            print('You are wrong!')
        print(explanation)

    file.close()


main()
