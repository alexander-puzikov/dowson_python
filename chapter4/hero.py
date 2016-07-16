inventory = ()
if not inventory:
    input('your inventory is empty.Please, press enter key...')

inventory = ('armor', 'sword',
             'health potion', 'shield')
print('Courtesy has ', inventory)

print('Ones again inventory contains')
for item in inventory:
    print(item)
print('Now there is ' , len(inventory) , ' items in your inventory')
input('Press enter to continue...')
if 'health potion ' in inventory:
    print('you are lucky to have health potion!')

index = input('Please enter index position of item in inventory: ')
print('In position ' + str(index) + ' lies ' + inventory[int(index)])
input('Press enter to continue...')
chest =('gold', 'gems')
print('You have found a magic box with treaasures!')
print('There lies ', chest)
inventory += chest
print('You have added all this stuff to your inventory')
print(inventory[2:5])
