"""
Start with your work from Exercise 8-10. Call the
function make_great() with a copy of the list of magicians’ names. Because the
original list will be unchanged, return the new list and store it in a separate list.
Call show_magicians() with each list to show that you have one list of the original
names and one list with the Great added to each magician’s name.
"""

# MODIFYING A COPY OF LIST IN FUNCTION USING SLICE NOTATION [:]
# WITHOUT CHANGING THE ORIGINAL LIST

def make_great(magician_names, new_magician_list):
	
	counter = 0
	while magician_names:
		current_magician = magician_names.pop(counter)
		print("Adding Magician " + current_magician.title() + " to new list..")
		new_magician_list.append(current_magician)
		
		
def show_magicians(new_magician_list):
	
	print("\nThe following magicians performed last week:")
	for each_magician in new_magician_list:
		print(each_magician.title())
	 

magician_names = ['swit zak', 'bakiloko', 'imenianda', 'mizaanj', 'hawalai']
new_magician_list = []

make_great(magician_names[:], new_magician_list)
show_magicians(new_magician_list)

# Checking if orginal list magician_names is not modified.
print("\nChecking if orginal list magician_names is not modified.")
print(magician_names)
