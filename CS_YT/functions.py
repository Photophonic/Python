def test_func(val_in):
    # this allows to run without doing anything
    return "words" + str(val_in)


print(test_func(2))


def hello(greeting, name="Bob"):
    return greeting + " Bob."


print(hello("Hello"))


# Passing Defaults
def hello(greeting="morning", name="Bob"):
    return f"{greeting}, {name}!"


# *args (Non-Keyword Arguments)
# **kwargs (Keyword Arguments)


def student_info(*args, **kwargs):
    print(args)
    print(kwargs)


courses = ["Math", "Art"]
info = {"name": "John", "age": 22}

# this will unpack the values
# * will unpack the list, ** will unpack the dictionary
student_info(*courses, **info)

# list of days in month by position
month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def is_leap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def days_in_month(year, month):

    if not 1 <= month <= 12:
        return "Invalid Month"

    if month == 2 and is_leap(year):
        return 29

    return month_days[month]


print(days_in_month(2023, 2))
