
# Immutable items like a string. Uses () instead pf []
import copy
items = ('Test', 82, 'Value', 99, 22)
print(items[1])
print(items[1:4])
# attempt to reassign the value at index 1
# this will result in an error
try:
    items[1] = 93
except:
    print("Touples are immutable itmes")


# References point to a memory space
myList = [0, 1, 2, 3, 4]


newList = myList

newList[1] = 99

# This change to newList will impact both since they are pointing to the same memory space
for i in myList:
    print(i)

for i in newList:
    print(i)

# Passing references


print('**************')


def myRef(valueIn):
    valueIn.append('Test')


# to avoid unwanted updates to a ref item, create a copy

newList = copy.copy(myList)

myRef(newList)

for i in myList:
    print(i)
# new list will be a copy of myList and the update from myRef will not impact myList
for i in newList:
    print(i)
