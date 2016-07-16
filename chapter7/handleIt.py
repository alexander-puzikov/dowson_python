try:
    num = float(input('Please, enter a number: '))
except ValueError as e:
    print('Looks like this is not number ', e)
else:
    print('You have entered correct number')
for value in (None, 'text'):
    try:
        print('Trying to convert value ', value, ' to float')
        print(float(value))
    except  TypeError:
        print('ERROR!')
    except ValueError:
        print("VERROR")
