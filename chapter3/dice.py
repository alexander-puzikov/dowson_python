# dice demo
import random

die1 = random.randint(1,6)
die2 = random.randint(1,6)#random.randrange(6) + 1
total = die1 + die2
print(" Throwing dice comes up with sum " + str(die1) + " + " +  str(die2) + " = " + str(total))
