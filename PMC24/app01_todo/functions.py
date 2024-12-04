# standard practice to break up logical application behavior
# define constants here and are in uppercase
FILEPATH = "app01_todo/list.txt"


# def name(arguments): and set default path to the constant above
def get_todos(filepath=FILEPATH):
    # do something here
    with open(filepath, "r") as file:
        todos = file.readlines()
    # return value to the calling code
    return todos


# this function uses two parameters, path and the list
def write_todos(list, filepath=FILEPATH):
    # write edits to the file
    with open(filepath, "w") as file:
        file.writelines(list)
    # does not need to return anytbing since it updates a file.


# these will only run if THIS file is run directly
if __name__ == "__main__":
    print("hello")
    print(get_todos())
