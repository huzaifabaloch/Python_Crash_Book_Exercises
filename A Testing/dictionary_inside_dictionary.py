# NESTING 
# DICTIONARY INSIDE ANOTHER DICTIONARY

#---------------------------------------------

'''
You can nest a dictionary inside another dictionary, but your code can get
complicated quickly when you do. For example, if you have several users
for a website, each with a unique username, you can use the usernames as
the keys in a dictionary. You can then store information about each user by
using a dictionary as the value associated with their username. In the following
listing, we store three pieces of information about each user: their
first name, last name, and location. We’ll access this information by looping
through the usernames and the dictionary of information associated with
each username:
'''

users = {
	'aeinstein': {
		'first': 'albert',
		'last': 'einstein',
		'location': 'london',
		},
		
	'mcurie': {
		'first': 'maire',
		'last': 'curie',
		'location': 'paris',
		},
	}

for username, user_info in users.items():
	print("\nUsername: " + username)
	full_name = user_info['first'] + " " + user_info['last']
	location = user_info['location']
	
	print("\tFull name: " + full_name.title())
	print("\tLocation: " + location.title())
