temps = [221, 234, 340, -9999, 230]

new_temps = []
for temp in temps:
    new_temps.append(temp / 10)

print("Loop: ", new_temps)


# using list comprehension
# implicit loop to create lists based off anohter list
new_temps = [temp / 10 for temp in temps]
print("list comprehension", new_temps)


# list comp with conditionals
new_temps = [temp / 10 for temp in temps if temp != -9999]
print("conditional list comprehension", new_temps)


# function with condition list comp
def list_convert(my_list):
    new_list = [item for item in my_list if type(item) == int]
    return new_list


mix_list = [99, "no data", 95, 92, "no data", 3]
print(list_convert(mix_list))


def only_positive(list_in):
    return [item for item in list_in if item > 0]


my_list = [-5, 2, 99, -100, 0, 55]
print(only_positive(my_list))


# when using an if-else in a list comp, the order of the loop needs to change
temps = [221, 234, 340, -9999, 230]
# the condictional must come before the loop
new_temps = [temp / 10 if temp != -9999 else 0 for temp in temps]

print(new_temps)


# replace the no data with 0
def convert_temp(list_in):
    # when replacing a value, set the desired item first
    new_list = [0 if item == "no data" else item for item in list_in]

    return new_list


# 'no data' will be replaced by the 0
this_list = [99, "no data", 95, 94, "no data"]

print(convert_temp(this_list))


# convert and sum a list
def sum_list(list_in):
    new_list = [float(i) for i in list_in]
    return sum(new_list)


my_list = ["1.2", "2.6", "3.3"]

print(sum_list(my_list))
print(type(sum_list(my_list)))
