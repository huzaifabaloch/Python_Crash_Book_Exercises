"""
An ice cream stand is a specific kind of restaurant. Write
a class called IceCreamStand that inherits from the Restaurant class you wrote
in Exercise 9-1 (page 166) or Exercise 9-4 (page 171). Either version of
the class will work; just pick the one you like better. Add an attribute called
flavors that stores a list of ice cream flavors. Write a method that displays
these flavors. Create an instance of IceCreamStand, and call this method.
"""

class Restaurant():
	"""An attempt to model a restaurant."""
	
	def __init__(self, restaurant_name, cuisine_type):
		"""Initilaize the class attributes."""
		self.restaurant_name = restaurant_name.title()
		self.cuisine_type = cuisine_type.title()
		
		
	def describe_restaurant(self):
		"""Print the restaurant information."""
		print("Restaurant Name: " + self.restaurant_name)
		print("Cuisine Type: " + self.cuisine_type)
		print("\n")
		

class IceCreamStand(Restaurant):
	"""
	Represents aspects of restaurant, specific to ice cream
	stand.
	"""
	
	def __init__(self, restaurant_name, cuisine_type):
		super().__init__(restaurant_name, cuisine_type)
		# An attribute(list) with default values.
		self.flavors = ['strawberry', 'mint', 'dark chocolate',
						'blue berry', 'dark crisp']
						
	
	def show_flavors(self):
		print("Flavor available here:")
		for each_flavor in self.flavors:
			print(each_flavor.title())	


# Creating an instance of IceCreamStand Class.
my_ice_stand = IceCreamStand('doopo ice', 'large')

# Calling the method from parent class.
my_ice_stand.describe_restaurant()

# Calling the method from child class to print ice-cream flavors.
my_ice_stand.show_flavors()
