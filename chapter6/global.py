def readGlobal():
    print('read ', value)


def shadowGlobal():
    value = 4
    print('shadow ', value)


def changeGlobal():
    global value
    value -= 4
    print('change ', value)


value = 10
readGlobal()
shadowGlobal()
changeGlobal()
