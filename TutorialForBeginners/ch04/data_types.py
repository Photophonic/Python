# string datatype

# literal assignments
first = "Bob"
last = "Dole"

# returns str
print(type(first))
# boolean check
print(type(first) == str)
# is an instance of
print(isinstance(first, str))

print("")

# constructor function
pizza = str("Pepperoni")
print(pizza)
print(type(pizza))
print(type(pizza) == str)
print(isinstance(pizza, str))

# concatination
fullname = first + " " + last
print(fullname)


# casting number to a string
decade = str(1980)
print(type(decade))
# to concat this to a sentence, the num would need to be
# cast as a string
print(decade)

statement = "I like music from the " + decade + "'s."
print(statement)


# multiline statement, use three "" together. T
# This will preserve the white space between lines
multiline = """
Hey, how are you?   

I was just doing stuff   

        Niiiiice.
"""

# print(multiline)

# escaping special characters, use
# \t - tab, \n - new line, \' or ""
sentence = "I'm back at work!\tHey!\n\nWhere's the beef?"

print(sentence)

# String Methods, functions called on the string class
print(first)
print(first.lower())
# shift command D to copy line down (MAC)
print(first.upper())

# will capitalize first letter
print(multiline.title())
# replaced syntax
print(multiline.replace("stuff", "things"))

# to get the lenght of a string, pass a string into len(xyz)
# this will count whitespace
print(len(multiline))

# remove whitespace
print(len(multiline.strip()))
# can also use lstrip() or rstrip()

print("")

# build a menu as an example
title = "menu".upper()

print(title.center(20, "="))
print("Coffee".ljust(16, ".") + "$1".rjust(4))
print("Muffin".ljust(16, ".") + "$2".rjust(4))
print("Roll".ljust(16, ".") + "$4".rjust(4))


# String index values
# will return the specific letter of the string
print(first[1])
# last letter
print(first[-1])
# range of,
print(first[1:-1])
