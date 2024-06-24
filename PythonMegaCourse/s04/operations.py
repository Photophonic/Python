# List data type
# dir(list) to view operations on list data type
monday_temps = [91.1, 88.8, 75.2]

monday_temps.append(72.4)

monday_temps.remove(88.8)

print(monday_temps)

monday_temps.clear()

print(monday_temps)

monday_temps = [91.1, 88.8, 75.2]

# provides the index location for the matching item
mt_index = monday_temps.index(75.2)
print(mt_index)

monday_temps = [91.1, 88.8, 75.2, 88.8]
# can define a start location in the list
mt_index = monday_temps.index(88.8, 2)
# returns 3 for the index location
print(mt_index)


seconds = [1.23, 1.45, 1.02]
current = 1.11

seconds.append(current)
seconds.remove(1.45)
print(seconds)

# create list of items to remove.
seconds_to_remove = [1.45, 1.02, 1.11]

# loop over removal list
for second in seconds_to_remove:
    # if the iterator is in the original list then remove it
    if (second) in seconds:
        seconds.remove(second)

print(seconds)

# to get an item with the index, returns 88.8
print(monday_temps[1])


serials = ["1234HHHH", "8237BBB", "0987ABC", "ZXCVVB763", "888JHGFD", "QWERT12345"]
print(serials[0], serials[2], serials[5])


workdays = ["Mon", "Tues", "Wed", "Thur", "Fri"]
weekend = ["Sat", "Sun"]
# append only the first item from weekend to the workday list
workdays.append(weekend[0])
print(workdays)


# slicing
print(len(workdays))

# create a new list with a section with a start and stop range
new_workdays = workdays[1:4]
# Tues, Wed, Thur
print(new_workdays)


# last item
last_item = workdays[-1]
print(last_item)

# string slicing
my_string = "this is a test string"
print(my_string[10:])

letters = ["a", "b", "c", "d", "e", "f", "g"]

print(letters[1:4])
print(letters[:3])
print(letters[-3:])

# to get the items from a dictionary
student_grades = {"Sam": 88, "Bob": 75, "Pete": 90}
# wikll return 75
print(student_grades["Bob"])


abc = "abcdef"
print(abc[:3])
print(abc[2:4])
print(abc[-2:])

print(letters[-2][-2])

data = {"a": [123], "b": [456], "c": [789]}
print(data["b"][2])
