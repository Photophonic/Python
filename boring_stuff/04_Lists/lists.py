# Lists
myList = ['cat', 'bat', 'rat', 'mat']
print(myList)
print(myList[2])

superList = [['cat', 'bat', 'rat'], [10, 20, 30, 40]]
# will print first list then bat
print(superList[0][1])
# will print from second group, 40
print(superList[1][3])
# will print the last thing in the list, -X works backwards
print(myList[-1])
# will print the whole list
print(myList[:])

# to get the length of a list
print(len(myList))

# to change a value with the index
print(myList)
myList[3] = 'hat'
print(myList)

# join lists
myList = myList + superList

print(myList)

# tp delete from lists
# deletes rat
del myList[2]

myList
print(myList)

print('***********')
# using a loop with range
for i in range(len(myList)):
    print(myList[i])


# multiple assignments and unpacking
cat = ['small', 'grayish', 'murps']
# Pythong will assign the values in the list to the order they are seen.
size, color, disposition = cat
# will print small
print(size)

# to return the k/v pair in a list use enumerate()
# can be used in place of len(listName)
movies = ['Deathproof', 'Scott Pilgrim', 'Hateful Eight', 'Fury Road']

# idex will contain the list index, item is the value
for index, items in enumerate(movies):
    # convert index to a string
    print('Index ' + str(index) + ' movie: ' + items)
