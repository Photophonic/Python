class Restaurant:
    """Basic place to eat"""

    def __init__(self, name, style):
        self.name = name
        self.style = style
        self.served = 0
        self.span = ''

    def describe_place(self):
        print(f'{self.name} specializes in {self.style}')

    def open_busingess(self):
        print(f'{self.name} is now open for the day')

    def update_served(self, customers):
        self.served = customers

    def increment_served(self, span, customers):
        self.served += customers
        print(f'\nThere were {customers} in the last {self.span}')
        print(f'\nThis brings the total served to {self.served}')

    def number_served(self):
        print(f'The number of customers served is {self.served}')


class IceCream(Restaurant):
    """Simple extended class from restaurant"""

    def __init__(self, name, *style):
        """get methods and attributes of parent class"""
        super().__init__(name, style)

        self.flavors = ['Choclate', 'Vanilla', 'Rocky Road', 'Coffee']

    def describe_flavors(self):
        for flavor in self.flavors:
            print(flavor)


local_shop = IceCream("Betty Rae's", "Ice Cream")

local_shop.describe_flavors()
