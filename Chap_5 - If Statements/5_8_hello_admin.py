user_names = ["tuna", "salmon", "trout", "admin", "pompano", "permit"]

# this will check if the list is not empty and returns true, if it is not
if user_names:
	for user_name in user_names:
		if user_name == 'admin':
			print("\nHello " + user_name.title() + " would you like to see a report?")
		else:
			print("\nHello " + user_name.title() + " thank you for logging in again")
