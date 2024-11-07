# standard practice to break up logical application behavior


# def name(arguments):
def get_todos(filepath="app01_todo/list.txt"):
    # do something here
    with open(filepath, "r") as file:
        todos = file.readlines()
    # return value to the calling code
    return todos


# this function uses two parameters, path and the list
def write_todos(list, filepath="app01_todo/list.txt"):
    # write edits to the file
    with open(filepath, "w") as file:
        file.writelines(list)
    # does not need to return anytbing since it updates a file.
