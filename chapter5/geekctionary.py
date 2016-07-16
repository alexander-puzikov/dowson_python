dictionary = {'football': 'a game of 22 gays',
              'russia': 'the manliest football players ever'}

choice = None
while choice != 0:
    print('''
        0 - Exit
        1 - Show full dictionary
        2 - Show desctription by key
        3 - Add new item
        4 - delete item by key
        5 - Delete item by value
        6 - Update item
    ''')
    try:
        choice = int(input('What you will do next: '))
    except ValueError as e:
        print('You fool!')
        break
        
    if choice == 0:
        break
    elif choice == 1:
        print(dictionary)
    elif choice == 2:
        key = input('Please, enter the term you want to know: ')
        if key in dictionary:
            print(key + ' means ' + dictionary.get(key))
        else:
            print('No such term, in dictionary')
    elif choice == 3:
        key = input('Please, enter the term you want to add: ')
        if not key in dictionary:
            value = input('Please, enter description for this term: ')
            dictionary[key] = value
        else:
            print('There is already such term in dictionary')
    elif choice == 4:
        key = input('Please, enter the term you want to delete: ')
        if key in dictionary:
            del dictionary[key]
        else:
            print('No such term, in dictionary')
    elif choice == 5:
        desc = input('Please, enter the description you want to delete: ')
        if desc in dictionary.values():
            keyToDelete = None
            for item in dictionary.items():
                if item[1] == desc:
                    keyToDelete = item[0]
            if keyToDelete:
                del dictionary[keyToDelete]
        else:
            print('No such description found')
    elif choice == 6:
        key = input('Please, enter the term you want to add: ')
        if key in dictionary:
            value = input('Please, enter description for this term: ')
            dictionary[key] = value
        else:
            print('No such term in dictionary')
    else:
        print('You have picked the wrong choice fool!')
