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


# todo = []
# user_val = ""

# while True:
#     user_val = input("Enter a To Do: \n")

#     if user_val.upper() == "Q":
#         break

#     todo.append(user_val.title())

# for item in todo:
#     print(item)

# todo = []
# user_action = ""

# while True:
#     user_action = input("Type add, show, edit, or quit: \n")

#     match user_action.strip():
#         case "add":
#             user_val = input("Enter a To Do: ")
#             todo.append(user_val.title())
#         case "show":
#             for item in todo:
#                 print(item)
#         case "edit":
#             edit_item = int(input("Number of item to edit? "))
#             adj_index = edit_item - 1
#             new_todo = input("Enter a new To Do: ")
#             todo[adj_index] = new_todo

#         case "quit":
#             break
#         case _:
#             pass


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
name = input("Enter a name for their rank: ")

print(ranking.index(name))
