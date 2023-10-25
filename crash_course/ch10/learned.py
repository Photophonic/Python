from pathlib import Path

path = Path('Python/ch10/stuff.txt')

contents = path.read_text()

print(contents)

lines = contents.splitlines()
my_lines = ''

for line in lines:
    # to add a space bewtween each part
    my_lines += (line+' ')  # .lstrip()

print(my_lines)

# use .repace('word','new word) to replace an item in text
modifiied_lines = my_lines.replace('Python', 'Pasta')

print(modifiied_lines)

# use .wrtie_text(something) on the path to output the text
path.write_text(modifiied_lines)


modifiied_lines = my_lines.replace('Pasta', 'Python')

print(modifiied_lines)

path.write_text(modifiied_lines)
