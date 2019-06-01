"""
Make a list of magician’s names. Pass the list to a function
called show_magicians(), which prints the name of each magician in the list.
"""
# USE OF LIST IN A FUNCTION

# Defining a function.
def show_magicians(magician_names):
	
	print("\nThis is a list of magicians performed last week:.\n")
	for each_magician in magician_names:
		print(each_magician.title())
	

magician_names = ['swit zak', 'bakiloko', 'imenianda', 'mizaanj', 'hawalai']

# Calling a function.
show_magicians(magician_names)
