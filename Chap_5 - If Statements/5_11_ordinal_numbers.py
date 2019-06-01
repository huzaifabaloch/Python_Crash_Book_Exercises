some_numbers = list(range(1, 10))

for each_number in some_numbers:
	if each_number == 1:
		print(str(each_number) + 'st')
	elif each_number == 2:
		print(str(each_number) + 'nd')
	elif each_number == 3:
		print(str(each_number) + 'rd')
	else:
		print(str(each_number) + 'th')
