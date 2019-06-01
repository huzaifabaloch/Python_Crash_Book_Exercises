# Importing a single class.
from car import Car

my_new_car = Car('audi', 'a5', 2017)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 32
my_new_car.read_odometer()
