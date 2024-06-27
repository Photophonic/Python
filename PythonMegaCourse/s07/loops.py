#  for loops
today_temps = [75.2, 78.5, 82.4, 80.0]


def print_temp(temps):
    for temp in temps:
        print(round(temp))


print_temp(today_temps)

print("\n")

colors = [11, 34, 98, 43, 45, 54, 54]

for color in colors:
    print(color)

print("\n")

colors = [11, 34, 98, 43, 45, 54, 54]

for color in colors:

    if color > 50:
        print(color)

print("\n")

colors = [11, 34.1, 98.2, 43, 45.1, 54, 54]

for color in colors:
    if type(color) == int:
        print(color)

print("\n")


colors = [11, 34.1, 98.2, 43, 45.1, 54, 54]

for color in colors:
    if type(color) == int and color > 50:
        print(color)

print("\n")


student_grades = {"Bob": 98, "Sam": 82, "Josh": 80, "Rick": 72}

# specify the view obbject to loop over. This contains the K/V pairs
for student in student_grades.items():
    # this will return tuples
    print(student)


print("\n")

phone = {"John Smiht": "+37682929928", "Marry Simposon": "+8457326567293"}

for number in phone.items():
    print(f"{number[0]} has a number of {number[1]}")


print("\n")


phone_number = {"John Smiht": "+37682929928", "Marry Simposon": "+8457326567293"}

for key, value in phone_number.items():
    # use the replace method and declare what to replace and with what. 
    print(f"{key} has a number of {value.replace("+", "00")}")


# while loops
username = ''

while username != 'python':
    username = input("Enter Username:\n")
    

# a = 10

# while a > 0:
#     x = a + 1
#     print(x)


a = 0 

while a < 5:
    a = a + 1
    print(a)
