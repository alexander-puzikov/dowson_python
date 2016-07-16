X = 'X'
O = 'O'
EMPTY = ' '
TIE = 'tie'
SQUARES_NUM = 9


def askYesOrNo(question):
    response = None
    while response not in ('y', 'n'):
        response = input(question).lower()
    return response


def askNumber(question, low, high):
    number = None
    while number not in range(low, high):
        number = int(input(question))
    return number


def getHumanMove(board, human):
    legal = getLegalMoves(board)
    move = None
    while move not in legal:
        move = askNumber('Your move. Pick between 0 and 8: ', 0, SQUARES_NUM)
        if move not in legal:
            print(' You stupid human, this move is already been made!')
    print('ok')
    return move


def getComputerMove(board, computer, human):
    localBoard = board[:]
    BEST_MOVES = (4, 0, 2, 6, 8, 1, 3, 5, 7)
    print('I am going to choose field number... ', end=' ')
    for move in getLegalMoves(localBoard):
        localBoard[move] = computer
        if getWinner(localBoard) == computer:
            print(move)
            return move
        localBoard[move] = EMPTY

    for move in getLegalMoves(localBoard):
        localBoard[move] = human
        if getWinner(localBoard) == human:
            print(move)
            return move
        localBoard[move] = EMPTY
    for move in BEST_MOVES:
        if move in getLegalMoves(localBoard):
            print(move)
            return move


def congratulateWinner(winner, human, computer):
    if winner != TIE:
        print('Three ', winner, ' in a row!')
    else:
        print('Chichiwaki!')
    if winner == computer:
        print('As it was predicted, it was easy.')
    elif winner == human:
        print('This time you lucky, it will never happen again')


def nextTurn(turn):
    if turn == X:
        return O
    else:
        return X


def main():
    displayInstructions()
    computer, human = getPieces()
    turn = X
    board = newBoard()
    while not getWinner(board):
        if turn == human:
            move = getHumanMove(board, human)
            board[move] = human
        else:
            move = getComputerMove(board, computer, human)
            board[move] = computer
        displayBoard(board)
        turn = nextTurn(turn)
    winner = getWinner(board)
    congratulateWinner(winner, human, computer)


def getPieces():
    goFirst = askYesOrNo('Want to go first (y/n)?: ')
    if goFirst == 'y':
        print('Well, you have a handicap, play with crosses')
        human = X
        computer = O
    else:
        print('You will fail soon! Because I am starting')
        human = O
        computer = X
    return computer, human


def getWinner(board):
    WAYS_TO_WIN = ((0, 1, 2), (0, 3, 6), (3, 4, 5), (6, 7, 8), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for way in WAYS_TO_WIN:
        if board[way[1]] == board[way[2]] == board[way[0]] != EMPTY:
            return board[way[1]]
    if EMPTY not in board:
        return TIE
    else:
        return None


def newBoard():
    board = []
    for square in range(SQUARES_NUM):
        board.append(EMPTY)
    return board


def displayBoard(board):
    print("\n\t" + board[0] + '|' + board[1] + '|' + board[2])
    print("\t--------")

    print("\n\t" + board[3] + '|' + board[4] + '|' + board[5])
    print("\t--------")
    print("\n\t" + board[6] + '|' + board[7] + '|' + board[8] + '\n')


def getLegalMoves(board):
    moves = []
    for square in range(SQUARES_NUM):
        if board[square] == EMPTY:
            moves.append(square)
    return moves


def displayInstructions():
    """Prints instruction for player"""
    print(
        """
        Welcome, on fearless intellectual death match of all time!
        Your brain and my processor will fight in the game called 'Criss Cross'.
        To make move print number from 0 to 8. This numbers definitely matches
        with corresponding image below:
                0 | 1 | 2
                ---------
                3 | 4 | 5
                ---------
                6 | 7 | 8
          Prepare to die, you pitty meatbag. It is TIME!  for final battle!
        """)


main()
