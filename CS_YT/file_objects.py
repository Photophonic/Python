# File Objects

# open the file for read r, write w, or append a
f = open("test.txt", "r")
# print the name
print(f.name)
# close the file when complete
f.close()

# It's better to open the file with a context manager
with open("test.txt", "r") as f:
    # this will run the code and auto close it afterward
    print(f.name)
# will show this file is closed
print(f.closed)


with open("test.txt", "r") as f:
    # this will read the contents of the file
    # f_contents = f.read()
    # print(f_contents)

    # this will return all the contents and characters
    # f_read_lines = f.readlines()
    # print(f_read_lines)

    # this will read each line one at a time
    # f_read_line = f.readline()
    # print(f_read_line)

    # this approach will read each line of the file without loading the whole thing into memory
    # for line in f:
    #     print(line, end="")

    # to define the size we want read, pass in the character size
    # f_read = f.read(5)
    # print(f_read, end="")
    size_to_read = 10

    f_read = f.read(size_to_read)
    print(f_read, end="*")

    # while len(f_read) > 0:
    #     print(f_read, end="*")
    #     # this will increment the read location
    #     f_read = f.read(size_to_read)

    # using seek to change location of the read
    f.seek(0)
    print(f_read, end="")


# Writing to a file, w will create and overwrite existing contents.
# Append will add to existing contents
with open("test2.txt", "w") as f:
    f.write("Test")
    f.seek(0)
    f.write("Test32")
