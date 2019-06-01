"""
An administrator is a special kind of user. Write a class called
Admin that inherits from the User class you wrote in Exercise 9-3 (page 166)
or Exercise 9-5 (page 171). Add an attribute, privileges, that stores a list
of strings like "can add post", "can delete post", "can ban user", and so on.
Write a method called show_privileges() that lists the administrator’s set of
privileges. Create an instance of Admin, and call your method.
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
		# An attributes(list) with default values.
		self.privileges = ['can add post', 'can delete post', 'can ban user']
		
	
	def show_privileges(self):
		"""to display each task an admin can do."""
		for each_privilege in self.privileges:
			print(each_privilege.title())
			
			
	def greet_user(self):
		"""To overrride the method of parent class."""
		message = "\nWelcome " + self.first_name + " " + self.last_name + ", you are allowed to:"
		return message

# Instantiation of class Admin.
admin_101 = Admin('huzaifa', 'baloch', 20, 'male')
admin_101.describe_user()
print(admin_101.greet_user())
admin_101.show_privileges()
	
		
