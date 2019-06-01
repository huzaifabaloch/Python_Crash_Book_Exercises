# FULL UNDERSTANDING OF CLASSES AND INHERITANCE.
# How to use an attribute with a default value.
# How to modify that attribute directly, throught method,
# and incrementing it thorugh method.

"""
INHERITANCE: if a class you writing contains things from the 
previous class, inheritance can be used. when one class inherits 
from another class, the original class is a parent class and the 
new class is a child class. the child class inherits every attibute
and method from the parent class but it is also free to define its
own new attributes and methods
"""

# Definition of parent class or super class. 
class Car():
	"""An attempt to model a car"""
	"""Every method in the class will have atleast a self parameter
		that is for attributes reference."""
	
	# Special python method that initialize all the attributes,
	# when class is instantiated.
	def __init__(self, make, model, year):
		"""Initialize car attributes."""
		# Self is parameter that is used as refernce for object.
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0  # Attribute with default value.
		
	
	def get_descriptive_name(self):
		"""To concatenate all the attributes of class and store in a 
			long_name attribute and returning."""
		long_name = str(self.year) + ' ' + self.make + ' ' + self.model
		return long_name
		
	
	def read_odometer(self):
		"""To display the car odometer reading."""
		print("This " + self.make.title() + " has " + str(self.odometer_reading) + " miles on it.")
		
		
	def update_odometer(self, mileage):
		"""To update the odometer reading of a car."""
		if mileage >= self.odometer:
			self.odometer_reading = mileage
		else:
			print("You can't roll back an odometer.")
			
	
	def increment_odometer(self, miles):
		"""To increment the odometer reading of a car."""
		self.odometer_reading += miles


# Definition of child class
class ElectricCar(Car):	
	"""This class will contain all the attributes and methods
		from the parent class -> Car as it used in the paranthesis that
		is inheriting from Car class."""
		
	"""
		When you create a child class, the parent class
		must be part of the current file and must appear before the child
		class in the file.
		
	"""
		
	"""Represent aspects of a car, specific to electric vehicles."""
	
	def __init__(self, make, model, year):
		"""Initialize attributes of the parent class."""
		# The super() function at is a special function that helps, 
		# Python make connections between the parent and child class.
		# This line tells Python to call the __init__() method from
		# ElectricCar’s parent class, which gives an ElectricCar instance
		# all the attributes of its parent class.
		super().__init__(make, model, year)


# An attempt to create an instance of child class.
my_audi = ElectricCar('Audi', 'A5', 2016)
print(my_audi.get_descriptive_name())
