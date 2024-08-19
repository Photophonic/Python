# Key/Value pairs
student = {"name": "Bob", "age": 37, "courses": ["Math", "Art"]}
print(student)
# To get a single value
print(student["name"])
# get the second coures from the list
print(student["courses"][1])

print(student.get("name"))
# to get with a default value
print(student.get("phone", "Not Found"))

# to add an item
student["phone"] = "913-333-5734"
print(student.get("phone", "Not Found"))
# this will update the value
student["phone"] = "913-333-9999"
print(student.get("phone", "Not Found"))
# to update multiple items at once, uses a dictionary as an argument
student.update({"name": "Bill", "phone": "785-256-8956"})
print(student)

# to delete a value
del student["phone"]
print(student)
# can use pop to remove a value and store it in a variable
age = student.pop("age")
print(age)
print(student)

student["age"] = 37

# returns the lenght of the dict
print(len(student))
# can use key(), values(), items() to get different output
for value in student.values():
    print(value)

for key, value in student.items():
    print(f"{key}: {value}")
