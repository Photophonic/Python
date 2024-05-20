# basic syntax that will return a value
squared = lambda num: num * num

print(squared(2))

addTwo = lambda num: num + 2

print(addTwo(4))

# multi input
sum = lambda a, b: a + b

print(sum(2, 4))

print(sum(squared(2), addTwo(5)))

# #############


# example of how to use a lambda.


# create a function that takes an argument and returns the lambda output
def functionBuilder(x):
    return lambda num: num + x


# create a closure that passes in 10 as X
addTen = functionBuilder(10)
addTwenty = functionBuilder(20)

# call the variable containing the function and pass in our num variable
print(addTen(7))
# returns 17: X = 10 + num = 7 -> 17
print(addTwenty(7))
# returns 27: X = 20 + num = 7 -> 27


# Higher order functions
lambda num: num * num

numbers = [3, 5, 7, 12, 20, 23]

# map is a function built into python and takes a function as the first argument
# the second argument is the list we just created
squared_nums = map(lambda num: num * num, numbers)

# print out the contents on the list in a loop
# can also use print(list(squared_nums))
for _ in squared_nums:
    print(_)

# filter is another built in function
# check to see if equal, will return true/false
odd_nums = filter(lambda num: num % 2 != 0, numbers)
# filter will remove the values that do not meet the requirement
for _ in odd_nums:
    print(_)
