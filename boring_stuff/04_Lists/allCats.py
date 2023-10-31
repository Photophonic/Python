# app to ask for cat names and add them to a list
catNames = []

while True:
    # increment the prompt with the lenght of the list Cat 1, Cat 2....
    print('Enter the name of cat ' + str(len(catNames) + 1) +
          ' Or nothing to stop: ')
    name = input()
    # exit the loop if null
    if name == '':
        break
    # add the name to the list at the next index
    catNames = catNames + [name]

print('The cat names are: ')
# loop through the list and print the names
for name in catNames:
    print(' ' + name)
