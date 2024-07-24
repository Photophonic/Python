num = 3
# int
print(type(num))

num = 3.11
# float
print(type(num))

# even or odd
num1 = 4
num2 = 2

# use modulo to check if 1 or 0 as remainder
if (num1 % num2) == 0:
    print("even")
else:
    print("odd")


num3 = 0

num3 += 1

print(num3)


num4 = -4
# absolute value
print(abs(num4))

# round, will round to the 2nd digit
print(round(8.3565462, 2))

if 3 == 2:
    print("test")
else:
    print("bummer")

if 3 >= 2:
    print("test")
else:
    print("bummer")


# casting
num1 = "100"
num2 = "200"
print(num1 + num2)
# String
print(type(num1))


num1 = int(num1)
num2 = int(num2)
# casts to int and returns 300
print(num1 + num2)
