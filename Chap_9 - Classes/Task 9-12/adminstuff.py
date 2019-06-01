import user

class Admin(user.User):
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


