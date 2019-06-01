"""
Write a separate Privileges class. The class should have one
attribute, privileges, that stores a list of strings as described in Exercise 9-7.
Move the show_privileges() method to this class. Make a Privileges instance
as an attribute in the Admin class. Create a new instance of Admin and use your
method to show its privileges.
"""

class User():
	"""An attempt to model a user."""
	
	def __init__(self, first_name, last_name, age, gender):
		"""To initialize the class attribtes."""
		self.first_name = first_name.title()
		self.last_name = last_name.title()
		self.age = age
		self.gender = gender.title()
		
		
	def describe_user(self):
		"""To display information about a user."""
		print("User Information:")
		print("First Name: " + self.first_name)
		print("Last Name: " + self.last_name)
		print("Age: " + str(self.age))
		print("Gender: " + self.gender)
	
	
	def greet_user(self):
		"""To greet a user."""
		message = "Hello " + self.first_name + ' ' + self.last_name + ", have a nice day!"
		return message
		
		
class Admin(User):
	"""Represent aspects of user, specific to admin."""
	
	def __init__(self, first_name, last_name, age, gender):
		super().__init__(first_name, last_name, age, gender)
		self.privileges = Privileges()
		
			
	def greet_user(self):
		"""To overrride the method of parent class."""
		message = "\nWelcome " + self.first_name + " " + self.last_name + ", you are allowed to:"
		return message


class Privileges():
	"""
	An attempt to model privileges for admin.
	To divide a large class into chunks of classes.
	as using - Instance as attributes -
	"""
	
	def __init__(self, privileges=['can add post', 'can delete post',
				 'can can user']):
					 self.privileges = privileges
					 
	def show_privileges(self):
		for each_privilege in self.privileges:
			print(each_privilege.title())


admin_101 = Admin('peter', 'marc', 24, 'male')
admin_101.describe_user()
print(admin_101.greet_user())
admin_101.privileges.show_privileges()
