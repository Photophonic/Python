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
