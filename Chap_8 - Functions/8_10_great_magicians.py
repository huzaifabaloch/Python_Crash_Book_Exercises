"""
Start with a copy of your program from Exercise 8-9.
Write a function called make_great() that modifies the list of magicians by adding
the phrase the Great to each magician’s name. Call show_magicians() to
see that the list has actually been modified.
"""

# Modification of a list in function using while loop

def make_great(magician_names):
	
	counter = 0
	while counter < len(magician_names):
		magician_names[counter] += ' the Great'
		counter += 1
	

def show_magicians(magician_names):
	
	for each_magician in magician_names:
		print(each_magician.title())

magician_names = ['swit zak', 'bakiloko', 'imenianda', 'mizaanj', 'hawalai']

make_great(magician_names)
show_magicians(magician_names)

print("\n")
# Checking the list if it is really modified by function.
print(magician_names)
