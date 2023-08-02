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
