
# example of a list of dictionaries

student_150 = {
	'full name': 'huzaifa shakeel ahmed',
	'batch': 2017,
	'semester': 5,
	}

student_147 = {
	'full name': 'usman shakeel',
	'batch': 2017,
	'semester': 5
	}

student_120 = {
	'full name': 'kashif ali',
	'batch': 2016,
	'semester': 7
	}

students = [student_150, student_147, student_120]
counter = 1

for each_student in students:
	print("Student No " + str(counter))
	print("-----------------------------\n")
	for key, value in each_student.items():
		if type(value) != int:
			print(key.title() + ": " + value.title())
		else:
			print(key.title() + ": " + str(value))
		
		counter += 1
	print("\n")
