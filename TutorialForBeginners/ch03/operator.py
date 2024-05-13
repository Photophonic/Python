# assignment =
name = "Bob Dole"

# +, -, /, *
num = 2 * 2

numFloat = 2 / 2

# use floor devision to round down
numFloor = 2 // 2

# round
numRound = round(24 / 5)

# remainder/modulo
numRemian = 24 % 5

# power of
numPow = 2**3

print(numPow)

# comparison

# returns false
42 == 41
42 < 41

# returns true
43 != 41
42 > 41

# not, and also keywords for boolean logic
meaning = 42

print("")

if meaning < 10:
    print("Right on!")
else:
    print("Bummer :(")

# ternary operator, syntax is rather different from JS
print("Right on!") if meaning > 10 else ("Bummer :(")
