"""
Write a function that accepts a list of items a person wants
on a sandwich. The function should have one parameter that collects as many
items as the function call provides, and it should print a summary of the sandwich
that is being ordered. Call the function three times, using a different number
of arguments each time.
"""

def order_sandwich(*toppings):
	
	print("\nYour sandwich contains the following items:")
	for each_topping in toppings:
		print(each_topping)
	

order_sandwich('extra chesse', 'muffins', 'dort')
order_sandwich('gatri', 'polo')
order_sandwich('chesse', 'muffins', 'yoghurt', 'fajita')

