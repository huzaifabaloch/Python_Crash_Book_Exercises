"""
Use the final version of electric_car.py from this section.
Add a method to the Battery class called upgrade_battery(). This method
should check the battery size and set the capacity to 85 if it isn’t already.
Make an electric car with a default battery size, call get_range() once, and
then call get_range() a second time after upgrading the battery. You should
see an increase in the car’s range.
"""

class Car():
	"""An attempt to model a car."""
	
	def __init__(self, name, model, year):
		"""To initialize the car attributes."""
		self.name = name.title()
		self.model = model.title()
		self.year = year
		
	
	def describe_car(self):
		"""To display car information."""
		print("Name of car: " + self.name)
		print("Model of car: " + self.model)
		print("Manufactured year: " + str(self.year))
		
		
class ElectricCar(Car):
	"""Represents aspects of Car, specific to ElectricCar."""
	
	def __init__(self, name, model, year):
		"""
		Special method that connects parent and child class.
		this line tells python that call __init__() of ElectricCar 
		parent class (Car) and make available all the attributes and 
		methods for this child class when it is instantiated.
		"""
		super().__init__(name, model, year)
		# Created an instance as attribute with a user-defined value 75,
		# where default value is 70.
		self.battery = Battery(75)
		

class Battery():
	"""An attempt to model the battery of ElectriCar."""
	
	def __init__(self, battery_size=70):
		"""To initialize the battery"""
		self.battery_size = battery_size
		
		
	def describe_battery(self):
		"""Print a statement describing the battery size."""
		print("This car has a " + str(self.battery_size) + "-kWh battery.")
		
	
	def get_range(self):
		"""Print a statement about the range this battery provides."""
		if self.battery_size == 75:
			range = 240
		elif self.battery_size == 85:
			range = 270
			
		message = "This can go approximatley {}".format(str(range))
		message += " miles on a full charge." 
		print(message)
	
	
	def upgrade_battery(self):
		"""Setting the range of car to 85 if it is not."""
		if self.battery_size != 85:
			self.battery_size = 85 
	
	
car_101 = ElectricCar('tesla', 'model s', 2016)
car_101.describe_car()
car_101.battery.describe_battery()
car_101.battery.get_range()
car_101.battery.upgrade_battery()
car_101.battery.get_range()
