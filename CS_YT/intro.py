# message = input("Enter something here: \n")
message = "Here is a comment"

print(len(message))
# Will print the character at this index
print(message[0])
# Prints from first upto but not including the 4th index location
print(message[0:4])
# returns is
print(message[5:7])

# a method is a function that belongs to an object
print(message.lower())
print(message.upper())

# Will return the number of occurences of the passed in argument
print(message.count("e"))


# To find the index location
print(message.find("s"))


# to replace
new_message = message.replace("Here", "This")
print(new_message)
print(message)

greetig = "hey"
name = "Bob"
message = greetig + ", " + name
print(message)

print(f"{greetig.title()}, {name}!")
