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

todo = []
user_action = ""

while True:
    user_action = input("Type add, show, edit, or quit: \n")

    match user_action.strip():
        case "add":
            user_val = input("Enter a To Do: ")
            todo.append(user_val.title())
        case "show":
            for item in todo:
                print(item)
        case "edit":
            edit_item = int(input("Number of item to edit? "))
            adj_index = edit_item - 1
            new_todo = input("Enter a new To Do: ")
            todo[adj_index] = new_todo

        case "quit":
            break
        case _:
            pass
