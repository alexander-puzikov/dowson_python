import random

print('Hi! i can predict what is your mood today ')
randmood = random.randint(0,3)

if randmood == 1:
    print("""
        --------
        | 0  0  |
        |   >   |
        | .  .  |
        |  ''   |
        ---------
    """)
    print('You are in a good mood...')
elif randmood == 2:
    print("""
            --------
            | 0  0  |
            |   >   |
            | ....  |
            |       |
            ---------
        """)
    print('You are in an average mood...')
elif randmood == 3:
    print("""
        --------
        | 0  0  |
        |   >   |
        |  ..   |
        | '  '  |
        ---------
    """)
    print('You are in a bad mood...')

else:
    print('You are joking, there isn\'t such mood...')
print("But it's only for today...")

