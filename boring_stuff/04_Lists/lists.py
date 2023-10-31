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

# adding elements to a list
