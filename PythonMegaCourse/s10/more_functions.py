# functions with multiple arguments


# separate parameters with commas
def area(length, width):
    return length * width


# using non-keyword arguments, positional
print(area(3, 5))


# concat two strings
def concat(str_1, str_2):
    return str_1 + str_2


print(concat("string", "here"))


# default arguments with defaults
def concat(str_1, str_2="test"):
    return str_1 + str_2


# the default value will be used
print(concat("string"))
# this will override the default
print(concat("string", "here"))


# passing unknown number of arguments
# *args = non keyword arguments
#  **kwargs = keyword arguments
def mean(*args):
    return sum(args) / len(args)


print(mean(1, 2, 3, 4, 5, 6, 7, 8))


# average function
def average(*args):
    return int(sum(args) / len(args))


print(average(10, 20, 30, 40))


# return formatted list of strings
def string_formater(*args):
    args = [x.upper() for x in args]
    return sorted(args)


print(string_formater("snow", "glacier", "iceberg"))


# keyword arguments
def find_sum(**kwargs):
    return sum(kwargs.values())


print(find_sum(a=1, b=2, c=3, d=3))
