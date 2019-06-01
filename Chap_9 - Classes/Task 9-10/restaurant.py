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
		
