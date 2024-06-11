# r = Read
# a = append
# w = Write
# x = Create

# Read - error if does not exists

# this will open and read the file
file = open("names.txt", "r")

# use the read() method on the file
# print(file.read())

# to read only the first four characters
# print(file.read(4))

# to read the entire line but don't know the lenght
# print(file.readline())
# will read the second line
# print(file.readline())

# loop through the file
for line in file:
    # loops through but adds a new blank line on each loop on default
    print(line)

# close the file when done.
file.close()


# to avoid an error, use a try block
try:
    file = open("names.txt")
    print(file.read())
except:
    print("File does not exist. ")
finally:
    # use finally and .close() to ensure the file is closed in case there are no exceptions found
    file.close()

# append to the file, this will create the file regardless.
f = open("names.txt", "a")
f.write("\nStan")
f.close()

f = open("names.txt")
print(f.read())
f.close()

# to open for writing, this will overwrite whatever is there
f = open("context.txt", "w")
f.write("File deleted")
f.close

f = open("context.txt")
print(f.read())
f.close()


# create a new file for writing, will also create the file
# f = open("name_list.txt", "w")
# f.close()

# can create a file but might return an error if already exists
# f.open("name_list.txt", "w")

# to work around this, import os
import os

if not os.path.exists("name_lists.txt"):
    # x to create the file
    f = open("file_list.txt", "x")
    f.close()
else:
    print("File exists")


# to delete a file and avoid errors
if os.path.exists("name_lists.txt"):
    os.remove("name_list.txt")
else:
    print("File not found")
