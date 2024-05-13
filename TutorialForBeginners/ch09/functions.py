# define a function with def
def hello():
    print ("Hello!")

# call the function
hello()


def sum(num1, num2):
    print(num1 + num2)

# call the function with parameters
sum(2,8)
sum(10,3)
sum(1,2)


def sums(num1, num2):
    if (type(num1) is not int or type(num2) is not int):
        return 0 #('Error')
    else:
        return num1 + num2

total = sums(2,3)
print(type(total))
print(total)

total_str = sums('f', 't')
print(total_str)

# using default values
def sum_default(num1=2, num2=2):
    if (type(num1) is not int or type(num2) is not int):
        # return ('Error')
        # return 0 to keep things rolling vs a message
        return 0
    else:
        return num1 + num2
# will run as 1 + 2, returning 3
total = sum_default(1)
print(total)


# unknown number of parameters
# start with *
def multiple_items(*args):
    print(args)
    print(type(args))


multiple_items(1,'Dale', True)
# returns the args and type of tuple

# **kwargs collects all the keywords into a dictionary
def mult_names(**kwargs):
    print(kwargs)
    print(type(kwargs))

# must name the items else you will receive an error
mult_names(first = 'Bob', second = 'Sam', third = 'Dan')