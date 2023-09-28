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


class Battery:
    """A simple class for an electric car's batter"""

    def __init__(self, battery_size=40):
        """Initialize the battery settings"""
        self.battery_size = battery_size

    def describe_battery(self):
        print(f'This car has a {self.battery_size}-kWh')

    def upgrade_battery(self):
        if self.battery_size < 65:
            self.battery_size = 65

    def get_range(self):
        if self.battery_size == 40:
            range = 200
        elif self.battery_size >= 60:
            range = 400

        self.describe_battery()
        print(f'The car can go {range} miles on a full charge.')


class ElectricCar(Car):
    """class for an electric car, inheriting the Car class"""

    # Note, used double _ not triple _
    def __init__(self, make, model, year):
        """define items specific to the Electric car"""
        # super() allows you to call methods from the parent class
        super().__init__(make, model, year)

        # now that a child class is connected, you can add your own
        # special attributes unique to this class

        self.drive = '2WD'
        self.battery = Battery()

    def get_range(self):
        print(
            # to access the properties of the battery class, preface the value with the owning class .BATTERY.BAT_SIZ
            f'\nThe {self.make} {self.model} has a {self.battery.battery_size}-kWh battery.')


# my_car = ElectricCar('Toyota', 'Rav4 Prime', 2024)


# my_car.battery.get_range()

# my_car.battery.upgrade_battery()

# my_car.battery.get_range()
