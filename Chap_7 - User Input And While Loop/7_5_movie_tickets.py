no_quit = True
prompt = "MOVIE THEATRE\t -1 to quit\n"
prompt += "Kindly enter you age: "

while no_quit:
	age = int(input(prompt))
	if age == -1:
		no_quit = False
	elif age < 3:
		print("Ticket : Free")
	elif age >= 3 and age < 12:
		print("Ticket : 10$")
	else:
		print("Ticket : 15$")
	print("\n")
