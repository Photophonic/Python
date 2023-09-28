# # File name, import class name
# from car import Car

# my_new_car = Car('Toyota', 'GR86', 2024)

# print(my_new_car.get_description())


# To import all classes from a module
from elecCar import *
# ^ don't do this, better to specify what you're importing

my_car = ElectricCar('Toyota', 'Rav4 Prime', 2024)


print(my_car.get_description())
