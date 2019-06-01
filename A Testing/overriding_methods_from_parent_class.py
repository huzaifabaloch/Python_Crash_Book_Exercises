# OVERRIDING METHODS FROM PARENT CLASS.
"""
If a method in a child class doesnot fit what you are trying to model
, we can override that method. To do this we create a method in the child
with the same name as of parent class's method. Python will ignore the
method and only pay attention to method defined in child class.
Say the class Car had a method called fill_gas_tank(). This method is
meaningless for an all-electric vehicle, so you might want to override this
method.
"""

# Parent Class
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
		
# Child Class
class ElectricCar(Car):
	
	def __init__(self, name, model, year):
		# super method is used to connect parent and child class.
		# This line tells python to call the __init__() from ElectticCar
		# parent's class, which gives an instance of all the attributes
		# of parent class.
		super().__init__(name, model, year)
		
	# Overriding a parent class method fill_gas_tank() because,
	# an electric car doesnot need to fill gas.
	# For Overriding we use the same name of parent class's method.
	def fill_gas_tank(self):
		"""An electric car doesnot need to fill gas."""
		print("This car doesn't need a gas tank!")
		

my_car = ElectricCar('Audi', 'A5', 2016)
my_car.fill_gas_tank()
