cars = ['toyota', 'subaru', 'mazda', 'ford', 'kia']

print(sorted(cars))


for car in sorted(cars):
    # print(car)
    print(f"{car.title()}, is a pretty sweet car")
    # remember \n is new line
    print(f"{car.title()}, are all over the road.\n")

print("cars are sure expensive.")

# specify an incrementor with range
for i in range(1, 6):
    print(i)

# you can pass one argument and range will start at 0
for i in range(5):
    print(i)

# to use range to populate a list
numbers = list(range(1, 6))
print(numbers)

# you can add a thrid value as a step size
numbersEven = list(range(0, 11, 2))
print(numbersEven)

# creating an empyt list
squares = []

# range a loop 1~10
for value in range(1, 11):
    # create variable to hold the squared current range value
    square = value ** 2
    # uses list method .appedn(X) to add the new value to the list. Similar to push for arrays
    squares.append(square)

print(squares)

# a cleaner versiom
squares = []
for value in range(1, 11):
    squares.append(value**2)

print(squares)

# built in number functions similar to SQL
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

print(min(digits))

print(max(digits))

print(sum(digits))

# list comprehension, this is a mashup of all the other items
squares = [value**2 for value in range(1, 11)]
print(squares)


for i in range(1, 21):
    print(i)

numbers = list(range(1, 9))
for i in range(len(numbers)):
    print(numbers[i])


print(sum(numbers), min(numbers), max(numbers))


numbersOdd = list(range(1, 50, 2))
for i in range(len(numbersOdd)):
    print(numbersOdd[i])

squares = []
for value in range(1, 11):
    squares.append(value**2)


threes = []
for i in range(3, 30):
    threes.append(i**2)


list_of_multiples_of_3 = [x for x in range(1, 100) if x % 3 == 0]

print(list_of_multiples_of_3)

list3 = list(range(0, 30, 3))
print(list3)

# Slicing lists
# like range, slice values dictate the beginning and end range to work with
discord = ['Me', 'Billy', 'Yoshi', 'Richard', 'Sabrina', 'Anthony']
print(discord[2:5])

# without an index Python will start at the beginnig
print(discord[:4])
# starts from designated element to the end
print(discord[3:])
# negative starts at the back and revereses
print(discord[:-2])

# to loop through a list with slice
print("These people play HSR:")
for d in discord[0:3]:
    print(d)

# use [:] to make a copy of a whole list and assign that to a new variable
acen = discord[:]
# to prove it is a different list
acen.append('William')
for soon in acen[0:]:
    print(soon)

print('the first three items are:')
for ff in discord[0:3]:
    print(ff)

print('The middle items are:')
for ff in discord[3:5]:
    print(ff)

print('The last ones are:')
for ff in discord[-2:]:
    print(ff)

print("\n")

# my pizza list
myPizza = ['Pineapple', 'Meat', 'cheese', 'sauce']
# slice a new list startin at index 1 (not 0)
kellyPizza = myPizza[1:]
# add a new item to the new list with append
kellyPizza.append('sausage')
# pring the first list using a for loop with an open range
for p in myPizza[:]:
    print(p)
print("\n")
# pring the sencond list with same options
for k in kellyPizza[:]:
    print(k)


# an immutable list is known as a tuple
# defined by () instead of []
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1], "\n")

# this will error since you cannot change a tuple
# dimensions[0] = 250

# looping through a tuple is similar
for dimension in dimensions:
    print(dimension, "\n")

# Tuples can be overwriten
dimensions = (400, 100)
for dimension in dimensions:
    print(dimension)

print("\n")

dinnerMenu = ('Pasta', 'Pizza', 'BBQ', 'Wrap')
for meal in dinnerMenu:
    print(meal)
print("\n")

# dinnerMenu[2] = 'taco'

dinnerMenu = ('Pasta', 'Pizza', 'Taco', 'Burger')
for meal in dinnerMenu:
    print(meal)
print("\n")
