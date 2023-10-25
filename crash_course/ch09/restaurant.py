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


# local_restaurant = Restaurant('Long Boards', 'Hawaiian style wraps')

# local_pizza = Restaurant('Waldo Pizza', 'Pizza')

# local_burger = Restaurant('Snack Shack', 'Burgers and Shakes')

# local_restaurant.describe_place()
# local_pizza.describe_place()
# local_burger.describe_place()

# local_restaurant.number_served()
# local_restaurant.update_served(50)
# local_restaurant.number_served()


# local_restaurant.increment_served('Day', 100)
# local_restaurant.increment_served('Week', 1500)
