# Optimized version
user_action = ""

while True:
    user_action = input("Type add, show, edit, complete, or quit: \n").strip()

    # python case statement to compare user_action input
    match user_action.strip():
        case "add":
            user_val = input("Enter a To Do: ") + "\n"

            # revised read file using WITH context manager
            with open("app01_todo\list.txt", "r") as file:
                todo = file.readlines()

            # add to the list the capitalize user_input
            todo.append(user_val.title())

            # revised write using WITH
            with open("app01_todo\list.txt", "w") as file:
                file.writelines(todo)

        case "show":
            # revised read file using WITH context manager
            with open("app01_todo\list.txt", "r") as file:
                todo = file.readlines()

            # add enumerate to produce a list and their index
            for index, item in enumerate(todo):
                # this creates two variables that can be printed and removes newlines
                row = f"{index+1} - {item.strip('\n')}"
                print(row)

        case "edit":
            # get the index item from the user
            edit_item = int(input("Number of item to edit? "))

            # adjust for 0 index
            adj_index = edit_item - 1

            # open the file
            with open("app01_todo\list.txt", "r") as file:
                todo = file.readlines()

            # create a revised version of the to-do
            new_todo = input("Enter a new To Do: ")

            # update the value based on the index value
            todo[adj_index] = new_todo + "\n"

            # write edits to the file
            with open("app01_todo\list.txt", "w") as file:
                file.writelines(todo)

        case "complete":
            # open the file
            with open("app01_todo\list.txt", "r") as file:
                todo = file.readlines()

            # pop removes using the index value
            complete_val = int(input("Number To Do to complete: "))

            # pop returns the item that was removed from the list
            removed_val = todo.pop(complete_val - 1)
            print(f"{removed_val} has been removed")

            # write edits to the file
            with open("app01_todo\list.txt", "w") as file:
                file.writelines(todo)

        case "quit":
            break
        case _:
            pass
