# Lists

bourbon = ['4Roses', 'Buffalo Trace', 'weller', 'Makers Mark']
print(bourbon)
# Access an element just like an array in JS
print(bourbon[2].title())
# call the last element in a list
print(bourbon[-1])

message = (f"My favorite bourbon is {bourbon[-1].title()}")
print(message)

motorcycles = ['Honda', 'Yamaha', 'Triumph', 'Ural', 'BMW']
print(motorcycles)
motorcycles[-1] = 'Suzuki'
print(motorcycles)
# This will add an a new element to the end of the list
motorcycles.append('BMW')
print(motorcycles)

# To insert into a position
motorcycles.insert(1, 'Matchless')
print(motorcycles)

# To delete an element, -2 = second from last elemet
del motorcycles[-2]
print(motorcycles)

# pop removes an element but allows you to still work with it after
popMC = motorcycles.pop(-1)
motorcycles.insert(0, popMC)
print(motorcycles)

# use the remove method if you are not sure of the index location
motorcycles.remove('BMW')
print(motorcycles)


guestList = ['Bob', 'Isaac', 'Shannon', 'Kelly', 'Kari']
print(f"{guestList} is invited for dinner at our place")
print(f"Oh no {guestList[2]} cannot make it!")
guestList[2] = 'Cory'
print(f"{guestList} is invited for dinner at our place")
guestList.insert(0, 'Ben')
guestList.insert(3, 'Mitch')
guestList.append('Dawn')
print(
    f"we found a bigger table and can add 3 more people {guestList[0], guestList[3], guestList[-1]} are now invited")
print(guestList)

print("Oh crap, only room for 2 people, so sorry folks")
listLen = (len(guestList)-2)

print(listLen)

for i in range(listLen):
    popList = guestList.pop(0)
    print(f'{popList} has been uninvited for dinner')

print(guestList)

del guestList[-1]
del guestList[0]
print(guestList)


cars = ['BMW', 'Toyota', 'Audi', 'Subaru', 'Honda']
# cars.sort()
print(cars)

# use sorted to temp sort the list, retaining the original order
print('Here is a list of cars')
print(cars)
print("n\Here is a sorted list")
print(sorted(cars))
print("n\Here is the reverse list")
print(sorted(cars, reverse=True))
print("n\Here is the list back to normal")
print(cars)
print(len(cars))
