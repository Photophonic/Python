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
