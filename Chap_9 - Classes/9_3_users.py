"""
Make a class called User. Create two attributes called first_name
and last_name, and then create several other attributes that are typically stored
in a user profile. Make a method called describe_user() that prints a summary
of the user’s information. Make another method called greet_user() that prints
a personalized greeting to the user.
Create several instances representing different users, and call both methods
for each user.
"""


class User():
	"""A model that contain a user"""
	
	def __init__(self, first_name, last_name, gender, car):
		"""Initialize user information"""
		self.first_name = first_name.title()
		self.last_name = last_name.title()
		self.gender = gender.title()
		self.car = car
		
		
	def describe_user(self):
		print("\nUser Information:")
		print("First Name: " + self.first_name)
		print("Last Name: " + self.last_name)
		print("Gender: " + self.gender)
		print("Have Car ?: " + str(self.car))
		
		
	def greet_user(self):
		full_name = self.first_name + " " + self.last_name
		print("\nHello " + full_name + ", have a nice day!")
	
# User 1
user_1 = User('huzaifa', 'baloch', 'm', False)
user_1.describe_user()
user_1.greet_user()


# User 2
user_2 = User('tuna', 'fish', 'm', False)
user_2.describe_user()
user_2.greet_user()
