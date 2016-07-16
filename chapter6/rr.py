def display(message):
    print(message)


def givemMeFive():
    five = 5
    return five


def askYesOrNo(question):
    """' Ask a simple question with yes|no answer: '"""
    response = input(question)
    while response.lower() not in ('y', 'n'):
        response = input(question)
    return response



display("You have a message!")
number = givemMeFive()
print('Here is what givemMeFive function returned: ', number)
answer= askYesOrNo('Please enter y or n ')
print("thank you for choosing ", answer)
