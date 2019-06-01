"""
Start with a copy of user_profile.py from page 153. Build
a profile of yourself by calling build_profile(), using your first and last names
and three other key-value pairs that describe you.
"""

# Funcion to create user profile with first, last name and 
# some other extra information, storing in a dictionary.
def build_profile(first, last, **other_info):
	
	profile = {}
	profile['first name'.title()] = first.title()
	profile['last name'.title()] = last.title()
	
	for key, value in other_info.items():
		if type(value) != int:
			profile[key.title()] = value.title()
		else:
			profile[key.title()] = value 
	
	return profile


user_profile = build_profile('huzaifa', 'baloch',
							 gender = 'M', 
							 relationship = 'single',
							 address = 'lyari karachi',
							 friends = 203)

for key, value in user_profile.items():
	print(key + ': ' + str(value))							 
