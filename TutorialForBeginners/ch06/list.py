users =['Bob', 'Sam', 'Josh']

data = ['Dave', 42, True]

empty_list = []

# one way to check if something is in a list
print('Dave' in users) #False
print('Sam' in users)  #True

# access an element in the list
print(data[1]) # 42

# using a method on the list
# index(Value) returns the location in the list
print(users.index('Bob'))

# item 1 and 2 not 3
print(users[0:2])
# all items in the list range
print(users[0:])

# return the length of the list
print(len(data))

# to add users to a list use append
users.append("Liv")
print(users)

# adding a list to a list
users += ['Isaac']
print(users)

# or use the exten
users.extend(['Christian', 'Kelly'])
print(users)

# can also use extend and pass in a different list
# users.extend(data)
# print(users)

# to add in at a spot in an existing list
users.insert(0,'Dan')
print(users)

# using brackets to insert at spot
users[2:2] = ['Ben','Cory']
print(users)

# replacing users in a range. Also known as slice.
users[1:3] = ['Jan', 'Cole']
print(users)

# removing users
users.remove('Jan')
print(users)

# pop off the last users and returns the value
print(users.pop())
print(users)

# deleting using index
# del users[2]
del users[users.index('Liv')] # combining items
print(users)

# to empty a list
data.clear()
print(data)

users[1:1] = ['dave']

# lowercase comes after Uppercase
# pass in sort parameter to include lower on str
users.sort(key=str.lower)
print(users)

nums = [1,2,43,553,12,4,211,13]
# flips the entire list order, does not sort
nums.reverse()
print(nums)

# sort in descending order
# nums.sort(reverse=True)
# print(nums)

# These sort optipns modify the order of the list!!!

# will sort globally without impacting the order
print(sorted(nums, reverse=True))
# still shows original order
print(nums)

# copy lists
num_copy = nums.copy()
num_copy2 = list(nums)
num_copy3 = nums[:]

print(num_copy)
print(num_copy2)
num_copy3.sort()
print(num_copy3)
print(nums)

# Tuples
# like lists but the data will not change order

# creating with constructor
my_tuple = tuple(('Bob','Sam', 'Josh'))
# without a constructor
other_tuple = ('Bill', 'Peet', 'Dave')

print(my_tuple)
print(type(my_tuple))

# create a list from a tuple 
newlist = list(my_tuple)
# update the list
newlist.append('Neil')
# make a new tuple from appended list
new_tuple = tuple(newlist)
print(new_tuple)

# unpacking a tuple into variables
# use of * will gather remaining variables into a list
(one,two,*three) = new_tuple

print(one)
print(two)
print(three)