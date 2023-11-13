myPets = ['Beryl', 'Zeros', 'Komi', 'Sebastion']

print('Enter a pet name: ')
name = input()

if name in myPets:
    print('We have the same pet!!!')
else:
    print(f'We do not have a pet with the name {name}.')
