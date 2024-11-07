# # text = input("Enter a title: ")
# # length = len(text)
# # print(length)

# countries = []
# while True:
#     country = input("Enter a country: ")
#     countries.append(country)
#     print(countries)
# import builtinsa

# print(dir(builtins))


# tuples and strings = immutable
# tuples should be used when the list should not change. Use ()
# Lists = mutable. Use []
# Dictionary = {}
filenames = ["1.Raw Data.txt", "2.Reports.txt", "3.Presentations.txt"]
new_files = []

# to work around this limitation, create a new string
for filename in filenames:
    # replace what with what and how many occurences
    filename = filename.replace(".", "-", 1)
    new_files.append(filename)

print(new_files)

# Day 5
# Question 1
# dollar = int(input("Enter a dollar amount: "))
dollar = 10
rate = 2

print(type(dollar))
print(type(rate))
conversion = dollar * rate
print(f"Converted rate is {conversion}")

# Question 2
ranking = ["Stan", "Kyle", "Kenny"]
# rank = int(input("Enter a ranking number: "))
rank = 0

print(ranking[rank])

# Question 3
ranking = ["Stan", "Kyle", "Kenny"]
# name = input("Enter a name for their rank: ")
name = "Stan"

print(ranking.index(name))


# Question 4
mood = "Here"
strength = 6.7
rank = 2

# Question 5
color_code = (
    ("#4062ce", "rgb(64,98,206)", "hsl(225.6,59.2%,52.9%)"),
    ("#2f3609", "rgb(47,54,9)", "hsl(69.3,71.4%,12.4%)"),
    ("#f19cd0", "rgb(241,156,208)", "hsl(323.3,75.2%,77.8%)"),
)

# Question 6
serials = [
    "hsl(225.6,59.2%,52.9%)",
    "hsl(69.3,71.4%,12.4%)",
    "hsl(323.3,75.2%,77.8%)",
    "hsl(129.2,12.5%,39.2%)",
]

print(serials[2])

# Question 7
seconds = [1.23, 1.45, 1.02]
current = 1.11

seconds.append(current)

print(seconds)


# debug
elements = ["a", "b", "c"]
print(elements[1])

elemebts = ["a", "b", "c"]

new = "x"
# new = elements[1]
elements[1] = new
print(elements)

# Day 6 - Enumeration & f string
mailing_list = ["stan", "kyle", "kenny", "cartman"]
mailing_list.sort()

for index, item in enumerate(mailing_list):
    row = f"{index+ 1}. {item.capitalize()}"
    print(row)

print(mailing_list)

# Question 1
filenames = ["document", "report", "presentation"]

for index, items in enumerate(filenames):
    print(f"{index}-{items.capitalize()}.txt")

# Question 2
ips = ["100.122.133.105", "100.122.133.111"]

user_input = int(input("Enter an index value: "))

print(f"You selected {ips[user_input]}")

# Question 3
temp = [1.2, 9, "test"]

# Question 4
rainfall = [5.2, 13, "test", [1, 2, 3, 4, 5]]

# Question 5
seconds = [1.23, 1.45, 1.02, 1.11]
removed = seconds.pop(1)
print(removed)
print(seconds)

# Debug 1
menu = ["pasta", "pizza", "salad"]

user_choice = int(input("Enter what you would like: "))

print(f"You selected {menu[user_choice]}")

# Demo
buttons = [("Stan", "Kyle", "Kenny"), ("Butters", "Craig", "Klyde")]

for first, second, third in buttons:
    print(first, second, third)


# Day 7 Reading Files

# Question 1
file = open("section_notes/files/bear.txt", "r")
print(file.read())
file.close()

# Question 2
file = open("section_notes/files/bear.txt", "r")
print(file.read().title())
file.close()

# Question 3
file = open("section_notes/files/bear.txt", "r")
print(len(file.read()))
file.close()

# Question 4
file = open("section_notes/files/file.txt", "a")
file.write("Snail")
file.close()

# Question 5
member = input("Enter a new member: ")

with open("section_notes/files/members.txt", "a") as file:
    file.write(f"\n{member}")

with open("section_notes/files/members.txt", "r") as file:
    print(file.read())


# Day 7 quiz
new = []

for i in [1, 2, 3]:
    new.append(i + 10)

print(new)


old = [1, 2, 3]
new = [i + 10 for i in old]
print(new)


# Question 1
names = ["stan marsh", "kyle brofloski", "kenny mccormick", "eric cartman"]

new_names = [name.title() for name in names]

print(new_names)


# Question 2
usernames = ["stan 1980", "kyle2020", "cartman1123"]

un_len = [len(user) for user in usernames]

print(un_len)


# Question 3
user_entries = ["10", "19.1", "20"]

new_entries = [float(entry) for entry in user_entries]

print(new_entries)

# Question 4
user_entries = ["10", "19.1", "20"]

new_entries = [float(entry) for entry in user_entries]

print(sum(new_entries))

# Bug Fix
# temp = [10, 20, 30]
# file = open("file.txt", "w")
# file.writelines(str(temp))

temps = [10, 20, 30]
temps = [str(temp) + "\n" for temp in temps]
file = open("file.txt", "w")

file.writelines(temps)


# Bug Fix
numbers = [10.1, 12.3, 14.7]

numbers = [int(item) for item in numbers]

print(numbers)


# Wil produce an error since the file does not exist
with open(r"section_notes\myfiles\docs.txt", "r") as file:
    items = file.read()
    print(items)


# Will open the existing file. Python will add 'r' as default
with open(r"section_notes\myfiles\doc.txt") as file:
    items = file.read()
    print(items)

# items becomes a variable to a closed file in this scope.
print(items)


# Day 8:
# question 1
# file = open(r"section_notes\myfiles\doc.txt", "w")
# file.write("snail")
# file.close


with open(r"section_notes\myfiles\doc.txt", "w") as file:
    file.write("Test")


# question 2
languages = ["English", "German", "Spanish"]


for language in languages:
    filename = language + ".txt"
    with open(filename, "a") as file:
        file.write(language)

# question 3
with open(r"section_notes\myfiles\story.txt", "r") as file:
    story = file.read()


with open(r"section_notes\myfiles\story_copy.txt", "w") as file:
    file.write(story)


# debug 1
with open(r"section_notes\myfiles\file.txt", "r") as file:
    content = file.read()


print(content)
print(len(content))


# Section 9 questions

# question 1
password = input("Enter a password: ")

if len(password) >= 7:
    print("Great password there!")
else:
    print("Your password is weak.")

# question 2
password = input("Enter a password: ")

pw_test = len(password)

if pw_test > 7:
    print("Great password there")
elif pw_test == 7:
    print("Your password is mid ")
else:
    print("Your password is weak")

# question 3 & 4
day_temp = {
    "morning": (44.2, 22.3, 58.1),
    "noon": (46.4, 15.7, 95.2),
    "evening": (40.1, 995.2, 25.5),
}


# question 5, 6, 7
letters = ["a", "b", "c", "d", "e", "f", "g"]

print(letters[1:4])
print(letters[:3])
print(letters[-3:])


# Debugging
ids = ["XF345_89", "XER76849", "XA454_55"]

x = 0

for id in ids:
    if "_" in id:
        x = x + 1
    print(x)
# the if needed to be indented

ids = ["XF345_89", "XER76849", "XA454_55"]

x = 0

for id in ids:
    if "_" in id:
        x = x + 1
# print needed to be moved outside of the loop
print(x)


length = float(input("Enter length: "))
width = float(input("Enter width: "))


perimeter = (length + width) * 2
area = length * width

print("Perimeter is", perimeter)
print("Area is", area)

# needed to fluo area > to <
if perimeter < 14 and area < 10:
    print("OK")
else:
    exit("Not OK")


# Day 10
# question 1
try:
    total_value = float(input("Enter total value: "))
    value = float(input("Enter value: "))
    result = value / total_value * 100

    print(f"That is {result}%")

except ValueError:
    print("You need tp enter a number. Run the program again")


# question 2
try:
    total_value = float(input("Enter total value: "))
    value = float(input("Enter value: "))
    result = value / total_value * 100

    print(f"That is {result}%")

except ValueError:
    print("You need tp enter a number. Run the program again")

except ZeroDivisionError:
    print("Your total value cannot be zero")

# question 3
colors = [11, 34, 98, 43, 45, 54, 54]

for color in colors:
    if color > 50:
        print(color)

# Bug Fix 1
waiting_list = ["john", "marry"]

name = input("Enter a name: ")
try:
    number = waiting_list.index(name)
    print(f"{name}'s turn in {number}")

except ValueError:
    print(f"{name} is not in the list")

#  other
try:
    "a" + 2
except TypeError:
    print("cannot add str to int")


print("a" + 2)


# Day 11 Functions
def greet():
    message = "hello"
    return message.capitalize()


greeting = greet()
print(greeting)


# Day 11 functions
# question 1
def get_max():
    grades = [9.6, 9.2, 9.7]

    value = max(grades)
    return value


print(get_max())


# question 2
def get_max():
    grades = [9.6, 9.2, 9.7]

    get_max = max(grades)
    get_min = min(grades)
    return f"Max: {get_max}, Min: {get_min}"


print(get_max())


# Day 12 decouple functions
def convert(feet_inches):
    # returns a list from a string split at the character
    imperial = feet_inches.split(" ")
    # assign each list position to a variable
    feet = float(imperial[0])
    inches = float(imperial[1])

    meters = feet * 0.3048 + inches * 0.0254

    return meters


feet_inches = input("Enter the feet and incehs: ")

meters = convert(feet_inches)

print(f"{meters} meters")

if meters < 1.0:
    print("too short")
else:
    print("have fun")


def get_feet_inches(feet_inches):
    imperial = feet_inches.split(" ")

    # assign each list position to a variable
    feet = float(imperial[0])
    inches = float(imperial[1])

    return (feet, inches)


def convert(feet, inches):

    meters = feet * 0.3048 + inches * 0.0254

    return meters


feet_inches = input("Enter the feet and incehs: ")

feet, inches = get_feet_inches(feet_inches)

meters = convert(feet, inches)

print(f"{meters} meters")

if meters < 1.0:
    print("too short")
else:
    print("have fun")


# day 12 more functions


# question 1
def liters_to_m3(liters):
    cubic_meter = liters / 1000

    return cubic_meter


print(liters_to_m3(2500))


# question 2
def strength(password):

    results = []
    pw_message = "Weak Password"

    if len(password) >= 8:
        results.append(True)
    else:
        results.append(False)

    # Use isdigit() method on the string to check for numbers
    # note, isdigit() cannot be used on a whole string.
    digit = False

    # use a loop to verify the individual character to check if digit
    for i in password:
        if i.isdigit():
            digit = True

    results.append(digit)

    capital = False
    for i in password:
        if i.isupper():
            capital = True

    if False in results:
        pw_message = "Weak Password"
    else:
        pw_message = "Strong Password"

    return pw_message


print(strength("test"))


# queston 3
def num_average(num_list):
    list_sum = sum(num_list)

    list_avg = list_sum / len(num_list)

    return int(list_avg)


print(num_average([10, 20, 30, 40]))


# question 4
def person_name(name):
    return f"Hi {name}"


print(person_name("Lisa"))


# question 5
def str_concat(item1, item2):
    return item1 + item2


print(str_concat("hello", "hi"))


# question 6
def greeting(name):
    return f"Hi {name.title()}"


print(greeting("john"))


def prepare(text):
    text = text.title()
    text = text.strip()
    return text


print(prepare("hello    "))


# Day 13 function parameters


# Question 1
def get_age(year_of_birth, current_year=2024):
    return int(current_year - year_of_birth)


print(get_age(1980))


#  Question 2
def get_nr_items(user_input):
    value = user_input.split(",")

    return len(value)


get_nr_items("john,lisa,teresa")


# Queston 3
def area(side_length):
    return side_length * side_length


print(area(7))


# Question 4
def temp(temp_in):
    if temp_in > 7:
        return "Warm"
    else:
        return "Cold"


print(temp(8))


# Question 5
def password_lenght(password):
    if len(password) >= 8:
        return True
    else:
        return False


print(password_lenght("mypass"))


# Debug, flip default parameter
def calculate_time(h, g=9.80665):
    t = (2 * h / g) ** 0.5
    return t


time = calculate_time(100)
print(time)


def get_area(x=10):
    return x * 2


area = get_area(x=1)
print(area)
