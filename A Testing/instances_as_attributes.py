"""
When modeling something from the real world in code, you may find that
you’re adding more and more detail to a class. You’ll find that you have a
growing list of attributes and methods and that your files are becoming
lengthy. In these situations, you might recognize that part of one class can
be written as a separate class. You can break your large class into smaller
classes that work together.
"""

class Car():
	"""An attempt to model a car."""
	
	def __init__(self, name, model, year):
		"""Initialize all attributes of the class."""
		self.name = name.title()
		self.model = model
		self.year = year
		
		
	def fill_gas_tank(self):
		"""To fill gas in the car."""
		print("Filling gas in the car.")


class Battery():
	"""A simple attempt to model a battery for an electric car."""
	
	def __init__(self, battery_size=70):
		"""Initialize the battery's attributes."""
		self.battery_size = battery_size
		
		
	def describe_battery(self):
		"""Print a statement describing the battery size."""
		print("This car has a " + str(self.battery_size) + "-KWh battery.")
		
		
class ElectricCar(Car):
	"""Represent aspects of a car, specific to electric vehicles."""
	
	def __init__(self, make, model, year):
		"""
		Initialize attributes of the parent class.
		Then initialize attributes specific to an electric car.
		"""
		super().__init__(make, model, year)
	
		"""
		We now add an attribute called self.battery.
		This line tells Python to create a new instance of Battery (with a default size
		of 70, because we’re not specifying a value) and store that instance in the
		attribute self.battery. This will happen every time the __init__() method
		is called; any ElectricCar instance will now have a Battery instance created
		automatically.
		"""
		self.battery = Battery()


my_car = ElectricCar("Audi", "A5", 2016)
my_car.battery.describe_battery()
