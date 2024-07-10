# create an object in memory to hold the file
my_file = open("fruits.txt")


# call the read() method to view the contents of the var.
print(my_file.read())
my_file.close()


bear_file = open("bear.txt")

print(bear_file.read(), "\n")

bear_file.close()
# read() method places the cursor at the end of the list. So if an attempt to read() again, it will just return a blank line.

# to work around this, save the read to a variable then print it.

# use relative path to the file if not in the same folder
#  /files/bear.txt
bear_file = open("bear.txt")
file_content = bear_file.read()
bear_file.close()

print(file_content, "\n")
print(file_content, "\n")

# close is used to close a file you have read to remove it from memory.

# better way to do this is to use with context manager
with open("fruits.txt") as my_file:
    content = my_file.read()
    # will open, read, and close the file

print(content)

# to open and write to a file.
# Using write method, Python will overwrite the file
veggies = ["Carrot", "Potato", "Corn", "Kale"]

with open("vegetables.txt", "w") as my_file:
    for veggie in veggies:
        my_file.write(veggie)
        my_file.write("\n")

with open("vegetables.txt") as my_file:
    content = my_file.read()

print(content)


with open("bear.txt") as my_file:
    content = my_file.read()

print(content[:90])


def count_item(letter, file_name):
    with open(file_name) as my_file:
        content = my_file.read()

    return content.count(letter)


get_count = count_item("z", "bear.txt")
print(get_count)


with open("file.txt", "w") as my_file:
    my_file.write("snail")


with open("bear.txt", "r") as my_file:
    content = my_file.read()

slice_content = content[:90]

with open("first.txt", "w") as my_file:
    my_file.write(slice_content)


with open("fruits.txt", "a") as my_file:
    my_file.write("\nToast")
    my_file.write("\nWaffle")

# to append and then read the file in one command
with open("fruits.txt", "a+") as my_file:
    my_file.write("\nSpam")
    my_file.write("\nCheese")
    # this will move the cursor back to the start
    my_file.seek(0)
    content = my_file.read()


print(content)


with open("bear.txt", "r") as my_file:
    bear_content = my_file.read()

with open("bear2.txt", "a") as my_file:
    my_file.write(bear_content)


with open("data.txt", "a+") as my_file:
    my_file.seek(0)
    content = my_file.read()
    my_file.seek(0)
    my_file.write(content)
    my_file.write(content)


# with open("data.txt", "a+") as my_file:
#     for x in range(2):
#         my_file.write(content)
