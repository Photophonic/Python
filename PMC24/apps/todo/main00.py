# empyt to-do list
# remove list as it will be used in the add
# todo = []
# initialize varaible for input
user_action = ""

while True:
    user_action = input("Type add, show, edit, complete, or quit: \n").strip()

    # python case statement to compare user_action input
    match user_action.strip():
        case "add":
            user_val = input("Enter a To Do: ") + "\n"
            # open and read items in the list
            file = open("app01_todo\list.txt", "r")
            # read the contents and make a new list
            todo = file.readlines()
            # remember to close the file
            file.close()
            # add to the list the capitalize user_input
            todo.append(user_val.title())
            # open file and write to it,
            file = open("app01_todo\list.txt", "w")
            # witelines is a method to write from a list
            file.writelines(todo)
            file.close()
        case "show":
            file = open("app01_todo\list.txt", "r")
            # read the contents and make a new list
            todo = file.readlines()
            # remember to close the file
            file.close()

            # new_todo = []

            # for item in todo:
            #     new_item = item.strip("\n")
            #     new_todo.append(new_item)

            # using list comprehension in place of the for-loop and list var
            # new_todo = [item.strip("\n") for item in todo]
            # for index, item in enumerate(new_todo):

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
            # create a revised version of the to-do
            new_todo = input("Enter a new To Do: ")
            # update the value based on the index value
            todo[adj_index] = new_todo
        case "complete":
            # pop removes using the index value
            complete_val = int(input("Number To Do to complete: "))
            # pop returns the item that was removed from the list
            removed_val = todo.pop(complete_val - 1)
            print(f"{removed_val} has been removed")

        case "quit":
            break
        case _:
            pass
