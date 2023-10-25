from pathlib import Path

path = Path('Python/ch10/pi_million_digits.txt')

contents = path.read_text()
lines = contents.splitlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

birthday = input("Enter your birthday MMDDYY\n")

if birthday in pi_string:
    print(f'Your birthday {birthday} is found in Pi')
else:
    print(f'Your birthday {birthday} is not found in Pi.')
