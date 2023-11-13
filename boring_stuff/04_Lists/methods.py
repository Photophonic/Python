# Methods are the same thing as functions but are called on a variable
# the method comes after the variable, list.index()

movies = ['Death Proof', 'Scott Pilgrim',
          'Fury Road', 'Vanshing Point', 'Predator']

# this will return the place of Fury Road in the list - 2
print(movies.index('Fury Road'))


# some list methods. Only work on lists

# Add a movie to the end of the list
movies.append('Hateful Eight')

print(movies)

# remove an item from the list
movies.remove('Predator')

print(movies)

# to add an item to the list at a certain index
# insert(index_Num, item_name)
movies.insert(1, 'Deer Hunter')

print(movies)

# sorting lists
movies.sort()
print(movies)

# arguement to reverse the sort on the list
movies.sort(reverse=True)
print(movies)

# usung sort() is permanent
print(movies)

# reverse the list instead of using the argument
movies.reverse()
print(movies)
