
def add_one(num):
 
    if (num >= 9):
        return  num + 1
  
    total = num + 1
    print(total)

    # call self with the return total value
    # will continue to call self until total = 9
    # do not forget to add return for recursive call
    return add_one(total) 

# will store the complete recusive call total
val = add_one(0)

# prints 10
print(val)

print("Loop version using while loop")
def loop_one(num):
    total = num

    while total <= 10:
        print(total)
        total += 1


loop_one(1)