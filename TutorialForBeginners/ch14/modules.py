import math, sys, random

# print a constant value from the math module
print(math.pi)

# can also have dictionaries, tuples, ect.


value = random.choice("123")
print(value)

# to import onluy specific items, use from/import
from enum import Enum

# this will only bring in Enum
# e.g. from math import pi

# to view the contents of a module use dir(), returns as a list
print(dir(math))

# easy way to pretty the list up, remember _ is a unnamed variable
# for _ in dir(math):
#     print(_)

# to view the actual useage, go to the docs
# https://docs.python.org/3/py-modindex.html


import kansas


for _ in dir(kansas):
    print(_)

kansas.randomfunfact()

# returns __main__ because this is the running module
print(__name__)
print(kansas.__name__)
