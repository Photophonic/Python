
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
