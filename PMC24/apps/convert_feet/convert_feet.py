# this will import all functions
from functions import *


feet_inches = input("Enter the feet and incehs: ")

feet, inches = get_feet_inches(feet_inches)

meters = convert(feet, inches)

print(f"{meters} meters")

if meters < 1.0:
    print("too short")
else:
    print("have fun")
