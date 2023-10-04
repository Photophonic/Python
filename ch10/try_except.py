try:
    print(5/0)
except ZeroDivisionError:
    print('bummer')

print('Give me two numbers and I will divide them.')
print('Enter Q to quit')

while True:
    first_number = input("\nFirst Number: ")
    if first_number == 'Q':
        break
    second_number = input('\nSecond Number: ')
    if second_number == 'Q':
        break

    try:
        result = (int(first_number) / int(second_number))

    except ZeroDivisionError:
        print(f'\nCannot divide {first_number} by {second_number}')
    # moving the print statement to an else: line
    # can make the try block more error resistant
    else:
        print(result)
