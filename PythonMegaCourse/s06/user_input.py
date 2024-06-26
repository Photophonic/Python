def weather_conditions(temp):

    if float(temp) > 75:
        return "Warm"
    else:
        return "Cold"


# get_temp = input("What is the weather?\n")

# print(weather_conditions(get_temp))


# def greeting(first_name, last_name):
#     return f"Hello {first_name} {last_name}!"


# first_name = input("What is your first name?\n")
# last_name = input("What is your last name?\n")
# print(greeting(first_name, last_name))


def greet_person(name):
    return f"Hi {name}"


print(greet_person("Person"))
