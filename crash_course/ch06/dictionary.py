# example dictionary
# structured similar to JS objects
# they are a colection of key value pairs
alien01 = {'color': 'green',
           'points': 5,
           'fly?': True}

# accessing the property
print(alien01['color'])

# assign values to a variable to access them later
new_points = alien01['points']
print(f'You scored {new_points}!')

alien_color = alien01['color']
print(f"The alien's color is {alien_color}...")

# to add new values to an exisitng dictionary
print(alien01)
print('\n')
alien01['x_position'] = 0
alien01['y_position'] = 25
print(alien01)
print('\n')

# to start with an empty dictionary, leave the {} blank
alien00 = {}

# doing this will reference the original dictionay and any changes to one will impact the other
alien02 = alien01

alien01['isBoss'] = False
alien02['isBoss'] = True
print(alien01)
print(alien02)

# to modify values
alien00['color'] = 'green'
print(f'The alien color is {alien00["color"]}')
alien00['color'] = 'red'
print(f'The alien color is now {alien00["color"]}\n')


# anohter example
alien00 = {'x_axis': 0, 'y_axis': 25, 'speed': 'medium'}
print(alien00)

# use speed to determin how far it moves
if alien00['speed'] == 'slow':
    x_increment = 1
elif alien00['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

# += shorthand just like JS
alien00['x_axis'] += x_increment
print(f'Alien new x position is {alien00["x_axis"]}')

# to delete something from a dictionary
del alien02['isBoss']
print(alien02)

# using keys directly can lead to errors when attempting to retrieve values.
# print(alien00['isBoss']) -> throws error

# use .get() to access a dictionary, example similar to NVL
value = alien00.get('points', 'no points assigned')
print(value)  # retunrs 'no points assigned'

# Try it yourself
person = {'firstName': 'Bob', 'lastName': 'Dole', 'age': 98, 'city': 'Russell'}
print(f'{person["firstName"]} {person["lastName"]} is {person["age"]} and from {person["city"]}.')

numbers = {'person1': 1, 'person2': 83,
           'person3': 17, 'person4': 88, 'person5': 13}
print(numbers)

numbers['person6'] = 27
print(numbers)
del numbers['person3']

# Looping through pairs with a for loop
user_0 = {
    'username': 'bdole',
    'first': 'Bob',
    'last': 'Dole'
}
# you need to create variables for each k/v pair
# then use .items() returns a viewable object
for key, value in user_0.items():
    print(f'\nKey: {key}')
    print(f'Value: {value}')

# .keys() will return just the keys, .values() returns just values
for key in user_0.keys():
    print(f'\n{key}')

for value in user_0.values():
    print(f'\n{value}')

# sorted loops with dictionaries
for key, value in sorted(user_0.items()):
    print(f'\nKey: {key}')
    print(f'Value: {value}')


# sets do not have K/V pairs, just values
languages = {'python', 'rust', 'javascript', 'plsql', 'VB'}

languages = {'lang1': 'python', 'lang2': 'rust',
             'lang3': 'javascript', 'lang4': 'plsql', 'lang5': 'VB'}


for key, value in languages.items():
    print(key, value)

languages['lang6'] = 'C#'
languages['lang7'] = 'Java'

for key, value in languages.items():
    print(key, value)

print('\n')

rivers = {'nile': 'Egypt', 'amazon': 'South America', 'mississippi': 'US'}
for key, value in rivers.items():
    print(f'The {key.title()} runs through {value}')

for river in rivers.keys():
    print(river.title())

print('\n')

for country in rivers.values():
    print(country.title())

poll = {'Bob': True, 'Sam': False, 'Isaac': True,
        'Josh': True, 'Christian': False}

for key, value in poll.items():
    if value:
        print(f'{key} has taken the poll')
    else:
        print(f'{key} has not taken the poll yet')

print('\n')


# to make a list of lists, similar to nested arrays
alien_00 = {'color': 'red', 'points': 5, 'isBoss': False}
alien_01 = {'color': 'yellow', 'points': 5, 'isBoss': False}
alien_02 = {'color': 'gree', 'points': 10, 'isBoss': True}

aliens = [alien_00, alien_01, alien_02]

for alien in aliens:
    print(alien)

# example of making multiple aliens
# make an empy list

aliens = []

for alien_num in range(30):
    # create the new list in the loop and assign to variable
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    # use append method to add the new_alien to the empty list
    aliens.append(new_alien)


# to make the first three aliens different
for alien in aliens[0:3]:
    # check if the color is green, if not assign new values to each key in the list
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['points'] = 10
        alien['speed'] = 'medium'
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['points'] = 15
        alien['speed'] = 'fast'

for alien in aliens[:5]:
    print(alien)

# print length of the list
print(len(aliens))
print('\n')


# storing listss in dictionaries, similar to arrays in objects in JS
pizza = {
    'crust': 'honey wheat',
    'toppings': ['cheese', 'ham', 'pineapple'],
    'sauce': 'red'
}

# to print a dedicated item in the dictionary
print(pizza['toppings'])
print('\n')


# or loop through them
for topping in pizza['toppings']:
    print(topping)

# lists galor
favoriteLanguages = {
    'Bob': ['Unix Scripting'],
    'Christian': ['Ruby on Rails', 'JS'],
    'Billie': ['JS', 'Python', 'C#'],
    'Isaac': ['VB'],
    'Me': ['PLSQL', 'Python', 'JS']
}

# to loop through and get the key/value pairs and lopp the results
for name, languages in favoriteLanguages.items():
    # determine if they like more than one language
    if len(languages) > 1:
        print(f'{name} likes the following languages:')
        for language in languages:
            # \t is tab with .title() to capitalize
            print(f'\t{language.title()}')
    else:
        print(f'{name} likes the following language:')
        for language in languages:
            # \t is tab with .title() to capitalize
            print(f'\t{language.title()}')

# dictionay in dictionary, this gets complicatd quick
users = {
    'semarti': {
        'first': 'seth',
        'last': 'martin',
        'email': 'semarti@jocogov.org',
    },
    'bmaynard': {
        'first': 'bryan',
        'last': 'maynard',
        'email': 'bmaynard@jocogov.org',
    }
}

for username, user_info in users.items():
    print(f'\nUser Name: {username.title()}')
    fullname = f"{user_info['first']} {user_info['last']}"
    print(fullname.title())
