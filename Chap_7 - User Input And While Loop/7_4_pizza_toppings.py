active = True

while active:
	topping = input("Enter Your toppings: ")
	if topping == 'quit':
		active = False
	else:
		print("You'll add " + topping.title() + " to their pizza.\n")
