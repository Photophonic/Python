import re

message = 'Call me at 913-455-9438 tomorrow, or 816-433-7965 on the weekend'

phoneRegEx = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneRegEx.search(message)
print(mo.group())


print(phoneRegEx.findall(message))
