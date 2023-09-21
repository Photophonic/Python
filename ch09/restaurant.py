class Restaurant:
    """Basic place to eat"""

    def __init__(self, name, style):
        self.name = name
        self.style = style

    def describe_place(self):
        print(f'{self.name} specializes in {self.style}')

    def open_busingess(self):
        print(f'{self.name} is now open for the day')


local_restaurant = Restaurant('Long Boards', 'Hawaiian style wraps')

local_pizza = Restaurant('Waldo Pizza', 'Pizza')

local_burger = Restaurant('Snack Shack', 'Burgers and Shakes')

local_restaurant.describe_place()
local_pizza.describe_place()
local_burger.describe_place()
