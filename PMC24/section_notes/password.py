password = input("Enter a password: ")

# use list to store multiple things
results = []

if len(password) >= 8:
    results.append(True)
else:
    results.append(False)

# Use isdigit() method on the string to check for numbers
# note, isdigit() cannot be used on a whole string.
digit = False

# use a loop to verify the individual character to check if digit
for i in password:
    if i.isdigit():
        digit = True

results.append(digit)

capital = False
for i in password:
    if i.isupper():
        capital = True

results.append(digit)

print(results)


# can also use if all(results): ~
if False in results:
    print("Please enter a valid password.")
else:
    print("Password updated.")


# Using dictionaries in this scenario to get key/value pairs for True/False
password = input("Enter a password: ")

# use dictionary to store multiple different things
results = {}

if len(password) >= 8:
    results["Length"] = True
else:
    results["Length"] = False

# Use isdigit() method on the string to check for numbers
# note, isdigit() cannot be used on a whole string.
digit = False

# use a loop to verify the individual character to check if digit
for i in password:
    if i.isdigit():
        digit = True

results["Digit"] = digit

capital = False
for i in password:
    if i.isupper():
        capital = True

results["Capital"] = capital

print(results)


# can also use if all(results): ~
if False in results:
    print("Please enter a valid password.")
else:
    print("Password updated.")
