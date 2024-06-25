# creating our function
def mean(my_list):
    the_mean = sum(my_list) / len(my_list)
    return the_mean


test_list = (5, 2, 6, 7, 3, 6, 3, 9)

the_mean = mean(test_list)

print(the_mean)


def currency(amount):
    return amount * 1.75


print(currency(10.5))


def area_of_square(side):
    return side * side


print(area_of_square(7))
print(area_of_square(3))


def convert_liquid(fluid_ounces):
    return fluid_ounces * 29.57353


print(convert_liquid(1))
print(convert_liquid(5))


student_grades = {"Sam": 88, "Bob": 75, "Pete": 90}
monday_temps = [91.1, 88.8, 75.2]


# modify this to return if list or dictionary
def means(value):
    the_mean = ""
    # evaluate the data type of the value in.
    if type(value) == dict:
        # .values gets the value of the corresponding key pair
        the_mean = sum(value.values()) / len(value)
    else:
        the_mean = sum(value) / len(value)
    return the_mean


print(means(student_grades))
print(means(monday_temps))


def temp(my_temp):
    if my_temp > 7:
        return "Warm"
    else:
        return "Cold"


print(temp(6))
print(temp(9))


def passwords(value):
    if len(value) < 8:
        return False
    elif len(value) > 20:
        return False
    else:
        return True


print(passwords("mypass"))
print(passwords("mylongpassword"))
print(passwords("mylonglonglongpassword"))


x = -10
if x * 2 > x:
    print("Greater")
else:
    print("Less than")
