responses = {}

# Set a flag to indicate that polling is active.
polling_active = True

while polling_active:
	# Prompt for the person's name and response.
	name = input("\nWhat is your name? ")
	response = input("\nWhich mountain would you like to climb someday? ")
	
	# Store the response in the dictionary
	responses[name] = response
	
	# Find out if anyone else is going to take the poll.
	repeat = input("\nWould you like another person respond? ('yes'|'no') ")
	if repeat == 'no':
		polling_active = False
	
	
# Polling is complete. Show the results
for name, response in responses.items():
	print("\n")
	print(name.title() + " would like to climb " + response.title() + ".")
