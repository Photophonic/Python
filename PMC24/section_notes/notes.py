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
