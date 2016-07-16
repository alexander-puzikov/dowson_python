file = open('resources/write.txt', 'w' , encoding='UTF-8')
file.write('First row \n')
file.write('This is second row\n')
file.write('And finally this is third row\n')
lines = (
    'the 1 of lines\n',
    'the second of lines\n',
    'the third of lines'
)
file.writelines(lines)
file.close()