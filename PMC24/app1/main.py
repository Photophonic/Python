# text = input("Enter a title: ")
# length = len(text)
# print(length)


todo = []
user_val = ""

while True:
    user_val = input("Enter a To Do: \n")

    if user_val.upper() == "Q":
        break

    todo.append(user_val)

for item in todo:
    print(item)
