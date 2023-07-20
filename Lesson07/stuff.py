Python 3.11.4 (v3.11.4:d2340ef257, Jun  6 2023, 19:15:51) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
'Hell'
'Hell'
'Hello'
'Hello'
'That\'s'
"That's"
"That's"
"That's"
print('Hello there! \n Nice weather')
Hello there! 
 Nice weather
r'Hello that\'s a nice cat'
"Hello that\\'s a nice cat"
print(r'Hello that\'s a nice cat\n')
Hello that\'s a nice cat\n
print ('''Hi there
this is a multiline comment
see look at the lines''')
Hi there
this is a multiline comment
see look at the lines
'My list item'
'My list item'
myString = 'My string is here'
myString[0]
'M'
'Hello' in myString
False
newString = 'I am now upper'
newString
'I am now upper'
newString.upper()
'I AM NOW UPPER'
answer = input()
YES
answer
'YES'
if answer == 'yes':
    print('Playing again?')

    
if answer.lower()=='yes':
    print('Playing again?')

    
Playing again?
answer.isUpper()
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    answer.isUpper()
AttributeError: 'str' object has no attribute 'isUpper'. Did you mean: 'isupper'?
answer.isupper()
True
answer.isLower()
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    answer.isLower()
AttributeError: 'str' object has no attribute 'isLower'. Did you mean: 'islower'?
answer.islower()
False
answer.upper().isupper()
True
answer.lower().islower()
True
answer.istitle()
False
>>> answer.istitle('yes')
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    answer.istitle('yes')
TypeError: str.istitle() takes no arguments (1 given)
>>> newString
'I am now upper'
>>> newString.startswith('I')
True
>>> newString.endswith('pper')
True
>>> ','.join('cats','rats','bats')
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    ','.join('cats','rats','bats')
TypeError: str.join() takes exactly one argument (3 given)
>>> ','.join(['cats','rats','bats'])
'cats,rats,bats'
>>> 'This is a split method string'.split()
['This', 'is', 'a', 'split', 'method', 'string']
>>> ['This', 'is', 'a', 'split', 'method', 'string']
['This', 'is', 'a', 'split', 'method', 'string']
>>> 'Hello'+' this string'
'Hello this string'
>>> name = 'Alice'
>>> place = 'main street'
>>> food = 'Pizza'
>>> large string = name +' you are invited at '+place +' to enjoy '+food
SyntaxError: invalid syntax
>>> largeString = name +' you are invited at '+place +' to enjoy '+food
>>> largeString
'Alice you are invited at main street to enjoy Pizza'
>>> largeString = 'Hello, %s, you are invited to %s to enjoy %s.'%(name, place, food)
>>> 
>>> 
>>> largeString
'Hello, Alice, you are invited to main street to enjoy Pizza.'
