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


for i in range(len(threes)):
    print(threes[i])
