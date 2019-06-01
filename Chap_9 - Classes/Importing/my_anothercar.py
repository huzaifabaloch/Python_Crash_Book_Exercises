# Importing a class from multiple classes module.
from anothercar import ElectricCar

# Importing multiple classes.
#from anothercar import Car, ElectricCar

my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
