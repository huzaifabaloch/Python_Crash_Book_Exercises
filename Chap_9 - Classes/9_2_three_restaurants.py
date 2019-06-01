"""
Start with your class from Exercise 9-1. Create three
different instances from the class, and call describe_restaurant() for each
instance.
"""

# Creating multiple instances of a class, each instance will have 
# unique attributes and methods.

# Defining a class called Restaurant
class Restaurant():
	"""A class to model a restaurant"""
	
	def __init__(self, restaurant_name, cuisine_type):
		"""Initialize restaurant name and cuisine type"""
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		
	
	def describe_restaurant(self):
		"""All about restaurant"""
		print("The restaurant name is " + self.restaurant_name.title() + ".")
		print("The cuisine type is " + self.cuisine_type.title() + ".")
		print("\n")
	
	def open_restaurant(self):
		"""Restaurant is open"""
		print("Restaurant is open.")
		
		

# Instance 1
restaurant_1 = Restaurant("woogie hoogi howls", 'large')

# Instance 2
restaurant_2 = Restaurant("shezi", 'medim')

# Instance 3
restaurant_3 = Restaurant("lal qila", 'large')

# Calling method of instance 1
restaurant_1.describe_restaurant()

# Calling method of instance 2
restaurant_2.describe_restaurant()

# Calling method of instance 3
restaurant_3.describe_restaurant()
