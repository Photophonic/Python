# Custom functions version


# def name(arguments):
# set a default argument for the file path
def get_todos(filepath="app01_todo/list.txt"):
    # do something here
    with open(filepath, "r") as file:
        todos = file.readlines()
    # return value to the calling code
    return todos


# this function uses two parameters, path and the list
# default arguments must come after non defaulted values.
def write_todos(list, filepath="app01_todo/list.txt"):
    # write edits to the file
    with open(filepath, "w") as file:
        file.writelines(list)
    # does not need to retunr anytbing since it updates a file.


while True:
    user_action = input("Type add, show, edit, complete, or quit: \n").strip()

    # if "add" in user_action[:3]:
    # alternate option to validate input
    if user_action.startswith("add"):
        # revised read file using WITH context manager

        # get action from the user input and strip out add_
        # list slicing to extract everything at & acter p4
        action = user_action[4:] + "\n"

        # replace the line above with function call and stored value
        # update parameter in to use the default argument value
        todo = get_todos()

        # add to the list the capitalize user_input and breakline
        todo.append(action.title())

        # revised write using WITH
        # with open("app01_todo/list.txt", "w") as file:
        #     file.writelines(todo)

        # replace the code above with this new function.
        # provide the file path and the appended list

        # update parameter to pass in the list. Path is defaulted
        write_todos(todo)

    elif user_action.startswith("show"):
        # revised read file using WITH context manager
        todo = get_todos()

        # add enumerate to produce a list and their index
        for index, item in enumerate(todo):
            # this creates two variables that can be printed and removes newlines
            row = f"{index+1} - {item.strip('\n')}"
            print(row)

    elif user_action.startswith("edit"):
        try:
            # get the index item from the user
            edit_item = int(user_action[5:])

            # adjust for 0 index
            adj_index = edit_item - 1

            # open the file
            todo = get_todos()

            # create a revised version of the to-do
            new_todo = input("Enter a new To Do: ")

            # update the value based on the index value
            todo[adj_index] = new_todo + "\n"

            # write edits to the file
            write_todos(todo)

        # must provide the type of error to look for.
        except ValueError:
            print("Enter a valid edit option")
            # continue will skip any remaining code at this point and go back to the top for the next itteration of the loop.
            continue
            """this will never execute, same with the remianing elif lines below."""
            print("Code after the continue")

    elif user_action.startswith("complete"):
        try:
            # open the file
            todo = get_todos()

            # pop removes using the index value
            complete_val = int(user_action[8:])

            # pop returns the item that was removed from the list
            removed_val = todo.pop(complete_val - 1)
            print(f"{removed_val} has been removed")

            # write edits to the file
            write_todos(todo)

        except IndexError:
            print("Enter a valid item in range")
            continue

    elif user_action.startswith("quit"):
        break
    else:
        print("Please enter a valid option")
        pass
