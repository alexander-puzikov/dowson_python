import shelve, pickle

print('loading from conserve')

file = open('resources/shelved.dat', 'rb')
vegetables  = pickle.load(file)
print(vegetables)