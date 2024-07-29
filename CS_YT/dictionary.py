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
