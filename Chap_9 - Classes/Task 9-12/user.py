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
		
