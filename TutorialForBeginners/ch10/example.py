value = "y"
count = 0

# check if value exists
# evaluates to True because it exists
while value:
    count += 1
    print(count)
    if (count == 5):
        # exit the loop
        break
    else:
        # 0 = false whereas anything else is true
        value = 1
        # continue will still evaluate the while condition
        continue