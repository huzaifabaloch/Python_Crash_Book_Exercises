"""
The module random contains functions that generate random numbers
in a variety of ways. The function randint() returns an integer in the
range you provide. The following code returns a number between 1 and 6:
from random import randint
x = randint(1, 6)
Make a class Die with one attribute called sides, which has a default
value of 6. Write a method called roll_die() that prints a random number
between 1 and the number of sides the die has. Make a 6-sided die and roll
it 10 times.
Make a 10-sided die and a 20-sided die. Roll each die 10 times.
"""
from random import randint

class Dice():
	"""An attempt to model a dice."""
	
	def __init__(self, sides=6):
		"""To initialize the dice attributes."""
		self.sides = sides
		
	def roll_die(self):
		"""To return a random number between user selected side."""
		if self.sides == 6:
			return randint(1, self.sides)
		elif self.sides == 10:
			return randint(1, self.sides)
		else:
			return randint(1, self.sides)


# Creating an instance of dice class.
random_number = Dice()

# Printing 6 sided die 10 times.
print("Rolling 6 sided die 10 times.")
print(random_number.roll_die())
print(random_number.roll_die())
print(random_number.roll_die())
print(random_number.roll_die())
print(random_number.roll_die())
print(random_number.roll_die())
print(random_number.roll_die())
print(random_number.roll_die())
print(random_number.roll_die())
print(random_number.roll_die())

# Modified the attribute value directly.
random_number.sides = 10

print("\nRolling 10 sided die 10 times.")
print(random_number.roll_die())
print(random_number.roll_die())
print(random_number.roll_die())
print(random_number.roll_die())
print(random_number.roll_die())
print(random_number.roll_die())
print(random_number.roll_die())
print(random_number.roll_die())
print(random_number.roll_die())
print(random_number.roll_die())

random_number.sides = 20

print("\nRolling 20 sided die 10 times.")
print(random_number.roll_die())
print(random_number.roll_die())
print(random_number.roll_die())
print(random_number.roll_die())
print(random_number.roll_die())
print(random_number.roll_die())
print(random_number.roll_die())
print(random_number.roll_die())
print(random_number.roll_die())
print(random_number.roll_die())


