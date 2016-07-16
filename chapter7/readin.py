file = open('resources/write.txt', 'r', encoding='UTF-8')
for line in file:
    print(line)

file.close()