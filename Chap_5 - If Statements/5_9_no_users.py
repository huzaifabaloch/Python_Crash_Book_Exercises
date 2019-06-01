user_names = ["tuna", "salmon", "trout", "admin", "pompano", "permit"]


'''
	Whenever deleting all the or some of the items using loop
	always remember that assign the length of a list - 1 in a variabe
	and loop through items one by one by deleting the last element first 
	and decrement the count variable.
	
	Deleting a single element like del list[3], will make python to 
	adjust the items inex that precedes after itis item. 
'''

count = len(user_names) - 1

for i in range(len(user_names)):
	del user_names[count]
	count -= 1
	
if not user_names:
	print("We need to find some users!")
	
