"""
Add an attribute called login_attempts to your User
class from Exercise 9-3 (page 166). Write a method called increment_
login_attempts() that increments the value of login_attempts by 1. Write
another method called reset_login_attempts() that resets the value of login_
attempts to 0.
Make an instance of the User class and call increment_login_attempts()
several times. Print the value of login_attempts to make sure it was incremented
properly, and then call reset_login_attempts(). Print login_attempts again to
make sure it was reset to 0.
"""


class User():
	"""A model that contain a user"""
	
	def __init__(self, first_name, last_name, gender):
		"""Initialize user information"""
		self.first_name = first_name.title()
		self.last_name = last_name.title()
		self.gender = gender.title()
		self.login_attempts = 0
		
		
	def describe_user(self):
		print("\nUser Information:")
		print("First Name: " + self.first_name)
		print("Last Name: " + self.last_name)
		print("Gender: " + self.gender)
		
		
	def greet_user(self):
		full_name = self.first_name + " " + self.last_name
		print("\nHello " + full_name + ", have a nice day!")
		
		
	def increment_login_attempts(self, login_attempts):
		self.login_attempts += login_attempts
		
	
	def reset_login_attempts(self):
		self.login_attempts = 0
		

user1 = User('huzaifa', 'baloch', 'm')

# Login attempting...
user1.increment_login_attempts(1)
user1.increment_login_attempts(1)
user1.increment_login_attempts(1)
user1.increment_login_attempts(1)
user1.increment_login_attempts(1)
user1.increment_login_attempts(1)
print(user1.login_attempts)

# Reseting 
user1.reset_login_attempts()
print(user1.login_attempts)
