# Dictionary
vehicle = {
    "type":"suv",
    "make":"Toyota",
    "model":"4Runner"
}

vehicle2 = dict(type="car", make="Toyota", model="GR86")

print(vehicle)
print(type(vehicle))
print(len(vehicle))
print(vehicle2)

# accessing items in a dictionary
print(vehicle["model"])
# or via method
print(vehicle.get("make"))

# to list all keys or values
print(vehicle.keys())
print(vehicle.values())

# return as tuples, will return K/V pairs
print(vehicle.items())

# verify if a key exists in the dictionary
print("type" in vehicle)
# verify is value is in the dictionary 
print("Toyota" in vehicle["make"])

# change values
vehicle2['model'] = 'Corolla GR'
# add an item to a dictionary
vehicle2.update({"transmission":"manual"})
print(vehicle2)

print(vehicle2.pop("transmission"))
# can use .popitem to remove the last K/V item, 
# returns a tuple

vehicle2.clear() #empty the dictionary
print(vehicle2)

# this creates a reference, not a copy, do not do this
# vehicle2 = vehicle

# the proper way to create a copy
new_vehicle = vehicle.copy()
# add a new K/V to the new dictiopnary
new_vehicle["color"] = 'Red'

print(new_vehicle)

# copy using the constructor function
other_vehicle = dict(vehicle)
print(other_vehicle)



# nested dictionaries, the value of a K/V is another dict
member1 = {
    'name':'plant',
    'role ':'dude'
}
member2 = {
    'name':'tree',
    'role':'chill'
}
group = {
    "member1":member1,
    "member2":member2
}

# must burrow down [X][Y] to access the data in the nested pair
print(group["member1"]["name"])



# Sets, does not allow duplicates, will also order the content
nums = {1,2,3,4}

nums2 = set((1,2,3,3,4,4,5))

print(nums)
print(nums2)
print(type(nums))
print(len(nums))

# will remove True and 0 because those are boolean dups.
nums3 = {1,True,2,False, 3,4,0}
print(nums3)

# to add to a set use .add(X) method
nums.add(23)
print(nums)

# to add one set to another
nums.update(nums2)

print(nums)


# to merge sets
one = {1,2,3}
two = {3,4,5,6,7}

newset = one.union(two)
print(newset)

# to keep the duplicates
one = {1,2,3,4,5}
two = {3,4,5,6,7}

one.intersection_update(two)
print(one)

