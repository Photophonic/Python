spent = 3
donated = 4

total_amount = spent + donated
print(total_amount)


items = 2
price = 10

total_price = items * price

print(f"Total price is ${total_price:.2f}")


x = 10
y = "10"

sum1 = x + x
sum2 = y + y

print(sum1)
print(sum2)


mood = "here"
strength = 10.3
rank = 10

print(mood, strength, rank)


x = 1
y = 2
z = 3

s = x + y + z
print(s)


# list
student_grades = [100, 90, 80, 85, 75, 95]
print(student_grades[1])

# mixed list
mixed_list = [9, "Hello", [1, 2, 3, 4]]
print(mixed_list)

# this will just print the list twice
print(mixed_list * 2)

# auto gen a list in a range, convert a range into a list.
list_range = list(range(0, 11))
print(list_range)

temperatures = [98.0, 90, 75.2, 88, 72.4]
print(temperatures)

rainfall = [55.5, 70, "String here", ["another list", 55.3, 90]]

# to print an item from the nested list
print(rainfall[3][0])


# use dir() function to see everything you can do with a fucntion
# print(dir(float))

# to find the average of a list of nubmers


# create a function named Average and pass in a list
def Average(list):
    # return the summation and divide by the lenght
    # assume only int or float at this time
    return sum(list) / len(list)


average = Average(student_grades)

print(average)


student_grades = [9.1, 8.8, 7.5]
max_value = max(student_grades)
print(max_value)


student_grades = [9.1, 8.8, 10.0, 7.7, 6.8, 8.0, 10.0, 8.1, 10, 0, 9.9]
# will count the number of times a specified item appears in a list
count_value = student_grades.count(10.0)
print(count_value)

# produce lowercase
username = "Python3"
print(username.lower())


# dictionary, used to organize key value pairs
student_grades = {"Sam": 90, "Josh": 75, "Bob": 84, "Pete": 68}

print(student_grades["Sam"])

# will return the dict_values data type
print(student_grades.values())
# returns the k/v pairs
print(student_grades.items())


# to get the average of the scores
def Average(my_dictionary):
    # return the summation and divide by the lenght
    # assume only int or float at this time
    my_sum = sum(my_dictionary.values())
    calc_len = len(my_dictionary)

    return my_sum / calc_len


average = Average(student_grades)

print(average)

# temp
day_temperature = {"morning": 65.4, "noon": 70.2, "evening": 60.0}

temp_average = Average(day_temperature)

print(temp_average)


# tuples use (), lists use [], dictionaties use {}
temp = (1, 2, 3, 4)
# this will not work as tuples are immutable
# temp.append(5)
temp = [1, 2, 3, 4]
temp.append(5)
print(temp)

# complex dictionary
day_temps = {
    "morning": (66.1, 66.3, 64.0),
    "noon": (70.2, 71.5, 72.2),
    "evening": (67.2, 65.3, 64.1),
}


print(day_temps["morning"])
