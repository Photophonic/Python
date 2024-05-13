person = "Bob"

coins = 3

# print("\n" + person + " has " + str(coins) + " coins left.")

# old way of doing this, must be in order for substitution
message = "\n%s has %s coins left" %(person, coins)
print(message)

# uaing only format
message = "\n{} has {} coins left.".format(person, coins)
print(message)

# using format with index location
message = "\n{1} has {0} coins left.".format(coins, person)
print(message)

# format with value assignment
message = "\n{person} has {coins} coins left.".format(coins = coins, person = person)
print(message)

# using a dictionary
player = {'person': "Bob", "coins":3}
# use format(**DictName) to pull the values into the string
message = "\n{person} has {coins} coins left.".format(**player)
print(message)

# f is the newer approach and recommended usage
message = (f"\n{person} has {coins} coins left.")
print(message)

num = 10 
# :.2f will format to a fixed 2 decimal places
print(f"\n2.25 times {num} is {2.25 * num:.2f}\n")

for num in range(1, 11):
    print(f"\n2.25 times {num} is {2.25 * num:.2f}\n")

for num in range(1, 11):
    # used of :2% will show a two decimal place with % on end
    print(f"\n{num} divided by 2.25 is {2.25 / num:.2%}\n")
