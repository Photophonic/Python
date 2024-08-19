# if statements will check if evaluates to T/F
lang = "Python"

if lang == "Python":
    print(f"{lang} is True")
else:
    print("False")

# Object Identity: is statement
lang = "C#"

if lang == "Python":
    print(f"Lang is {lang}")
elif lang == "Java":
    print(f"Lang is {lang}")
else:
    print(f"{lang} not found")

# Python does not have a switch case, instead uses elif
lang = "JS"

if lang == "Python":
    print(f"Lang is {lang}")
elif lang == "Java":
    print(f"Lang is {lang}")
elif lang == "JS":
    print(f"Lang is {lang}")
else:
    print(f"{lang} not found")

# Boolean and or not
user = "Test"
logged_in = True

if not logged_in:
    print("Please log in")
elif user == "Admin" and logged_in == True:
    print("Admin Page")
elif user == "User" or logged_in == True:
    print("Landing Page")
else:
    print("Bummer")


a = ["a", "b", "c"]
b = ["a", "b", "c"]

# prints true
print(a == b)
# prints false
print(a is b)

b = a
# prints true
print(a is b)
