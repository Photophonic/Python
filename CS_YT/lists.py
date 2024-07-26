# lists - sequential data
# sets - unordered values without duplicates

# lists
courses = ["History", "Math", "Science", "CompSci"]
print(len(courses))
print(courses)
# print the value at the index
print(courses[1])
# will always return the last index item
print(courses[-1])
# range from up to
print(courses[1:3])
# print from a point to the end
print(courses[2:])
# add items to the list
courses.append("Art")
print(courses)
# insert at a specific index location
courses.insert(1, "Geography")
print(courses)
# extend will add multiple values to the end
courses2 = ["Business", "Education"]
# this will add the values to the original list
courses.extend(courses2)
print(courses)
# to remove a value
courses.remove("Math")
print(courses)
# Pop will remove the last item and save it
popped = courses.pop()
print(courses)
print(popped)
# reverse a list
courses.reverse()
print(courses)
# alpha order
courses.sort()
print(courses)
