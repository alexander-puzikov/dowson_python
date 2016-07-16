import pickle, shelve

print('Shelving lists')
variety = ['tomatos', 'apples', 'cabbage']
file = open('resources/shelved.dat', 'wb')
pickle.dump(variety, file)
file.close()
