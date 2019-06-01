prompt = "How many people are in your dinner group? "
no_of_people_for_dinner = int(input(prompt))

if no_of_people_for_dinner > 8:
	print("Sorry Sir, you will have to wait for a table.")
else:
	print("Your table is ready.")
