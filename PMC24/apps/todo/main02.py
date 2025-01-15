# Optimized version
user_action = ""

while True:
    user_action = input("Type add, show, edit, complete, or quit: \n").strip()

    # remove match/case statement & replace with if/els
    # This will allow the app to use IN expression for evaluation
    if "add" in user_action:
        # revised read file using WITH context manager
        # can use r to force path as a raw string

        # get action from the user input and strip out add_
        # list slicing to extract everything at & acter p4
        action = user_action[4:] + "\n"

        with open("app01_todo/list.txt", "r") as file:
            todo = file.readlines()

        # add to the list the capitalize user_input
        todo.append(action.title())

        # revised write using WITH
        with open("app01_todo/list.txt", "w") as file:
            file.writelines(todo)

    elif "show" in user_action:
        # revised read file using WITH context manager
        with open("app01_todo/list.txt", "r") as file:
            todo = file.readlines()

        # add enumerate to produce a list and their index
        for index, item in enumerate(todo):
            # this creates two variables that can be printed and removes newlines
            row = f"{index+1} - {item.strip('\n')}"
            print(row)

    elif "edit" in user_action:
        # get the index item from the user
        edit_item = int(user_action[5:])

        # adjust for 0 index
        adj_index = edit_item - 1

        # open the file
        with open("app01_todo/list.txt", "r") as file:
            todo = file.readlines()

        # create a revised version of the to-do
        new_todo = input("Enter a new To Do: ")

        # update the value based on the index value
        todo[adj_index] = new_todo + "\n"

        # write edits to the file
        with open("app01_todo/list.txt", "w") as file:
            file.writelines(todo)

    elif "complete" in user_action:
        # open the file
        with open("app01_todo/list.txt", "r") as file:
            todo = file.readlines()

        # pop removes using the index value
        complete_val = int(user_action[8:])

        # pop returns the item that was removed from the list
        removed_val = todo.pop(complete_val - 1)
        print(f"{removed_val} has been removed")

        # write edits to the file
        with open("app01_todo/list.txt", "w") as file:
            file.writelines(todo)

    elif "quit" in user_action:
        break
    else:
        print("Please enter a valid option")
        pass
