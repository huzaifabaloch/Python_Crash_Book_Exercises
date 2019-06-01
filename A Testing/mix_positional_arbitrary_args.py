# Mixing Positional and Arbitrary Arguments.

def make_pizza(size, *toppings):
	
	print("\nMaking a " + str(size) +
	"-inch pizza with the following toppings:")
	for topping in toppings:
		print("- " + topping)

make_pizza(6, 'pepperoni')
make_pizza(12, 'muffin', 'extra cheese', 'garlic')
