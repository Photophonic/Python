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

    def read_odometer(self):
        """read the odometer"""
        print(f'{self.model} has {self.odometer} miles on it.')


my_car = Car('toyota', '4Runner', 2021)
kelly_car = Car('mini', 'countryman', 2024)
print(my_car.get_description())
print(kelly_car.get_description())

# access the attribute directly and update it in MY instance of the class
# my_car.odometer = 40000

# The better way to do this is through a method in the class
my_car.update_odometer(40000)

my_car.read_odometer()

my_car.update_odometer(50000)

my_car.read_odometer()
