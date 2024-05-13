#  Global scope
name = 'Bob'

count = 1

# global scope function
def greeting(name):
    # Local scope, but has access to global
    # value of name will print due to global level
    print(name)

    # also local scope and cannot be accessed outside function
    color = "Blue"
    print(color)
    # local variable name will now be printed
    name = "Bill"
    print(name)
    print("")

    # this will result in an error out of scope
    # count += 1
    global count
    count += 1
    print(count)

greeting(name)  


def another():
    # call the greeting and pass in a new name
    # this will override the gloval value 
    greeting("Pete")
    

    color = "red"

    # function defined in the another scope
    def colors(color):
        print(color)

    # can only be called within anohter()
    colors(color)

another()

print(name)
print("")

# nonlocal will tell Python to use a value not local to the current scope

# VS code will help to ID scope by graying out variables based on current defined scope of items
