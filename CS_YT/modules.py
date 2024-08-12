# not really used so don't use it
# from my_module import *

# Python will check sys.path to look for module directories
# import sys
# print(sys.path)


# import my_module from a

# import my_module from a different folder

import sys

sys.path.append("modules")

from my_module import find_index

courses = ["Math", "Science", "History", "CompSci"]


index = find_index(courses, "CompSci")

print(index)


import random

random_course = random.choice(courses)
print(random_course)


import math

rads = math.radians(90)

print(rads)

import datetime


today = datetime.date.today()
print(today)


import os

# get current working directory
print(os.getcwd())

# see where this lives and able to open it to vide
print(os.__file__)

import antigravity
