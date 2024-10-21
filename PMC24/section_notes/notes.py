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
    print("Not OK")
