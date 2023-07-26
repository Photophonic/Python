import re

message = 'call me at 913-333-4453 or 913-334-6322 or 816-999-3847'
phoneRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')

print(phoneRegex.findall(message))

#\d character class numeric digit, \D not numeric digit
#\w word characters \W not word
#\s space, tab, new line \S not <--

words = '12 words here, 11 songs there, 10 books up there, 9 things to do, 8 rabbits unde there, 7 blah'

# \d+ one or more digits, \s space, \w+ one or more letters
xmasRegex = re.compile(r'\d+\s\w+')
print(xmasRegex.findall(words))


wordz = '12 words here, 11 songs there, 10 books up there, 9 things to do, 8 rabbits unde there, 7 blah'

vowelRegex = re.compile(r'[aeiou]')
print(vowelRegex.findall(words))
