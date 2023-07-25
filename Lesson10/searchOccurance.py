import re

# ()? search 0 or 1 times
# ()* search ) or more
# ()+ search one or more, not optional
# {} multiple times
# {3,5} creates a range of 3 to 5 search matches


batRegex = re.compile(r'Bat(wo)?man')
mo = batRegex.search('The adventures of Batman!')

print(mo.group())

mo = batRegex.search('The adventurs of Batwoman!!')

print(mo.group())


# make the areacode search optional
phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
mo = phoneRegex.search('My phone number is 999-8888, call me tomorrow')
print(mo.group())


haRegex = re.compile(r'(Ha){3}')
mo = haRegex.search('He said HaHaHa.')
print(mo.group())
