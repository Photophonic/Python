birthdays = {'Alice': 'Apr 1', 'Bob': 'Jan 1', 'Carol': 'Mar 4'}

while True:
    print('Enter a name: (blank to quit)')
    name = input()
    if name == '':
        break

    # check if the input value matches a dictionary key
    if name in birthdays:
        # use [key] to interact with the dictionary
        # will return the value of the entry
        print(birthdays[name] + ' is the birthday of ' + name)
    else:
        print('I do not have info on ' + name)
        print('What is their birthday?')
        # get the bday to serve as the value
        bday = input()
        # adds the value to the key stored in name
        # then updates the dictionary with the new info
        birthdays[name] = bday
        print('Birthday has been updates')
