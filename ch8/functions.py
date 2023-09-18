# # define the function with def .....
# def greet():
#     # the next line is a docstring enclosed in triple quotes. it allows multiline comments
#     # for the funtion
#     """Diplay a simple message:"""
#     print('Hello')


# # call the function to execute the code in the function body
# greet()

# # modify the function to take in user paramets


# def greet_name(username):
#     print(f'Hello {username.title()}!')


# # Create variable to hold user input.
# name = input('Enter your name here.\n')
# # pass the variable into the function.
# greet_name(name)


# def favorite_book(bookName):
#     print(f'My favorite book is {bookName.title()}.')


# book = input('Enter the name of your favorite book please.\n')
# favorite_book(book)

# # Passing multiple arguments into a function.
# # Positional


# def describe_pet(animal_type, pet_name):
#     print(f'\nI have a {animal_type.title()}.')
#     print(f'\nTheir name is {pet_name.title()}')


# describe_pet('cat', 'komi')
# describe_pet('cat', 'Beryl')
# describe_pet('dog', 'sebastian')

# # keyword arguments


# def describe_pet(animal_type, pet_name):
#     print(f'\nI have a {animal_type.title()}.')
#     print(f'\nTheir name is {pet_name.title()}')


# # Explicitly declare the name of the argument along with the input.
# describe_pet(pet_name='zeros', animal_type='cat')

# # to default a value, define it in the def
# # Default values must be listed at the end of the arguments


# def describe_car(car_model, car_make='toyota'):
#     print(f'\nI have a {car_make.title()}.')
#     print(f'\nIt is a {car_model.title()}')


# describe_car('4Runner')


# def make_tshirt(message, size='Medium'):
#     print(f'\nThe size of the shirt is {size}')
#     print(f'The message is "{message}".')


# make_tshirt(size='Large', message='Have a taco')

# # Return values in functions


# def get_foratted_name(first, last):
#     """Return formatted name"""
#     full_name = f"{first} {last}"
#     return full_name.title()


# fname = input(f'\nEnter your first name: ')
# lname = input(f'\nEnter your last name: ')

# formatted_name = get_foratted_name(fname, lname)
# print(f'Hi there {formatted_name}.')

# # making an input optional
# # default the middle to an empty value


def get_formatted_name(first, last, middle=''):
    """Updated to get middle name and make it optional"""
    # create a test condition against the middle name then return the proper result
    if middle:
        full_name = f"{first} {middle} {last}"
    else:
        full_name = f"{first} {last}"
    return full_name.title()


formatted_name = get_formatted_name(first='bob', last='dole')
print(formatted_name)

formatted_name = get_formatted_name(
    first='lee', middle='harvey', last='oswald')
print(formatted_name)


# returning a dictionary
# using a default Null value (none)
def build_person(first_name, last_name, age=None):
    """Return dictonary of person"""
    person = {'first': first_name, 'last': last_name, 'human': True}
    if age:
        # append the age variable, if available, into the person dictionary
        person['age'] = age
    return person


person = build_person('bob', 'dole', 98)
print(person)

for i in range(6):
    person = build_person('bob', 'dole', 98)
    print(person)


# passing lists into a function
def greet_users(names):
    """Print a simple greetin to each user"""
    for name in names:
        msg = f"Hello {name.title()}!"
        print(msg)


# create the list of names
usernames = ['Hanna', 'Bob', 'Billy', 'Sam']
# pass the list into the new function
greet_users(usernames)


# Modifying a list
# functions have access to the list contents and changes are permanent


# example without using functions
unprinted_designs = ['phone case', '40K army', 'game terrain', 'random crap']
printed_designs = []

while unprinted_designs:
    current_design = unprinted_designs.pop()
    print(f"\nPrinting {current_design}.")
    printed_designs.append(current_design)

print(f"\nThe following items have been printed")
for printed_design in printed_designs:
    print(printed_design)


unprinted_items = ['phone case', '40K army', 'game terrain', 'random crap']
printed_items = []

# Using a function to accomplish the same thing


def print_models(unprinted_designs, printed_models):
    """Simulate printing designs until none are left"""
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"\nPrinting {current_design}.")
        printed_models.append(current_design)


def show_complete_prints(printed_models):
    print(f"\nHere is a list of things you have printed:")
    for printed_design in printed_models:
        print(printed_design)


# use the list slice method to retain the original [:]
print_models(unprinted_items[:], printed_items)
show_complete_prints(unprinted_items)
show_complete_prints(printed_items)


print_models(unprinted_items, printed_items)
show_complete_prints(printed_items)


# using an argument with * will tell pythong to make a touple allowing unknown number of arguments
def make_pizza(*toppings):
    print(f"\nMaking your pizza with: ")
    for topping in toppings:
        print(f"Topping - {topping}")


my_pizza = ['cheese', 'ham', 'pineapple']
make_pizza('Cheese')
make_pizza(my_pizza)
make_pizza('ham', 'cheese', 'sauce', 'pineapple')


def make_sandwich(*ingredients):
    print(f"\nMaking sandwich with the following toppings:")
    for ingredient in ingredients:
        print(f'Adding {ingredient}')


make_sandwich('turkey')
make_sandwich('turkey', 'bacon', 'swiss')


# the ** tells python to create a dictionary of the extra K/V pairs used as arguments
def build_profile(first, last, **user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last
    # returns the created list to the calling item
    return user_info


user_profile = build_profile(
    'Bob', 'Dole', occupation='Senator', state='Kansas')

print(user_profile)


def car_info(make, model, **model_details):
    model_details['make'] = make
    model_details['model'] = model
    return model_details


my_car = car_info('Toyota', '4Runner', trim='SR5', drive='AWD', color='Red')

print(my_car)
