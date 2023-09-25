class Car:
    """A class for cars"""

    def __init__(self, make, model, year):
        """Initialize the car"""
        self.make = make
        self.model = model
        self.year = year
        # this sets a default value for an attribute in the class
        self.odometer = 0

    def get_description(self):
        """Return formatted information"""
        long_name = f'{self.year} {self.make} {self.model}'
        return long_name.title()

    def update_odometer(self, mileage):
        """Update the odometer"""
        if (mileage >= self.odometer):
            self.odometer = mileage

    def increment_odometer(self, mileage):
        self.odometer += mileage

    def read_odometer(self):
        """read the odometer"""
        print(f'{self.model} has {self.odometer} miles on it.')


class ElectricCar(Car):
    """class for an electric car, inheriting the Car class"""

    # Note, used double _ not triple _
    def __init__(self, make, model, year):
        """define items specific to the Electric car"""
        # super() allows you to call methods from the parent class
        super().__init__(make, model, year)

        # now that a child class is connected, you can add your own
        # special attributes unique to this class
        self.range = 400
        self.drive = '2WD'

    def get_range(self):
        print(f'\nThe {self.make} {self.model} has a range of {self.drive}')


my_Leaf = ElectricCar('Toyota', 'Rav4 Prime', '2024')
my_Leaf.get_range()


# my_car = Car('toyota', '4Runner', 2021)
# kelly_car = Car('mini', 'countryman', 2024)
# print(my_car.get_description())
# print(kelly_car.get_description())

# # access the attribute directly and update it in MY instance of the class
# # my_car.odometer = 40000

# # The better way to do this is through a method in the class
# my_car.update_odometer(40000)

# my_car.read_odometer()

# my_car.update_odometer(50000)

# my_car.read_odometer()
