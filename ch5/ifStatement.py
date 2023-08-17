# If Statements
cars = ['audi', 'bmw', 'subaru', 'toyota']

# for loop
for car in cars:
    # if with equality check
    if car == 'bmw':
        # upper the whole word
        print(car.upper())
    else:
        # Upper just the first letter
        print(car.title())


# case is important when testing for equality.
# use something to level the values if case is not important for the test
car = 'Audi'
print(car == 'audi')  # returns false
print(car.lower() == 'audi')  # returns true
print("\n")

# != is for inequality NOT something
pizzaTopping = 'mushrooms'
if pizzaTopping != 'anchovies':
    print('Hold the anchovies please \n')

number = 13
if number != 27:
    print(f'{number} is not the correct number')

# checking multiple conditions with and/or
number1 = 13
number2 = 27

# both must evaluate TRUE to be true
print(number1 >= 21 and number2 >= 21)

# only one needs to evaluate to TRUE to be true
print(number1 > 0 or number2 > 20)


# check if a value is in a list
cars = ['audi', 'bmw', 'subaru', 'toyota', 'mini']
carInList = 'mini' in cars
print('Mini is in the list?', carInList)

carInList = 'mini' not in cars
print('Mini is not in the list?', carInList)


car = 'subaru'
print('is car == suabru?')
print(car == 'subaru')

print('\n is car == audi?')
print(car == 'audi')


# if statements

# simple if
age = 22
if age >= 18:
    print('You can go vote')
elif age >= 21:
    print('You can go to the beer store')
else:
    print('nice try')

# better example

age = 66

if age < 10:
    price = 0
elif age > 10 and age < 50:
    price = 20
else:
    price = 15
# pythoon does not require an end else as long as the conditions are covered
print(f'{price} is your price today')

# evaluating multiple conditions
pizzaToppings = ['pineapple', 'ham', 'sauce', 'cheese']
# if you need to test multiples, make various if conditions vs if/elif
if 'mushrooms' in pizzaToppings:
    print('Gross')
elif 'pineapple' and 'ham' in pizzaToppings:
    print('Man of culture right here')
if 'cheese' in pizzaToppings:
    print('adding more cheese')

print('\n')
# try it yourself
alien_color = 'red'
if alien_color == 'green':
    print(f'You selected {alien_color} as your color. +5 points')
else:
    print(f'You selected {alien_color} as you color, try again')

alien_color = 'yellow'
if alien_color == 'green':
    print(f'You selected {alien_color} as your color. +5 points')
elif alien_color == 'red':
    print(f'You selected {alien_color} as you color. +10 points')
else:
    print(f'You selected {alien_color} as you color, try again')
print('\n')


# if and lists
# Loop through the list and check the item to determine if/else behavoir
requestedToppings = ['mushroom', 'cheese', 'sausage', 'pepperoni']
for topping in requestedToppings:
    if topping == 'sausage':
        print("We're out of sausage")
    else:
        print(f'adding {topping}')
print("\nFinished the pizza\n")


# checking if the list is not empty
requestedToppings = []
if requestedToppings:
    for topping in requestedToppings:
        if topping == 'sausage':
            print("We're out of sausage")
        else:
            print(f'adding {topping}')
    print("\nFinished the pizza\n")
else:
    print("That's a plain pizza")


# using a list to validate another list
availableToppings = ['mushroom', 'cheese', 'sausage', 'pepperoni']

requestedToppings = ['cheese', 'pineapple', 'sausage']

# loop through the requested list
for requestedToping in requestedToppings:
    # check if the current item is in the validation list
    if requestedToping in availableToppings:
        # if yes, add item
        print(f'adding {topping}')
    else:
        # if not, so sorry
        print(f'Sorry, we do not have {requestedToping}')
print("\nFinished the pizza\n")


# Try it yourself
usernames = ['smith99', 'dole75', 'sjohns23', 'kart57', 'admin']

for username in usernames:
    if username.lower() == 'admin':
        print(f'Hello {username} here are the reports')
    else:
        print(f'Hello {username}')
print('\n')


usernames = []
if usernames:
    for username in usernames:
        if username.lower() == 'admin':
            print(f'Hello {username} here are the reports')
        else:
            print(f'Hello {username}')
else:
    print('We need som users')
print('\n')


current_users = ['ssmith', 'jdodson', 'bdole', 'spooter', 'broster']

new_users = ['cwass', 'Bdole', 'Trake', 'Broster', 'nright']

for new_user in new_users:
    if new_user.lower() in current_users:
        print(f'{new_user} already exists, please pick a new name')
    else:
        print(f'{new_user} has been created')
