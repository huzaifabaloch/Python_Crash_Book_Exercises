"""
Make a class called Restaurant. The __init__() method for
Restaurant should store two attributes: a restaurant_name and a cuisine_type.
Make a method called describe_restaurant() that prints these two pieces of
information, and a method called open_restaurant() that prints a message indicating
that the restaurant is open.
Make an instance called restaurant from your class. Print the two attributes
individually, and then call both methods.
"""

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
		
	
	def open_restaurant(self):
		"""Restaurant is open"""
		print("Restaurant is open.")
		
# Instansiation of a class.
my_restaurant = Restaurant("woogie hoogi rodgers", "large")

# Accessing instance two attributes individually.
print(my_restaurant.restaurant_name)
print(my_restaurant.cuisine_type)

# Calling both methods.
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()

