

spam = [2, 4, 6, 8, 10]

spam[2] = 'Hello'

print(spam[2])

spams = ['a', 'b', 'c', 'd']

print(spams[int(int('3'*2)//11)])

print(int('3'*2))

print(spams[:2])


bacon = [3.14, 'cat', 11, 'cat', True]

print(bacon.index('cat'))
bacon.remove('cat')
bacon.append(99)
print(bacon)


concatList = spam + spams

print('New list ', concatList)

concatList = spam * 2

print(concatList)

# good for removing by index
del concatList[2]
print(concatList)

# good for removing a known value
concatList.remove(2)
print(concatList)


tup = (42)

print(tup)

# convert touple to a list
convList = ((tup))

print(convList)


# copy.copy() copies a list
#  copy.deepcopy() copies a list's lists
