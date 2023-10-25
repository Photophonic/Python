from pathlib import Path
import json

path = Path('Python/ch10/username.json')

# refactor to a function
# check if the file is found using .exists()
# if path.exists():
#     contents = path.read_text()
#     username = json.loads(contents)
#     print(f'Welcome back {username}')
# else:
#     username = input('Enter your username: \n')
#     contents = json.dumps(username)
#     path.write_text(contents)
#     print(f"We'll remember the next time {username}")


def get_username(path):
    # check if the file is found from the path
    if path.exists():
        # if found read the contents into a variable
        contents = path.read_text()
        username = json.loads(contents)
        #  return the python converted username
        return username
    else:
        # else do nothing
        None


def create_username(path):
    # function specific to capturing the username
    username = input('Enter your username: \n')
    contents = json.dumps(username)
    path.write_text(contents)
    return username

# create main function


def greet_user():
    # check if the username exists using new function ^
    username = get_username(path)
    # if true then print welcome message
    if username:
        print(f'Welcome back {username}')
    else:
        # else gather user info and store it to the file
        create_username(path)
        print(f"We'll remember the next time {username}")


# call the function
greet_user()
