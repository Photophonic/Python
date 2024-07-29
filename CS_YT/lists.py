# lists - sequential data
# sets - unordered values without duplicates

# lists, uses []
courses = ["History", "Math", "Science", "CompSci"]
num = [1, 54, 97, 8, 32, 2]
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
# numbers sort in ascending
num.sort()
print(num)
# To flip the sort around with sort
courses.sort(reverse=True)
print(courses)
num.sort(reverse=True)
print(num)

# to get a sorted version without altering the original list
courses = ["History", "Math", "Science", "CompSci"]
num = [1, 54, 97, 8, 32, 2]

print(sorted(courses), courses)
print(sorted(num), num)

# To find the index in a list
print(courses.index("Science"))
# Returns T/F to see if item is in the passed argument
print("Art" in courses)

# To print out each item on a new line
for item in courses:
    print(item)

# enumerate returns the index and value, can adjust the index nubmer
for index, course in enumerate(courses, start=1):
    print(index, course)


# can convert a list into a str value
courses = ["History", "Math", "Science", "CompSci"]
# set a new variable and use the .join method after the new string
course_str = ", ".join(courses)
# will print History, Math, Science, CompSci
print(course_str)

# can split a string into separate values
course_split = course_str.split(", ")
for index, course in enumerate(course_split, start=1):
    print(index, course)


# Tuples, similar to strings but cannot be modified. Uses ()
# example issue of lists
list_1 = ["History", "Math", "Science", "CompSci"]
list_2 = list_1

list_1.append("Art")
print(list_1)
print(list_2)

# Tuple example
tuple_1 = ("History", "Math", "Science", "CompSci")
tuple_2 = tuple_1

# Will throw an error as you cannot change a tuple's values
# tuple_1[0] = "Art"
print(tuple_1)
print(tuple_2)


# Sets are unordered and have no duplicates. Uses {}
cs_course = {"History", "Art", "Math", "CompSci"}
print(cs_course)
cs_course.add("Econ")
print(cs_course)
cs_course.add("Art")
# will not list Art a second time as it would be a duplicate
print(cs_course)


# Sets can quickly comapre to other sets
cs_course = {"History", "Math", "CompSci", "Physics"}
art_courses = {"History", "Art", "Design", "Math"}
# To see what they share, use intersect, will print {'History', 'Math'}
print(cs_course.intersection(art_courses))
# will print the difference {'CompSci', 'Physics'}
print(cs_course.difference(art_courses))
# to merge use Union
print(cs_course.union(art_courses))


# to create empty versions
empty_list = []
empty_list = list()

empty_tuple = ()
empty_tuple = tuple()

empty_set = set()
# using {} will create an empty dictionary
