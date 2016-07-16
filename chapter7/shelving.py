import shelve, pickle

file = shelve.open('resources/shelved2.dat')
file['descrpitors'] = ['SIFT', 'SURF', 'GLOH', 'HOG']
file['brand'] = ['opencv', 'mathematica', 'ImageJ']
file.sync()
file.close()

file = shelve.open('resources/shelved2.dat')

print('reading from shelve')
print(file['descrpitors'])
print(file['brand'])