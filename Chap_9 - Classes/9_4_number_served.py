"""
Start with your program from Exercise 9-1 (page 166).
Add an attribute called number_served with a default value of 0. Create an
instance called restaurant from this class. Print the number of customers the
restaurant has served, and then change this value and print it again.
Add a method called set_number_served() that lets you set the number
of customers that have been served. Call this method with a new number and
print the value again.
Add a method called increment_number_served() that lets you increment
the number of customers who’ve been served. Call this method with any number
you like that could represent how many customers were served in, say, a
day of business.
"""

# MODIFICATION IN CLASS ATTRIBUTES.

class Restaurant():
	"""A class to model restaurant."""
	
	# This special method will initialize the attributes
	# when class is instantiated.
	def __init__(self, restaurant_name, cuisine_type):
		"""Initialize the class attributes."""
		self.restaurant_name = restaurant_name.title()
		self.cuisine_type = cuisine_type.title()
		self.number_served = 0   # Attribute with default value.
		
	
	# A method to display restaurant details
	def describe_restaurant(self):
		"""Print information about restaurnat."""
		print("Restaurant Name: " + self.restaurant_name)
		print("Cuisine Type: " + self.cuisine_type)
		
		
	# 2 -- A method that will modify attribute through method
	def set_number_served(self, number_served):
		self.number_served  = number_served
		
	
	# 3 -- A method that will modigy attribute through method by
	# incrementing.
	def increment_number_served(self, customer_increment):
		self.number_served += customer_increment



# Instantiation of class
restaurant = Restaurant("hoogi boogie howls", 'large')

# 1 -- Modification of attribute direct.
# restaurant.number_served = 44

# no of customers, restaurant served.
print("Monday - Customer Served: " + str(restaurant.number_served))

restaurant.set_number_served(10)
print("Tuesday - Customer Served: " + str(restaurant.number_served))

restaurant.increment_number_served(4)
print("Wednesday - Customer Served: " + str(restaurant.number_served))

