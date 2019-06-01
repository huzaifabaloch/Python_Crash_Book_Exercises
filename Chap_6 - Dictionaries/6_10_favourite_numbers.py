favourite_number = {
	'tuna': [3, 5, 78, 23],
	'pompano': [45, 76, 120],
	'permit': [41],
	'salmon': [78, 97],
	}

for name, numbers in favourite_number.items():
	if len(numbers) != 1:
		print(name.title() + "'s favourite numbers are: ")
		for number in numbers:
			print("\t" + str(number))
	else:
		print(name.title() + "'s favourite number is: ")
		for number in numbers:
			print("\t" + str(number))
	print("\n")
