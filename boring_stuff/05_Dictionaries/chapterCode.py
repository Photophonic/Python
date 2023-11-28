# like a list, dictionaries are mutable data structures
# can use many different data types for key/value pairs
# uses {dictionary} instead of [list]
# similar to objects in JS
myCat = {'size': 'fat', 'color': 'black', 'disposition': 'fussy'}

print(myCat['size'])

# dictionaries are unordered unlike lists
spam = ['cats', 'dogs', 'moose']
bacon = ['dogs', 'moose', 'cats']

print(spam == bacon)
# returns false because the order does not match

eggs = {'name': 'beryl', 'size': 'small', 'color': 'brownish'}
ham = {'size': 'small', 'color': 'brownish', 'name': 'beryl'}

print(eggs == ham)
# returns true because order does not matter, just content

x = slice(0, 1)
print(bacon[x])

# key(), values(), items() methods
spam = {'color': 'red', 'age': 42, 'hobby': 'reading'}
# loop over the dictionary and return the values
print('\nkeys:')
for v in spam.keys():
    print(v, end=", ")
print('\nvalues:')
for v in spam.values():
    # prit output on a single line
    print(v, end=", ")
print('\nitems:')
for v in spam.items():
    # returns a touple data type, immutable
    print(v, end=", ")


# can use multiple assigments for lists
for k, v in spam.items():
    # need to use str() to convert the number from the value
    print('Key: ' + k + ' Value: ' + str(v))

# to check if exists
print('name' in spam.keys())
# returns false since name is not in the dictionary spam

print('color' in spam)
# returns true, written in a shorten form

# using get() to determin if item is in the k/v
picnicItems = {'apples': 5, 'cups': 2}
# .get() will search the dictionary for the matching Key
# and return the value if found. If not, it defaults to a value
print('I am bringing '+str(picnicItems.get('cups', 0)) + ' cups')
# without the get.() plates would cause the code to error
print('I am bringing '+str(picnicItems.get('plates', 0)) + ' plates')


# Set default can be used to simplify values not in dictionaries
myItems = {'name': 'Beryl', 'age': 10}
myItems.setdefault('color', 'Brownish')
# prints myItems along with the default for color
for k, v in myItems.items():
    # need to use str() to convert the number from the value
    print('Key: ' + k.title() + ', Value: ' + str(v))

# if setdefault is ran again with a different value,
# it would not change since the K/V now exists
myItems.setdefault('color', 'Greyish')
# can use multiple assigments for lists
for k, v in myItems.items():
    # need to use str() to convert the number from the value
    print('Key: ' + k.title() + ', Value: ' + str(v))
