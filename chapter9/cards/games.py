class Player(object):
    def __init__(self, name, score=0):
        self.name = name
        self.score = score

    def __str__(self):
        return self.name + ':\t' + str(self.score)


def ask_yes_no(question):
    response = None
    while response not in ('yes', 'no', 'y', 'n'):
        response = raw_input(question).lower()
    return response


def ask_number(question, low, high):
    response = None
    while response not in range(low, high):
        response = int(raw_input(question))
    return response


if __name__ == '__main__':
    input('You are fool! Press enter')
