import os

# print(dir(os))

# get the current location
print(os.getcwd())

# change the current directory
# os.chdir("C:\Git\Repo\Python\CS_YT\modules")
# print(os.getcwd())

# move back
# os.chdir("C:\Git\Repo\Python\CS_YT")
# print(os.getcwd())

# see items in the current dir
print(os.listdir())

# create a new directory
# os.mkdir will create the directory
# os.makedirs will create nested dir
# os.mkdir("test")
# os.makedirs("tests/nested")

# to remove
# os.rmdir("test")
# os.removedirs("tests/nested")

# to rename
# os.rename("test.txt", "new.txt")

# view stats on the item
print(os.stat("new.txt"))


# to get the last modification date and in a readable format?"vdsxC"
from datetime import datetime

# get the last modified time (st_mtime)
f_date = os.stat("new.txt").st_mtime
print(datetime.fromtimestamp(f_date))
# 2024-08-13 16:29:05.062324

# get the file path information in the form of a tuple
for dirpath, dirnames, filenames in os.walk("C:\Git\Repo\Python\CS_YT"):
    print(dirpath, dirnames, filenames)
