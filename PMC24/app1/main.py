# # text = input("Enter a title: ")
# # length = len(text)
# # print(length)

# countries = []
# while True:
#     country = input("Enter a country: ")
#     countries.append(country)
#     print(countries)

# import builtins

# print(dir(builtins))


todo = []
user_val = ""

while True:
    user_val = input("Enter a To Do: \n")

    if user_val.upper() == "Q":
        break

    todo.append(user_val.title())

for item in todo:
    print(item)
