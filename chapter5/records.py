scores = []
text = '''
        0 - Exit
        1 - Add score
        2 - Show records
        3 - Sort records
        4 - Delete record by index
        5 - Delete record by value

        '''
choice = None
while choice != 0:
    print(text)
    choice = int(input('Enter your choise: '))
    if choice == 1:
        newName = input('Enter new name: ')
        newScore = input('Enter your new score: ')
        scores.append((newName, newScore))
    elif choice == 2:
        print(scores)
    elif choice == 3:
        scores.sort(reverse=True)
        print(scores)
    elif choice == 4:
        print(scores)
        index = int(input('Choose whos score you want to delete'))
        del scores[index]
    elif choice == 5:
        print(scores)
        value = input('Choose what score you want to delete')
        if value in scores:
            scores.remove(value)
        else:
            print('No such value')
    else:
        None


print('Thank you for playing')
