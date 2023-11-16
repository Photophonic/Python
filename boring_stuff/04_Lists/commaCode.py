# comma code
def commaCode(listIn):
    # return a string with each item broken out:

    # create empty string
    item = ''

    # test to see if the list is null
    if len(listIn) > 0:
        # create loop to itterate equal to length -1
        for list in listIn[:-1]:
            # convert to string and add to string
            # add comma and a space
            item += str(list) + ', '
        # exit the loop append the last item of the list
        # include and (space) to the fron of item
        item += 'and ' + listIn[-1]
    # return the item to the calling function
    return item


myList = ['apples', 'bananas', 'tofu', 'cats']
zeroList = []
mixList = ['snake', 123, True, 'test']

print(commaCode(myList))
print(commaCode(zeroList))
print(commaCode(mixList))
