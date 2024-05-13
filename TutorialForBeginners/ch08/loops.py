# while loop runs until false
print("While")
value = 1
while value <= 10:
    print(value)
    value +=1

print("\nBreak")
value = 1
while value <= 10:
    print(value)
    if value == 5:
        break # will exit the loop when value is 5
    value += 1

print("\nContinue")
value = 0
while value < 10:   
    # make sure to increment before contine statement
    value += 1
    if value == 5:
        continue # will stop the loop at 5 then keep going
    print(value)
else:
    print("Complete " + str(value))   

# For loops
print("\nFor Loops")
# lists are an iterable item
names = ['Bob',"Sam", "Dan"]
for name in names:
    print(name)

# STR are also iterable items
# for letter in "Mississippi":
#     print(letter)

print("\nfor break")
for name in names:
    if name == 'Sam':
        break
    print(name)

print("\nfor continue")
for name in names:
    # will skip over sam
    if name == "Sam":
        continue
    print(name)

print("\nRanges")
# ranges in for loop
for name in range(4):
    print(name)

print("")
# can privide positional notation for the range
for x in range (2,4):
    print(x)

# can also state steps
for x in range(0,100, 10):
    print(x)
else:
    print("That's done!")

# lists and loops again
print("Nested loops")
names = ['Bob',"Sam", "Dan", 'Liv', 'Jess', "Mike"]
actions = ['coding', "eats", "sleeps"]

for name in names:
    for action in actions:
        print(name, action)
print("Done\n")