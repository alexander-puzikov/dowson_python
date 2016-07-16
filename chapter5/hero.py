def wait():
    input('Press enter to continue...')


inventory = ()
if not inventory:
    input('your inventory is empty.Please, press enter key...')

inventory = ['armor', 'sword', 'health potion', 'shield']
print('Courtesy has ', inventory)

print('Ones again inventory contains')
for item in inventory:
    print(item)
print('Now there is ', len(inventory), ' items in your inventory')
wait()
if 'health potion ' in inventory:
    print('you are lucky to have health potion!')

index = int(input('Please enter index position of item in inventory: '))
if index >= len(inventory) or index < 0:
    print('You fealthy bastard! there is now such item in inventory')
else:
    print('In position ' + str(index) + ' lies ' + inventory[int(index)])
wait()
chest = ['gold', 'gems']
print('You have found a magic box with treaasures!')
print('There lies ', chest)
inventory += chest
print('You have added all this stuff to your inventory')
print(inventory[2:5])
wait()
print('you suddenly have changed your sword on arbalet')
inventory[inventory.index('sword')] = 'arbalet'
print(inventory)
wait()
print('and exchanged two of your items on magic crystal')
inventory[3:5] = ['magic crystal']
print(inventory)
wait()
print('Suddenly, a dragon attacked! You have lost all your armor and arbalet!')
del inventory[:3]
print(inventory)
