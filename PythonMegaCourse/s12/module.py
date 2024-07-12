username = "tacocat"

print(len(username))


# import time

# count = 0

# while count < 3:
#     with open("vegetables.txt") as my_file:
#         print(my_file.read())
#         my_file.seek(0)
#         time.sleep(3)
#     count += 1
# print("end of loop")


# use the os module

# run pip3 install panndas from CLI first

# import time, os

# while True:
#     if os.path.exists("vegetable.txt"):
#         with open("vegetable.txt") as file:
#             print(file.read())
#     else:
#         print("File not found")
#     time.sleep(3)


import time, os, pandas

path = "temps_today.csv"

while True:
    if os.path.exists(path):
        # this creates a dataframe
        data = pandas.read_csv(path)
        print(data.mean())
        # to print only station 1 column
        print(data.mean()["st1"])
    else:
        print("File not found")
    time.sleep(3)
