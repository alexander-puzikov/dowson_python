print('Opening and closing file')
textFile = open('resources/text.txt', 'r', encoding='UTF-8')
textFile.close()
print('Reading file by char')
textFile = open('resources/text.txt', 'r')
print(textFile.read(1))
print(textFile.read(5))
textFile.close()
print('Reading the whole file ')
textFile = open('resources/text.txt', 'r', encoding='UTF-8')
wholeThing = textFile.read()
print(wholeThing)
textFile.close()
print('reading one line by char')
textFile = open('resources/text.txt', 'r', encoding='UTF-8')
print(textFile.readline(1))
print(textFile.readline(5))
textFile.close()
print('reading lines in list')
textFile = open('resources/text.txt', 'r', encoding='UTF-8')
lines = textFile.readlines()
print(lines)
print(len(lines))
for line in lines:
    print(line)
textFile.close()
print('reading file by lines')
textFile = open('resources/text.txt', 'r', encoding='UTF-8')
for line in textFile:
    print(line)
textFile.close()